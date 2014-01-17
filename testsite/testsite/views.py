from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def hello(request):
    return HttpResponse("Hello world! See I'm not *that* bad at git")
