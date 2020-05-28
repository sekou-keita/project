from django.urls import path 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    
    path('Post/<int:pk>/', PostDetailView.as_view(), name='post-Detail'),
    path('Post/new/', PostCreateView.as_view(), name='post-Create'),
    path('Post/<int:pk>/Update/', PostUpdateView.as_view(), name='post-Update'),
    path('Post/<int:pk>/Delete/', PostDeleteView.as_view(), name='post-Delete'),
    path('about/', views.about, name='blog-about'),
    path('', PostListView.as_view(), name='blog-home'),
]

