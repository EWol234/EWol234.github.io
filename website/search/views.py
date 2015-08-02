from django.shortcuts import render
from .forms import SearchForm
from projects.models import Post

# Create your views here.
def list(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        posts = Post.objects.filter(title__icontains=form.query)
        return render(request, 'search/results.html', {'posts': post, 'form': form})

    else:
        form = SearchForm()
        return render(request, 'search/results.html', {'form': form})
