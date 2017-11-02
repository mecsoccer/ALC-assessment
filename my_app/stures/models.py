# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Student(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    passport = models.FileField(default=0)
    age = models.IntegerField(default=0)
    cgpa = models.FloatField(default=5.0)

    def get_absolute_url(self):
        return reverse('stures:student')

    def __str__(self):
        return self.name + ':' + str(self.cgpa)


class Resource(models.Model):
    type = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    topic = models.CharField(max_length=100)
    content = models.CharField(max_length=3000)
    date = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('stures:resource')

    def __str__(self):
        return self.type + self.author

