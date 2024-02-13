from django.urls import path
from . import views
from .views import AddRecipe, IndexView, RecipeList


urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipes'),
    path('addrecipe/', AddRecipe.as_view(), name='add_recipe'),
    path('', IndexView.as_view(), name='index')
]