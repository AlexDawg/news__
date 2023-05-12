from datetime import datetime
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, resolve
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from requests import request

from .models import Post, PostCategory, Category
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2


class PostDetail(DetailView):
    model = Post
    template_name = 'some_news.html'
    context_object_name = 'some_news'


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')
    permission_required = ('NewsPortal.add_post', )

    def form_valid(self, form):
        post = form.save(commit=False)
        http_info = resolve(self.request.path).url_name
        if http_info == 'news_edit' or http_info == 'news_update' or http_info == 'news_delete':
            post.type = 'NW'
        elif http_info == 'article_edit' or http_info == 'article_update' or http_info == 'article_delete':
            post.type = 'AR'
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_update.html'
    success_url = reverse_lazy('post_detail')
    permission_required = ('NewsPortal.change_post', )


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
        # context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class CategoryList(ListView):
    model = Category
    ordering = 'name_category'
    template_name = 'category_list.html'
    context_object_name = 'category'


class CategoryPost(DetailView):
    model = Category
    template_name = 'post_category.html'
    context_object_name = 'postcategory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.categories.filter(categories=kwargs['pk'])
        return context

