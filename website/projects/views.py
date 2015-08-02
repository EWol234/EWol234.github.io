from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Picture
from search.forms import SearchForm
from django.utils import timezone

# Create your views here.

def index(request):
    form = SearchForm()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'projects/index.html', {'posts': posts, 'form': form})

def proj_display(request, pk):
    form = SearchForm()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'projects/proj_display.html', {'post': post, 'form': form})

def proj_list(request):
    form = SearchForm()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'projects/projects.html', {'posts': posts, 'form': form})

def about(request):
    form = SearchForm()
    return render(request, 'projects/about.html', {'form': form})

def extras(request):
    form = SearchForm()
    return render(request, 'projects/extras.html', {'form': form})
