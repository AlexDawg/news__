from django.contrib import admin
from .models import Post, PostCategory, Category, CategorySubscribe, Author

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(CategorySubscribe)
admin.site.register(Author)
# Register your models here.
