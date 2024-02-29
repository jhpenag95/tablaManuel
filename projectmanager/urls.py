from django.contrib import admin
from django.urls import path
from gestor.views import *
from gestor.pruebas import * 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login, name='login'),
    path('project/',inicio,name='inicio'),
    path('inicioCard/',inicioCard,name='inicioCard'),
    path('project/new',nuevoproyecto,name='nuevoproyecto'),
    path('project/create',crearprojecto,name='crearprojecto'),
    path('project/asignar/new',asignar,name='asignar'),
    path('project/12',diagrama,name='diagrama'),
]
