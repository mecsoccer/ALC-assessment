# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stures', '0003_auto_20171030_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='content',
            field=models.CharField(default=0, max_length=2000),
        ),
    ]
