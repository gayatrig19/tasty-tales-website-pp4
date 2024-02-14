from django.urls import path
from . import views
from .views import AddRecipe, IndexView, RecipeList, RecipeDetail


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipes/', RecipeList.as_view(), name='recipes'),
    path('<int:pk>/', RecipeDetail.as_view, name='recipe_detail'),
    path('addrecipe/', AddRecipe.as_view(), name='add_recipe')    
]