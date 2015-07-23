# -*- coding: utf-8 -*-
from blogs.models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['owner']