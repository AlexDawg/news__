from datetime import datetime
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, resolve
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2


class PostDetail(DetailView):
    model = Post
    template_name = 'some_news.html'
    context_object_name = 'some_news'
# Create your views here.


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')


    def form_valid(self, form):
        post = form.save(commit=False)
        http_info = resolve(self.request.path).url_name
        if http_info == 'news_edit' or http_info == 'news_update' or http_info == 'news_delete':
            post.type = 'NW'
        elif http_info == 'article_edit' or http_info == 'article_update' or http_info == 'article_delete':
            post.type = 'AR'
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_update.html'
    success_url = reverse_lazy('post_detail')
    login_url = '/login/'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
        # context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context



