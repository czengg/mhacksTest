from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world! See I'm not *that* bad at git")
