from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    owner = models.ForeignKey(User)
    title = models.TextField
    summary = models.TextField
    content = models.TextField
    # Indicamos que el campo image_url es opcional
    image_url = models.URLField(blank=True, default="")
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title


class Category(models.Model):
    posts = models.ManyToManyField(Post)
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name