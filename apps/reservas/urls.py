from django.urls import path
from . import views

app_name= 'reservas'

urlpatterns = [
    path('criar', views.criar, name='criar'),
]
