# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter, SimpleRouter
from users.api import UserViewSet

# APIRouter
router = DefaultRouter()
router = SimpleRouter(trailing_slash=False)

router.register(r'users', UserViewSet, base_name='user')

urlpatterns = [

    # API URLs
    url(r'1.0/', include(router.urls)),
]
