# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from users.forms import LoginForm


def login(request):
    error_messages = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect('blogs_home')
                else:
                    error_messages.append('El usuario no está activo')
    else:
        form = LoginForm()
    context = {
        'errors': error_messages,
        'login_form': form
    }
    return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('blogs_home')
