from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("Hello, world. You are at django series Home page")
 return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. You are at django series About page")

def contact(request):
    return HttpResponse("Hello, world. You are at django series contact page")

