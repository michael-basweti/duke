# Generated by Django 2.2.3 on 2019-07-10 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HappyClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
