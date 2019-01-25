# -*- coding: utf-8 -*-
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    temp = loader.get_template('blog/index.html')
    return HttpResponse(temp.render({}, request))


def create_blog(request):
    return HttpResponse()
