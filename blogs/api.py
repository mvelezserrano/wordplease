# -*- coding: utf-8 -*-
from blogs.models import Post
from blogs.serializers import BlogSerializer, PostListSerializer, PostDetailSerializer
from blogs.views import PostsQuerySet, PostDetailQuerySet
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin


class BlogListAPI(APIView):

    def get(self, request):
        blogs = User.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostViewSet(PostsQuerySet, PostDetailQuerySet, ReadOnlyModelViewSet):
    """
    Este ViewSet hace lo mismo que las clases PostListAPI y PostDetailAPI
    pero en una sola clase
    """
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if self.action == 'list':
            return self.get_posts_queryset(self.request)
        else:
            return self.get_post_detail_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerializer


class CreatePostViewSet(CreateModelMixin, GenericViewSet):

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría del nuevo post
        al usuario autenticado
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)