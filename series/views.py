from django.shortcuts import render

# Create your views here.
def all_series(request):
    return render(request, 'series/all_series.html')
