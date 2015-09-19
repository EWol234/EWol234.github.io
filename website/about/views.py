from django.shortcuts import render
from .models import Category

# Create your views here.
def about(request):
    categories = Category.objects.all().order_by('order')
    return render(request, "about/about.html", {'categories': categories,})
