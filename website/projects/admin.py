from django.contrib import admin
from .models import Post
from .models import Picture

# Register your models here.
admin.site.register(Post)
admin.site.register(Picture)
