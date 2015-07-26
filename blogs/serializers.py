# -*- coding: utf-8 -*-
from blogs.models import Post
from django.contrib.auth.models import User
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):

    blogname = serializers.SerializerMethodField('username')
    url = serializers.SerializerMethodField('blogURL')
    number_of_posts = serializers.SerializerMethodField('numberOfPosts')

    class Meta:
        model = User
        fields = ('blogname', 'url', 'number_of_posts')

    def username(self, obj):
        return obj.username

    def blogURL(self, obj):
        url = "/blogs/" + obj.username
        return url

    def numberOfPosts(self, obj):
        posts = Post.objects.filter(owner__username=obj.username)
        return len(posts)


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('owner',)


class PostListSerializer(PostDetailSerializer):

    class Meta(PostDetailSerializer.Meta):
        fields = ('title', 'image_url', 'summary', 'pub_date')
