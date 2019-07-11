from django.db import models
from datetime import datetime

class HappyClient(models.Model):
    company = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.company
