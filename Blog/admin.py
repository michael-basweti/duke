from django.contrib import admin
from .models import Blog
class Post(admin.ModelAdmin):
    exclude = ('author',)
    list_display = ('title', 'author', 'date_added')
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
admin.site.register(Blog, Post)
