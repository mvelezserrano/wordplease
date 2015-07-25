from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class Post(models.Model):
    owner = models.ForeignKey(User)
    title = models.TextField()
    summary = models.TextField()
    content = models.TextField()
    # Indicamos que el campo image_url es opcional
    image_url = models.URLField(blank=True, null=True, default="")
    pub_date = models.DateTimeField(blank=True, null=True, default="")
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title