# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='max_attendance',
            field=models.IntegerField(default=10),
        ),
    ]