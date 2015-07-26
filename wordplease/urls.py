# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from users import urls as users_urls, api_urls as users_api_urls
from blogs import urls as blogs_urls, api_urls as blogs_api_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Users URLs
    url(r'', include(users_urls)),
    url(r'api/', include(users_api_urls)),

    # Photos URLs
    url(r'', include(blogs_urls)),
    url(r'api/', include(blogs_api_urls))
]