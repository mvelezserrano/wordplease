# -*- coding: utf-8 -*-
from blogs.forms import PostForm
from blogs.models import Post
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView


class PostsQuerySet(object):
    def get_posts_queryset(self, request):
        queryset = Post.objects.all().filter(owner__username=self.kwargs['user'])
        if not request.user.is_authenticated():
            posts = queryset.filter(pub_date__isnull=False).order_by('-pub_date')
        elif request.user.is_superuser:
            posts = queryset
        else:
            posts = queryset.filter(Q(owner=request.user) | Q(pub_date__isnull=False))
        return posts


class PostDetailQuerySet(object):
    def get_post_detail_queryset(self, request):
        queryset = Post.objects.filter(owner__username=self.kwargs['user'], pk=self.kwargs['pk'])
        if not request.user.is_authenticated():
            posts = queryset.filter(pub_date__isnull=False).order_by('-pub_date')
        elif request.user.is_superuser:
            posts = queryset
        else:
            posts = queryset.filter(Q(owner=request.user) | Q(pub_date__isnull=False))
        return posts



class HomeView(View):
    def get(self, request):
        posts = Post.objects.filter(pub_date__isnull=False).order_by('-pub_date')
        context = {
            'post_list': posts[:5]
        }
        return render(request, 'blogs/home.html', context)


class BlogsView(View):
    def get(self, request):

        users = User.objects.all()
        context = {
            'user_list': users
        }
        return render(request, 'blogs/blogs.html', context)


class UserPostsView(ListView, PostsQuerySet):
    model = Post
    template_name = 'blogs/user_posts.html'

    def get_queryset(self):
        return self.get_posts_queryset(self.request)


class DetailView(View, PostDetailQuerySet):
    """
        Carga la página de detalle en un post
        :param request: HttpRequest
        :param user: blog del usuario al que pertenece le post
        :param pk: id de la post
        :return: HttpResponse
        """
    def get(self, request, user, pk):
        possible_post = self.get_post_detail_queryset(self.request).select_related('owner')
        post = possible_post[0] if len(possible_post) >= 1 else None
        if post is not None:
            context = {
                'post': post
            }
            return render(request, 'blogs/detail.html', context)
        else:
            return HttpResponseNotFound('No existe el post')

class CreateView(View):
    @method_decorator(login_required())
    def get(self, request):
        """
        Muestra un formulario para crear un post
        :param request:
        :return:
        """
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'blogs/new_post.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Crea un post en base a la información POST
        :param request:
        :return:
        """
        success_message = ''
        post_with_owner = Post()
        post_with_owner.owner = request.user
        form = PostForm(request.POST, instance=post_with_owner)
        if form.is_valid():
            # Guardamos el objeto post y lo devolvemos
            new_post = form.save()
            form = PostForm()
            success_message = 'Post generado con éxito!'
            success_message += '<a href="{0}">'.format(
                reverse('post_detail', args=[new_post.owner, new_post.pk])
            )
            success_message += ' Ver post'
            success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'blogs/new_post.html', context)