# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stures', '0004_resource_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='date',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
