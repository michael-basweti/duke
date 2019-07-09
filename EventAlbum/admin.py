from django.contrib import admin
from .models import Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'album_name', 'date_added')
    list_display_links = ('id', 'album_name')
    search_fields = ('album_name',)
    list_per_page = 20


admin.site.register(Album, AlbumAdmin)