# -*- coding: utf-8 -*-
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from forms import BlogEntry
from models import blog
from datetime import datetime

# Create your views here.
def index(request):
    temp = loader.get_template('blog/index.html')
    return HttpResponse(temp.render({}, request))


def create_blog(request):
    if request.method == 'POST':
        form = BlogEntry(request.POST)
        if form.is_valid():
            ent = blog()
            ent.user = request.session['username']
            ent.datetime = datetime.now()
            ent.title = form.cleaned_data['blogTitle']
            ent.tags = form.cleaned_data['blogTags']
            ent.content = form.cleaned_data['blogContent']
            ent.save()
            #print 'form saved'
            return HttpResponseRedirect('../blog')
    form = BlogEntry()
    context = dict()
    context['form'] = form
    temp = loader.get_template('blog/register.html')

    return HttpResponse(temp.render(context, request))
