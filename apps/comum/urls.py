from django.urls import path
from . import views

app_name= 'comum'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
]
