from .models import Recipe, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class RecipeForm(forms.ModelForm):
    """
    Recipe Form to create/add new recipes
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
            'description': forms.Textarea(
                attrs={'rows': 5, 'placeholder': 'Describe your recipe here'}),
            'prep_time': forms.NumberInput(
                attrs={'placeholder':
                       'Preparation time is counted in minutes'}),
            'cooking_time': forms.NumberInput(
                attrs={'placeholder':
                       'Cooking time is counted in minutes'}),
            'servings': forms.NumberInput(
                attrs={'placeholder': 'Number of Servings'})
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


class CommentForm(forms.ModelForm):
    """
    Comment Form to add comments
    """
    class Meta:
        model = Comment
        fields = ('comment_body',)

        labels = {
            'comment_body': 'Leave your comment here',
        }
