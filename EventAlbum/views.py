from django.shortcuts import render, get_object_or_404
from .models import Album
from Gallery.models import Gallery

def albums(request):
    albums = Album.objects.order_by('-date_added')

    context = {
        "albums":albums
    }

    return render(request, 'past_events/albums.html', context)

def album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    photos = Gallery.objects.order_by('-date_added').filter(album_id=album_id)
    context = {
        "album":album,
        "photos":photos
    }
    return render(request, 'past_events/album.html', context)
    