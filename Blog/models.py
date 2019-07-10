from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from datetime import datetime

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, blank=False, default="title")
    blog = RichTextUploadingField(default="Your Blog")
    blog_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default="main photo")
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

