from django.shortcuts import render
from Testimonials.models import Testimonial
from EventAlbum.models import Album
from team.models import Team
from Blog.models import Blog
from clients.models import HappyClient

def index(request):
    testimonials = Testimonial.objects.order_by('-date')
    albums = Album.objects.order_by('-date_added')[:6]
    blogs = Blog.objects.order_by('-date_added')[:3]
    clients = HappyClient.objects.order_by('-date_added')
    context = {
        'testimonials': testimonials,
        'albums': albums,
        "blogs":blogs,
        "clients":clients
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def team(request):
    team = Team.objects.order_by('-start_date')
    context = {
        "team_members":team
    }
    return render(request, 'pages/team.html', context)

def services(request):
    return render(request,'services/hire_corporate_social.html')

def contact(request):
    return render(request, 'pages/contact.html')
