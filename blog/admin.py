from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'cuisines_type', 'status', 'created_on')
    search_fields = ['title', 'description', 'ingredients', 'cuisines_type', 'status']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('ingredients', 'instructions')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('comment_author', 'recipe', 'comment_body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('comment_author', 'comment_body')
    actions = ['approve_comments']












# admin.site.register(Comment)
