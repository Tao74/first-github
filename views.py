from django.http import HttpResponse

def index(request):
    return HttpResponse('test is ok')


def login(request):
    return HttpResponse('tset is ok')

