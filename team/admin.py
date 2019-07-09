from django.contrib import admin
from .models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'role')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'role')
    list_per_page = 20


admin.site.register(Team, TeamAdmin)
