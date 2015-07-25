# -*- coding: utf-8 -*-
from blogs.forms import PostForm
from blogs.models import Post
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View

class HomeView(View):
    def get(self, request):
        posts = Post.objects.filter(pub_date__isnull=False).order_by('-pub_date')
        context = {
            'post_list': posts[:5]
        }
        return render(request, 'blogs/home.html', context)

class ListView(View):
    """
    Devuelve:
    - Los posts publicados si el usuario no está autenticado
    -
    """



class BlogsView(View):
    def get(self, request):

        users = User.objects.all()
        context = {
            'user_list': users
        }
        return render(request, 'blogs/blogs.html', context)

class UserPostsView(View):
    def get(self, request, user):
        """
        Cargamos la pagina que lista los posts de un blog (usuario)
        :param request: HttpRequest
        :param user: Usuario al que pertenecen los posts
        :return: HttpResponse
        """

        posts = Post.objects.filter(owner__username=user).order_by('-created_at')
        context = {
            'post_list': posts,
            'author':user
        }
        return render(request, 'blogs/userposts.html', context)

class DetailView(View):
    def get(self, request, user, pk):
        possible_post = Post.objects.filter(owner__username=user, pk=pk).select_related('owner')
        post = possible_post[0] if len(possible_post) >= 1 else None
        if post is not None:
            context = {
                'post': post
            }
            return render(request, 'blogs/detail.html', context)
        else:
            return HttpResponseNotFound()

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
                reverse('post_detail',args=[new_post.owner, new_post.pk])
            )
            success_message += ' Ver post'
            success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'blogs/new_post.html', context)