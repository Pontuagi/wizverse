from django.urls import path
from . import views
from .views import PostListView, PostCreateView, AddCommentView, agree_post, disagree_post, post_detail
from .views import DashboardView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('home', PostListView.as_view(), name='home'),
    path('', views.landing, name='landing'),
    path('create/', PostCreateView.as_view(), name='createPost'),
    path('post/<int:post_id>/agree/', agree_post, name='agree_post'),
    path('post/<int:post_id>/disagree/', disagree_post, name='disagree_post'),
    path('post_detail/<int:tweet_id>/', post_detail, name='post_detail'),
    path('add_comment/<int:tweet_id>/', AddCommentView.as_view(), name='add_comment'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]