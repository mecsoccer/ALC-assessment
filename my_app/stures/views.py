# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Student, Resource
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


def index(request):
    return render(request, 'stures/index.html')


def about(request):
    return render(request, 'stures/about.html')


class StudentView(generic.ListView):
    template_name = 'stures/student.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Student.objects.all()


class ResourceView(generic.ListView):
    template_name = 'stures/resource.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Resource.objects.all()


class DetailView(generic.DetailView):
    model = Resource
    template_name = 'stures/detail.html'
    context_object_name = 'res'

    def get_queryset(self):
        return Resource.objects.all()


class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'sex', 'passport', 'age', 'cgpa']


class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'sex', 'passport', 'age', 'cgpa']


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('stures:student')


class ResourceCreate(CreateView):
    model = Resource
    fields = ['type', 'author', 'topic', 'content', 'date']
