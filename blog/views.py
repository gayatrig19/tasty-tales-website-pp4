from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm


class IndexView(TemplateView):
    """
    View to display home page
    """
    template_name = 'blog/index.html'


class RecipeList(ListView):
    """
    Class based view to display list of recipes
    """
    template_name = 'blog/recipes.html'
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 6

    def get_query(self):
        return Recipe.objects.filter(status=1)


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







