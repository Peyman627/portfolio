from django.shortcuts import render

from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/all_blogs.html', context)
