from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (TemplateView, CreateView, ListView, DetailView, DeleteView)
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm


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
        return Recipe.objects.filter(status=1)


class RecipeDetail(DetailView):
    """
    Class based view to display the recipe details
    """
    template_name = "blog/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    View to add/create recipes
    """
    template_name = "blog/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your recipe has been posted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super(AddRecipe, self).form_valid(form)


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View to delete recipe
    """
    model = Recipe
    success_url = '/blog/'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_object(self, queryset=None):
        recipe_id = self.kwargs.get('recipe_id')
        return Recipe.objects.get(pk=recipe_id)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your recipe has been deleted successfully.")
        return super().delete(request, *args, **kwargs)
        








