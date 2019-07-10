from django.urls import path

from . import views

urlpatterns = [
    path('', views.hire_corporate, name='hire'),
]