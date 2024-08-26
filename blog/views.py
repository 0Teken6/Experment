from django.shortcuts import render
from .models import Blog

def index(request):
    context = {'blogs': Blog.objects.all()}

    return render(request, 'blog/index.html', context=context)