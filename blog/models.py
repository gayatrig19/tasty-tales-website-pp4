from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator


CUISINES_TYPE = (
    ("american", "American"),
    ("african", "African"),
    ("asian", "Asian"),
    ("caribbean", "Caribbean"),
    ("chinese", "Chinese"),
    ("european", "European"),
    ("indian", "Indian"),
    ("indonesian", "Indonesian"),
    ("latin_american", "Latin American"),
    ("middle_eastern", "Middle Eastern"),
    ("mexican", "Mexican"),
    ("oceanic", "Oceanic"),       
)

STATUS = ((0, "Draft"), (1, "Published"))


def validate_nonzero(value):
    """
    Function to validate prep_time, cooking_time and servings
    field values.
    """
    if value == 0:
        raise ValidationError(
            ('Please enter a value that is greater than zero'),
            params={'value': value},
        )

class Recipe(models.Model):
    """
    A model to create and display recipes added by users.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_owner')
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=700, null=False, blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, default=None, blank=True,
                                   related_name='recipe_likes')
    prep_time = models.PositiveIntegerField(
        'prep_time', validators=[validate_nonzero, MaxValueValidator(300)], default=15)                              
    cooking_time = models.PositiveIntegerField(
        'cooking_time', validators=[
            validate_nonzero, MaxValueValidator(600)], default=15)
    servings = models.PositiveIntegerField(
        'servings', validators=[validate_nonzero, MaxValueValidator(50)])
    cuisines_type = models.CharField(
        max_length=60, choices=CUISINES_TYPE, default="Asian"
    )

    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title} | written by {self.author}'

    def total_num_of_likes(self):
        return self.likes.count()



class Comment(models.Model):
    """
    A Comment Model to create and handle comments added by users
    Before the comment is published, it needs to be approved by admin
    """

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment by {self.comment_author}"
    




