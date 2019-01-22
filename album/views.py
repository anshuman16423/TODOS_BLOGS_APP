from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from . import models
from .forms import NewTask


def index(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('../')
    curr_user = request.session['username']
    task = []
    for i in models.Task.objects.all():
        if i.username == curr_user:
            task.append(i)
    context = dict()
    context['user'] = curr_user
    context['task'] = task
    temp = loader.get_template('album\index.html')
    return HttpResponse(temp.render(context, request))


def addTask(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('../')
    curr_user = request.session['username']
    if request.method == 'POST':
        form = NewTask(request.POST)
        if form.is_valid():
            a = models.Task()
            a.username = curr_user
            a.task_title = form.cleaned_data['title']
            a.task_detail = form.cleaned_data['detail']
            a.save()
            return HttpResponseRedirect("../album")
    form = NewTask()
    temp = loader.get_template('album/addTask.html')
    return HttpResponse(temp.render({'form': form}, request))


def removeTask(request, task_id):
    try:

        models.Task.objects.get(id=task_id).delete()
        return HttpResponseRedirect('../album')
    except:
        return HttpResponseRedirect('../album')
