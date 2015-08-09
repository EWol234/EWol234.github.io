from django.contrib import admin
from .models import Post
from .models import Picture
from .models import Link

# Register your models here.
admin.site.register(Post)
admin.site.register(Picture)
admin.site.register(Link)
