# Generated by Django 2.2.3 on 2019-07-07 08:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EventAlbum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventAlbum.Album')),
            ],
        ),
    ]
