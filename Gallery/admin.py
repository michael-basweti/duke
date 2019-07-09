from django.contrib import admin
from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'photo')
    list_display_links = ('id', 'photo')
    search_fields = ('photo',)
    list_per_page = 20

admin.site.register(Gallery, GalleryAdmin)
