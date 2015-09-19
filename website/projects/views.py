from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Picture
from .models import Link
from django.utils import timezone

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'projects/index.html', {'posts': posts})

def proj_display(request, pk):
    post = get_object_or_404(Post, pk=pk)
    pictures = Picture.objects.filter(matching_post_id=pk).order_by('order')
    links = Link.objects.filter(matching_post_id=pk)
    return render(request, 'projects/proj_display.html', {'post': post, 'pictures': pictures, 'links': links})

def proj_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'projects/projects.html', {'posts': posts})

def extras(request):
    return render(request, 'projects/extras.html', {})
