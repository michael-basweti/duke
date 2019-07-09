from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

class Hire(models.Model):
    SERVICE = (
        ('tents', 'tents'),
        ('catering', 'catering'),
        ('electronics', 'electronics')
    )
    applicant_name = models.CharField(max_length=100, blank=False, null=False)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=100, blank=False, null=False)
    service = models.CharField(choices=SERVICE, max_length=20)
    application_description = models.TextField(max_length=500, default='Your application', null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.applicant_name

