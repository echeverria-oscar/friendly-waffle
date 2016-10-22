from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^travels$', views.travels),
    url(r'^addplan$', views.addplan),
    url(r'^process_plan$', views.process_plan),
    url(r'^locations/(?P<id>\d+)$', views.locations),
    url(r'^join/(?P<id>\d+)$', views.join),

]
