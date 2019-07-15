from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=20, blank = False)
    description = models.TextField()

    def __str__(self):
        return self.name
