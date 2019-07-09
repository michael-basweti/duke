from django.db import models
from datetime import datetime

class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=False)
    testimonial = models.TextField(blank=False)
    company = models.CharField(max_length=200, blank=False, default="Company name")
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
