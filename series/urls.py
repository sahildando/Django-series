
from django.urls import path, include
from . import views 


#localhost:8000/series
#localhost:8000/series/order

urlpatterns = [
    path('', views.all_series, name='all_series'),
    ]