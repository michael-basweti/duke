from django.db import models

from datetime import datetime

class Album(models.Model):
    album_name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False)
    album_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.album_name
