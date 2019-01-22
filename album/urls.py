from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'album'
urlpatterns = [
    url(r'^$', views.index),
    url(r'addTask', views.addTask),
    url(r'^(?P<task_id>[0-9]+)/$', views.removeTask, name='task_id')

]
