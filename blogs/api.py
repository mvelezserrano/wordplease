# -*- coding: utf-8 -*-
from blogs.models import Post
from blogs.serializers import BlogSerializer, PostListSerializer, PostDetailSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class BlogListAPI(APIView):

    def get(self, request):
        blogs = User.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostListAPI(ListCreateAPIView):

    '''
    Hay que mostrar los posts del usuario, y así muestra todos
    '''
    queryset = Post.objects.all()

    def get_serializer_class(self):
        return PostDetailSerializer if self.request.method == "POST" else PostListSerializer

    '''
    def get(self, request, user):
        existing_user = get_object_or_404(User, username=user)
        posts = Post.objects.filter(owner__username=existing_user.username).order_by('-pub_date')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    '''

class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer