from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'form', views.form_test),
    url(r'signup', views.signup),
    url(r'logout', views.logout)


]
