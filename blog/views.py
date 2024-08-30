from django.shortcuts import render
from .models import Blog

def main(request):
    context = {'blogs': Blog.objects.all()}

    return render(request, 'blog/main.html', context=context)