# -*- coding: utf-8 -*-

from blogs.api import BlogListAPI, PostViewSet, CreatePostViewSet
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter, SimpleRouter

# APIRouter
router = DefaultRouter()
router = SimpleRouter(trailing_slash=False)

router.register(r'blogs/(?P<user>[A-Za-z0-9]+)', PostViewSet)
router.register(r'blogs/new-post', CreatePostViewSet) # para la creación

urlpatterns = [
    # API URLs
    url(r'1.0/blogs/$', BlogListAPI.as_view(), name='blog_list_api'),
    url(r'1.0/', include(router.urls)),
]