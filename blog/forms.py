from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """
    Form to create/add new recipes
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description', 
            'featured_image', 
            'ingredients', 
            'instructions', 
            'prep_time',
            'cooking_time', 
            'servings', 
            'cuisines_type',
            'status', 
        ]

        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe your recipe here'}),
        }

        labels = {
            'title': 'Recipe Title',
            'description': 'Description',
            'featured_image': 'Recipe Image',
            'ingredients': 'Recipe Ingredients',
            'instructions': 'Recipe Instructions',
            'prep_time': 'Preparation Time',
            'cooking_time': 'Cooking Time', 
            'servings': 'Servings', 
            'cuisines_type': 'Cuisine Type',
            'status': 'Status',
        }


