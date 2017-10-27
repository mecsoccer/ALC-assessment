# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Student(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    passport = models.FileField(default=0)
    age = models.IntegerField(default=0)
    cgpa = models.FloatField()

    def get_absolute_url(self):
        return reverse('stures:student')

    def __str__(self):
        return self.name + ':' + str(self.cgpa)


class Resource(models.Model):
    type = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    image = models.FileField(default=0)

    def __str__(self):
        return self.type + self.author

