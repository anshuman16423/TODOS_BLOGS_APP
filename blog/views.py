# -*- coding: utf-8 -*-
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from forms import BlogEntry
from models import blog
from datetime import datetime


# Create your views here.
def index(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('../login')

    temp = loader.get_template('blog/index.html')
    blogs_all = list(blog.objects.all())
    blogs_all.sort(key=lambda x: x.datetime, reverse=True)
    context = dict()
    context['username'] = request.session['username']
    context['objects'] = blogs_all

    return HttpResponse(temp.render(context, request))


def create_blog(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('../login')
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
            return HttpResponseRedirect('../blog')
    form = BlogEntry()
    context = dict()
    context['form'] = form
    temp = loader.get_template('blog/register.html')

    return HttpResponse(temp.render(context, request))


def manage(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('../login')

    user_blog = blog.objects.filter(user=request.session['username'])
    context = dict()
    context['list'] = user_blog
    context['user'] = request.session['username']
    temp = loader.get_template('blog/manage.html')
    return HttpResponse(temp.render(context, request))


def edit(request, blog_edit):

    blog_data = blog.objects.get(id = blog_edit)
    d=dict()
    d['blogTitle'] = blog_data.title
    d['blogTags'] = blog_data.tags
    d['blogContent'] = blog_data.content
    blog.objects.filter(id=blog_edit).delete()
    form = BlogEntry(d)
    temp = loader.get_template('blog/edit.html')
    return HttpResponse(temp.render({'form':form}, request))


def delete(request, blog_delete):
    blog.objects.filter(id=blog_delete).delete()

    return HttpResponseRedirect('/blog')
