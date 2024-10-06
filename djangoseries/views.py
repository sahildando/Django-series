from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You are at django series Home page")

def about(request):
    return HttpResponse("Hello, world. You are at django series About page")

def contact(request):
    return HttpResponse("Hello, world. You are at django series contact page")