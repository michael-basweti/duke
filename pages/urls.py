from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]