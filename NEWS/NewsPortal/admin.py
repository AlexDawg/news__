from django.contrib import admin
from .models import Post, PostCategory, Category

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostCategory)
# Register your models here.
