from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'addBlog', views.create_blog),
    url(r'manage', views.manage),
    url(r'/edit/(?P<blog_edit>[0-9]+)/$', views.edit, name='blog_edit'),
    url(r'/delete/(?P<blog_delete>[0-9]+)/$', views.delete, name='blog_delete')

]
