from django.urls import path
from . import views
from .views import IndexView, RecipeList, RecipeDetail, AddRecipe, UpdateRecipe, DeleteRecipe


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipes/', RecipeList.as_view(), name='recipes'),
     path('add_recipe/', AddRecipe.as_view(), name='add_recipe'), 
    path('<slug:slug>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('edit_recipe/<slug:slug>/', UpdateRecipe.as_view(), name='update_recipe'),
    path('delete_recipe/<slug:slug>/', DeleteRecipe.as_view(), name='delete_recipe'),
   
       
]