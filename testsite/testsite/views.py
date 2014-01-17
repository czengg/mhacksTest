from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    #even better, don't have toe get the template and make a context
    return render(request, 'current_datetime.html', {'current_date' : now})


def hello(request):
    return HttpResponse("Hello world! See I'm not *that* bad at git")
