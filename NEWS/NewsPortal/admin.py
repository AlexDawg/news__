from django.contrib import admin
from .models import Post, PostCategory, Category, CategorySubscribe

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(CategorySubscribe)
# Register your models here.
