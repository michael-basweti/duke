# Generated by Django 2.2.3 on 2019-07-10 08:00

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_remove_blog_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Your Blog'),
        ),
    ]