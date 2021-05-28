from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog_index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('', views.post_index, name='blog_index'),
    # path('post/<int:pk>/', views.post_detail, name='blog_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("<category>/", views.blog_category, name="blog_category"),
]