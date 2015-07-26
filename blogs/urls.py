# -*- coding: utf-8 -*-

from django.conf.urls import url
from blogs.views import HomeView, BlogsView, UserPostsView, DetailView, CreateView

urlpatterns = [

    # Blogs URLs
    url(r'^$', HomeView.as_view(), name='blogs_home'),
    url(r'^blogs/$', BlogsView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<user>[A-Za-z0-9]+)$', UserPostsView.as_view(), name='user_posts'),
    url(r'^blogs/(?P<user>[A-Za-z0-9]+)/(?P<pk>[0-9]+)$', DetailView.as_view(), name='post_detail'),
    url(r'^blogs/new-post$', CreateView.as_view(), name='create_post'),
]