# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from users.forms import LoginForm, SignUpForm
from django.views.generic import View

class LoginView(View):
    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
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
                    url = request.GET.get('next', 'blogs_home') #si no existe el parámetro GET
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('blogs_home')

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        context = {
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)

    def post(self, request):
        success_message = ''
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignUpForm()
            success_message = 'Usuario creado con éxito!'
        context = {
            'signup_form': form,
            'success_message': success_message
        }
        return render(request, 'users/signup.html', context)
