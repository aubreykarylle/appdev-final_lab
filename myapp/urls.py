from django.urls import path
from .views import PostListView, PostDetailView, create_post

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create_post/', create_post, name='create-post')
]
