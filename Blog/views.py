from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request):
    blogs = Blog.objects.order_by('-date_added')
    context = {
        "blogs":blogs
    }
    return render(request, 'pages/blog.html', context)

def blog_detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        "blog":blog
    }
    return render(request, 'pages/blog_detail.html', context)
