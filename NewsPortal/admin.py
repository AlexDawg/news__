from django.contrib import admin
from .models import Post, PostCategory, Category, CategorySubscribe, Author

admin.site.register(Post)
admin.site.register(Category)
# Register your models here.
