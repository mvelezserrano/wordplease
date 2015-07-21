from blogs.models import Post
from django.contrib.auth.models import User
from django.shortcuts import render


def home(request):

    users = User.objects.all()#.order_by('-created_at')
    context = {
        'user_list': users
    }
    return render(request, 'blogs/home.html', context)

def blog(request, user):
    """
    Cargamos la pagina que lista los posts de un blog (usuario)
    :param request: HttpRequest
    :param user: Usuario al que pertenecen los posts
    :return: HttpResponse
    """

    posts = Post.objects.filter(owner__username=user)
    context = {
        'post_list': posts
    }
    return render(request, 'blogs/blog.html', context)
