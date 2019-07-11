from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

class HireCorporate(models.Model):
    SERVICE = (
        ('corporate', 'corporate'),
        ('social','social')
    )
    applicant_name = models.CharField(max_length=100, blank=False, null=False)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=100, blank=False, null=False)
    service = models.CharField(choices=SERVICE, max_length=20)
    application_description = models.TextField(max_length=500, default='Your application', null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.applicant_name

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Social and Corporate Events")