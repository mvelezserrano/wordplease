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


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('owner',)


class PostListSerializer(PostDetailSerializer):

    class Meta(PostDetailSerializer.Meta):
        fields = ('title', 'image_url', 'summary', 'pub_date')
