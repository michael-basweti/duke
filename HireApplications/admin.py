from django.contrib import admin
from .models import Hire

class HireAdmin(admin.ModelAdmin):
    list_display = ('id', 'applicant_name', 'email', 'phone', 'service')
    list_display_links = ('id', 'applicant_name')
    search_fields = ('applicant_name',)
    list_per_page = 20

admin.site.register(Hire, HireAdmin)
