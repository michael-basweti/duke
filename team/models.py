from django.db import models
from datetime import datetime

class Team(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False)
    role = models.CharField(max_length=100, blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    start_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
