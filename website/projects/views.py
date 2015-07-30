from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'projects/projects.html', {'posts': posts})

def proj_display(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'projects/proj_display.html', {'post': post})
