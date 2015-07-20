from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    fields = [
        'owner',
        'title',
        'summary',
        'content',
        'image_url',
        'pub_date',
        'categories'
    ]

    filter_horizontal = ('categories',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)