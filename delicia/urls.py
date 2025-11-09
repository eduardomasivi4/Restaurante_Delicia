from django.urls import path
from . import views

urlpatterns = [
    #           home
        path('', views.index, name='index'),
    
    #           menu
        path('/menu', views.menu, name='menu'),
    
    #           bebidas
        path('/bebidas', views.bebidas, name='bebidas'),
    
    #           sobre
        path('/sobre', views.sobre, name='sobre'),
    
    #           contato
        path('/contato', views.contato, name='contato'),
    
    #           reservar
        path('/reservar', views.reservar, name='reservar')
]
