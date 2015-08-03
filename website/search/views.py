from django.shortcuts import render
from projects.models import Post

# Create your views here.
def list(request):
    message = ''
    if request.GET['q'] is not '':
        q = request.GET['q']
        posts = Post.objects.filter(title__icontains=request.GET['q'])
        if not posts:
            message = 'No results found.'
            return render(request, 'search/results.html', {'posts': posts, 'q': q, 'message': message})
        else:
            return render(request, 'search/results.html', {'posts': posts, 'q': q})
    else:
        message = 'No results found.'
        return render(request, 'search/results.html', {'message': message})
