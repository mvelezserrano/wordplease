"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from blogs.api import BlogListAPI, PostListAPI
from django.conf.urls import include, url
from django.contrib import admin
from blogs.views import HomeView, BlogsView, UserPostsView, DetailView, CreateView#, PostListView
from users.api import UserListAPI, UserDetailAPI
from users.views import LoginView, LogoutView, SignUpView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Blogs URLs
    url(r'^$', HomeView.as_view(), name='blogs_home'),
    url(r'^blogs/$', BlogsView.as_view(), name='blogs_list'),
    #url(r'^blogs/all-posts/$', PostListView.as_view(), name='posts_list'),
    url(r'^blogs/(?P<user>[A-Za-z0-9]+)$', UserPostsView.as_view(), name='user_posts'),
    url(r'^blogs/(?P<user>[A-Za-z0-9]+)/(?P<pk>[0-9]+)$', DetailView.as_view(), name='post_detail'),
    url(r'^blogs/new-post$', CreateView.as_view(), name='create_post'),

    # Blogs API URLs
    url(r'^api/1.0/blogs/$', BlogListAPI.as_view(), name='blog_list_api'),
    url(r'^api/1.0/blogs/(?P<user>[A-Za-z0-9]+)$', PostListAPI.as_view(), name='post_list_api'),

    # Users URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^signup$', SignUpView.as_view(), name='users_signup'),

    # Users API URLs
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api')
]
