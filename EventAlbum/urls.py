from django.urls import path

from . import views

urlpatterns = [
    path('', views.albums, name='albums'),
    path('<int:album_id>', views.album, name='album'),
    # path('team', views.team, name='team'),
]