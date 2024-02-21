from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import (
    TemplateView, CreateView, ListView, DeleteView, UpdateView)
from django.contrib import messages
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.urls import reverse_lazy


class IndexView(TemplateView):
    """
    View to display home page
    """
    template_name = "blog/index.html"


class RecipeList(ListView):
    """
    Class based view to display list of recipes
    """
    template_name = "blog/recipes.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(status=1).order_by('-created_on')


class RecipeDetail(View):
    """
    View to render recipe detail
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.comment_author = self.request.user
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your Comment is submitted successfully and awaiting approval'
            )
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )



class AddRecipe(LoginRequiredMixin, CreateView):
    """
    View to add/create recipes
    """
    model = Recipe
    form_class = RecipeForm
    template_name = "blog/add_recipe.html"
    success_url = reverse_lazy('recipes')


    # Source: https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post #noqa
    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your recipe has been posted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super(AddRecipe, self).form_valid(form)


class UpdateRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to edit recipe
    """
    model = Recipe
    form_class = RecipeForm
    template_name = "blog/update_recipe.html"
    success_url = reverse_lazy('recipes')
   

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your recipe has been updated successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


    
class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View to delete recipe
    """
    model = Recipe
    success_url = reverse_lazy('recipes')

    def test_func(self):
        return self.request.user == self.get_object().author
      
    def form_valid(self, request, *args, **kwargs):
        success_message = "Your recipe has been deleted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().delete(request, *args, **kwargs)



class RecipeLike(View):

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))



class UserDrafts(ListView):
    """
    Class based views to view users own recipes
    """

    template_name = "blog/my_drafts.html"
    model = Recipe
    context_object_name = "recipe_drafts"
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user, status=0)
       

        








