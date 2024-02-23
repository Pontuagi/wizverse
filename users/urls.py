from django.urls import path
from . import views
from .views import PostListView, PostCreateView

urlpatterns = [
    path('home', PostListView.as_view(), name='home'),
    path('', views.landing, name='landing'),
    path('create/', PostCreateView.as_view(), name='createPost'),
]