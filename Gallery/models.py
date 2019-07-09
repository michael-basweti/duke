from django.db import models
from EventAlbum.models import Album

from datetime import datetime

class Gallery(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.description
