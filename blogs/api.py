# -*- coding: utf-8 -*-
from blogs.models import Post
from blogs.serializers import BlogSerializer, PostListSerializer, PostDetailSerializer
from blogs.views import PostsQuerySet
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BlogListAPI(APIView):

    def get(self, request):
        blogs = User.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostListAPI(PostsQuerySet, ListCreateAPIView):

    '''
    Hay que mostrar los posts del usuario, y así muestra todos
    '''
    #queryset = Post.objects.all()

    #lookup_url_kwarg = "user"
    permission_classes = (IsAuthenticatedOrReadOnly),

    def get_serializer_class(self):
        return PostDetailSerializer if self.request.method == "POST" else PostListSerializer
    '''
    def get_queryset(self):
        user = self.kwargs.get(self.lookup_url_kwarg)
        existing_user = get_object_or_404(User, username=user)
        posts = Post.objects.filter(owner__username=existing_user.username).order_by('-pub_date')
        return posts
    '''

    def get_queryset(self):
        queryset = self.get_posts_queryset(self.request)
        return queryset.filter(owner__username=self.kwargs['user']).order_by('-pub_date')


    '''
    def get(self, request, user):
        existing_user = get_object_or_404(User, username=user)
        posts = Post.objects.filter(owner__username=existing_user.username).order_by('-pub_date')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    '''

class PostDetailAPI(PostsQuerySet, RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly),

    def get_queryset(self):
        queryset = self.get_posts_queryset(self.request)
        return queryset.filter(owner__username=self.kwargs['user'], pk=self.kwargs['pk']).order_by('-pub_date')