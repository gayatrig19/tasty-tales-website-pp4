from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import (
    TemplateView, CreateView, ListView, DeleteView, UpdateView)
from django.db.models import Q
from django.contrib import messages
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm


class IndexView(TemplateView):
    """
    View to display home page.
    """
    template_name = "blog/index.html"


class RecipeList(ListView):
    """
    Class based view to display list of published recipes.
    Displays 6 recipes per page, filtered to show only
    recipes with a status of 'published',
    The recipes are ordered by the date they are created,
    with the latest ones appearing first.

    """
    template_name = "blog/recipes.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 6

    def get_queryset(self):
        """
        Retrieve the queryset of published recipes ordered
        by created date.
        """
        return Recipe.objects.filter(status=1).order_by('-created_on')


class RecipeDetail(View):
    """
    View to render recipe in detail.
    Allows logged-in users to leave comment.
    Retrieves info about comments and likes
    Handles comment form submission when valid and displays
    success message to user.
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
    Class based view to add/create recipes
    Requires user to be logged in.
    On successful form submission, redirects to the 'recipes' page.
    If the form is valid, sets the author of the recipe
    to the current logged-in user.
    Displays a success message to the user.
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
    Class based view to edit/update recipe
    Requires the user to be logged in and be the author of the recipe.
    On successful form submission, redirects to the 'recipes' page.
    Handles the form submission when valid.
    Displays a success message to the user
    on successful update.
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
    Class based view to delete recipe.
    Checks if the user is authorised to delete recipe.
    Manages delete request and override form_valid to
    displays a success message to user after successful deletion.
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
    """
    View to handle like/unlike recipe.
    Allows only logged-in users to like/unlike the recipe.
    Checks if the user has liked/unliked the recipe.
    Adds like if not/ removes like if yes
    Redirects user back to same page.
    """

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user) 
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class UserDrafts(ListView):
    """
    Class based view to display user's draft recipes.
    Displays drafts created by the currently logged-in user.
    Only visible to the draft author.
    Returns a list of recipes with status of 'draft'.
    Displays 6 recipes per page.
    """

    template_name = "blog/my_drafts.html"
    model = Recipe
    context_object_name = "recipe_drafts"
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user, status=0)
       
        
class RecipeSearchList(ListView):
    """
    View to display a list of recipes based on user search.
    Searches for recipes based on title, cuisine type, and description.
    Retrieves search for only recipes with status 'published'.
    Displays 6 recipes per page.
    """
    model = Recipe
    template_name = 'blog/recipe_search.html'
    context_object_name = 'recipes'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(cuisines_type__icontains=query) |
                Q(description__icontains=query),
                status=1  
            ).order_by('-created_on')
        else:
            queryset = Recipe.objects.none()
        return queryset

