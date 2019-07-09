from django.shortcuts import render
from Testimonials.models import Testimonial
from EventAlbum.models import Album
from team.models import Team

def index(request):
    testimonials = Testimonial.objects.order_by('-date')
    albums = Album.objects.order_by('-date_added')[:6]
    context = {
        'testimonials': testimonials,
        'albums': albums,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # # get all realtors
    # realtors = Realtor.objects.order_by('-hire_date')
    # # get mvp
    # mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    # context = {
    #     'realtors': realtors,
    #     'mvp_realtors': mvp_realtors
    # }
    return render(request, 'pages/about.html')

def team(request):
    team = Team.objects.order_by('-start_date')
    context = {
        "team_members":team
    }
    return render(request, 'pages/team.html', context)
