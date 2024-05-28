from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.contrib import admin


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories' 

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class PostInline(admin.TabularInline):
    model = Post 

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
    inlines = [
        PostInline,
    ]

