from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.http import HttpResponseRedirect, HttpRequest, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.template.loader import render_to_string
from django.urls import reverse_lazy, resolve, reverse
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from requests import request
from django.contrib.auth.models import User
from .models import Post, PostCategory, Category, CategorySubscribe
from .filters import PostFilter
from .forms import PostForm
from NEWS import settings


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
        author = self.request.user
        now = timezone.now()
        since_24_hours = now - timezone.timedelta(days=1)
        posts_count = Post.objects.filter(author=author, time_in__gte=since_24_hours).count()
        if posts_count >= 3:
            return HttpResponseBadRequest(f'{self.request.user.username}, Вы превысили лимит по количеству создаваемых'
                                          f' постов в сутки.')
        else:
            response = super().form_valid(form)
            post = self.object
            post_url = self.request.build_absolute_uri(reverse('post_detail', args=[post.pk]))
            categories = post.categories.all()
            category_name = []
            subscribers_emails = []

            for category in categories:
                category_name.append(category.name_category)
                subscriber = category.subscribers.all()
                subscribers_emails += [sub.email for sub in subscriber]


            send_mail(
                subject=f'{post.title}"{category_name}"',
                message=f'Здравствуй {self.request.user.username}. Новая статья в твоём любимом разделе! {post.text[:50]}\n\n Ссылка на новый пост: {post_url}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=subscribers_emails,
            )
            return response



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
        context['posts'] = Post.objects.filter(categories=kwargs['object'])
        return context

#class CategorySubscribed(View):
#    model = User
#    context_object_name = 'subscribe'
#
#    def get_subscribed(self, request):
#        user = request.user
#        if not Category.objects.filter(subscribers=user).exists():
#            Category.subscribers.add(request.user)
#        return redirect('category_post')
#
#    def post(self, request, *args, **kwargs):
#        self.get_subscribed(request)
#        print()
#        return super().post(request, *args, **kwargs)


def subscribe_to_category(request, pk):

    current_user = request.user
    CategorySubscribe.objects.create(category=Category.objects.get(pk=pk), subscriber=User.objects.get(pk=current_user.id))

    return render(request, 'subscribed.html')


def posts_created_last_week(request):
    now = timezone.now()
    since_one_week = now - timezone.timedelta(weeks=1)
    posts = Post.objects.filter(time_in__gte=since_one_week).order_by('-time_in')

    context = {
        'posts': posts,
    }

    return render(request, 'post_created_last_week.html', context)