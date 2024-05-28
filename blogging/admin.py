from django.contrib import admin

# Register your models here.
# a new import
from blogging.models import Post, Category, PostAdmin, CategoryAdmin


# and a new admin registration
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
