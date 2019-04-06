# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-03-31 00:26:01
# @Last Modified by:   vishalgupta07
# @Last Modified time: 2019-04-06 11:05:42
from django.urls import path
from .views import (PostListView,
 PostDetailView, 
 PostCreateView, 
 PostUpdateView, 
 PostDeleteView, 
 UserPostListView, 
 EventListView, 
 EventCreateView, 
 EventDetailView,
 EventUpdateView, 
 EventDeleteView)
from . import views
urlpatterns = [
    path('post/', PostListView.as_view(), name='post-home'),
    path('event/', EventListView.as_view(), name='event-home'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

    path('',views.home,name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]

# <app>/<model>_<viewtype>.html/
