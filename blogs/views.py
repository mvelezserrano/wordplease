from blogs.models import Post
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render


def home(request):
    posts = Post.objects.all().order_by('-pub_date')
    context = {
        'post_list': posts[:5]
    }
    return render(request, 'blogs/home.html', context)

def blogs(request):

    users = User.objects.all()
    context = {
        'user_list': users
    }
    return render(request, 'blogs/blogs.html', context)

def userposts(request, user):
    """
    Cargamos la pagina que lista los posts de un blog (usuario)
    :param request: HttpRequest
    :param user: Usuario al que pertenecen los posts
    :return: HttpResponse
    """

    posts = Post.objects.filter(owner__username=user).order_by('-pub_date')
    context = {
        'post_list': posts,
        'user': user
    }
    return render(request, 'blogs/userposts.html', context)

def detail(request, user, pk):
    possible_post = Post.objects.filter(owner__username=user, pk=pk)
    post = possible_post[0] if len(possible_post) >= 1 else None
    if post is not None:
        context = {
            'post': post
        }
        return render(request, 'blogs/detail.html', context)
    else:
        return HttpResponseNotFound()
