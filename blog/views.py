from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, CreateView)
from .models import Recipe
from .forms import RecipeForm


class IndexView(TemplateView):
    """
    View to display home page
    """
    template_name = 'blog/index.html'


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    View to add/create recipes
    """
    template_name = 'blog/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)







