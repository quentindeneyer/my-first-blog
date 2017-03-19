# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.workshop_list, name='workshop_list'),
    url(r'^taller/(?P<pk>\d+)/$', views.workshop_detail, name='workshop_detail'),
    url(r'^taller/new$', views.workshop_new, name='workshop_new'),
    url(r'^taller/(?P<pk>\d+)/edit/$', views.workshop_edit, name='workshop_edit'),
    url(r'^organizador/$', views.organizer_list, name='organizer_list'),
]