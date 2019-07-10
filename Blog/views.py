from django.shortcuts import render
from .models import Blog

def blog(request):
    blogs = Blog.objects.order_by('-date_added')
    context = {
        "blogs":blogs
    }
    return render(request, 'pages/blog.hml', context)
