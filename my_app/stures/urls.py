from django.conf.urls import url
from . import views

app_name = 'stures'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/$', views.StudentView.as_view(), name='student'),
    url(r'^resource/$', views.ResourceView.as_view(), name='resource'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add_stud/$', views.StudentCreate.as_view(), name='add_stud'),
    url(r'^detail/(?P<pk>[0-9]+)/update/$', views.StudentUpdate.as_view(), name='update'),
    url(r'^detail/(?P<pk>[0-9]+)/delete/$', views.StudentDelete.as_view(), name='delete')
]
