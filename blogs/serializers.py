# -*- coding: utf-8 -*-
from blogs.models import Post
from django.contrib.auth.models import User
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):

    blogname = serializers.SerializerMethodField('username')
    url = serializers.SerializerMethodField('blogURL')

    class Meta:
        model = User
        fields = ('blogname','url')

    def username(self, obj):
        return obj.username

    def blogURL(self, obj):
        url = "/blogs/" + obj.username
        return url


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'image_url', 'summary', 'pub_date')
