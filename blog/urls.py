from django.urls import path
from . import views
from .views import IndexView, RecipeList


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipes/', RecipeList.as_view(), name='recipes'),
    # path('<slug:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
    # path('delete/<slug:pk>/', DeleteRecipe.as_view(), name='delete_recipe'),
    # path('edit/<slug:pk>/', UpdateRecipe.as_view(), name='update_recipe'),
    # path('addrecipe/', AddRecipe.as_view(), name='add_recipe')    
]