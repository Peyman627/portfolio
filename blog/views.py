from django.shortcuts import render

from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    context = {'blogs': blogs}
    return render(request, 'blog/all_blogs.html', context)


def detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/detail.html', context)