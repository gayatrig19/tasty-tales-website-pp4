from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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

    def get_query(self):
        return Recipe.objects.filter(status=1).order_by('-created_on')


class RecipeDetail(View):
    """
    Class based view to display the recipe details
    """
    # template_name = "blog/recipe_detail.html"
    # model = Recipe
    # context_object_name = "recipe"

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

   
        








