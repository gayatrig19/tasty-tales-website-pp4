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
            'ingredients': SummernoteWidget(
                attrs={'placeholder': 'Please write one ingredient per line'}),
            'instructions': SummernoteWidget(), 
            'description': forms.Textarea(
                attrs={'rows': 5, 'placeholder': 'Describe your recipe in short here'}),
            'prep_time': forms.NumberInput(
                attrs={'placeholder': 'Preparation time is counted in minutes'}),
            'cooking_time': forms.NumberInput(
                attrs={'placeholder': 'Cooking time is counted in minutes'}),
            'servings': forms.NumberInput(attrs={'placeholder': 'Number of Servings'})
        }

        labels = {
            'title': 'Recipe Title',
            'description': 'Description',
            'featured_image': 'Recipe Image',
            'ingredients': 'Recipe Ingredients',
            'instructions': 'Recipe Instructions',
            'prep_time': 'Preparation Time (time in minutes)',
            'cooking_time': 'Cooking Time (time in minutes)', 
            'servings': 'Servings', 
            'cuisines_type': 'Cuisine Type',
            'status': 'Status (Save as a Draft / Publish Now)',
        }


