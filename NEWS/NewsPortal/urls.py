from django.urls import path
from .views import PostCreate, PostDelete, PostList, PostDetail, PostUpdate, PostSearch, CategoryList, CategoryPost, subscribe_to_category

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
    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryPost.as_view(), name='category_post'),
    path('category/<int:pk>/subscribe', subscribe_to_category),

]