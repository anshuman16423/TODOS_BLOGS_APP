from django.http import HttpResponse
from django.template import loader


def index(request):
    context = dict()
    context['flag'] = 0
    context['username'] = ''
    if 'username' in request.session:
        context['flag'] = 1
        context['username'] = request.session['username']
    temp = loader.get_template('first/index.html')
    return HttpResponse(temp.render(context, request))
