from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView)
from .models import Recipe


class IndexView(TemplateView):
    """
    View to display home page
    """
    template_name = 'blog/index.html'


class AddRecipe(CreateView):
    """
    View to add/create recipes
    """
    template_name = 'blog/add_recipe.html'
    model = Recipe
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)







