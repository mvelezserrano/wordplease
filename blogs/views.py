from blogs.models import Post
from django.shortcuts import render


def home(request):

    posts = Post.objects.all()
    return render(request, 'blogs/home.html')
