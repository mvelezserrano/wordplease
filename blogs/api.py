# -*- coding: utf-8 -*-
from blogs.models import Post
from blogs.serializers import BlogSerializer, PostSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


class BlogListAPI(APIView):

    def get(self, request):
        blogs = User.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


class PostListAPI(APIView):

    def get(self, request, user):
        posts = Post.objects.filter(owner__username=user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)