from django.urls import path
from .views import PostCreate, PostDelete, PostList, PostDetail, PostUpdate, PostSearch

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', PostCreate.as_view(), name='news_edit'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('article/create/', PostCreate.as_view(), name='article_edit'),
    path('article/<int:pk>/update/', PostUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),

]