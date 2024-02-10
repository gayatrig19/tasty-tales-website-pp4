from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Recipe(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_owner')
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500, null=False, blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, default=None, blank=True,
                                   related_name='recipe_likes')
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title} | written by {self.author}'

    def total_num_of_likes(self):
        return self.likes.count()




class Comment(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment by {self.comment_author}"
    




