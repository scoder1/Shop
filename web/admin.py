from django.contrib import admin
from .models import homePost, Post, Contact

# Register your models here.
admin.site.register(homePost)
admin.site.register(Post)
admin.site.register(Contact)