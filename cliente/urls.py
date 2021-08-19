from django.urls import path, include
from . import views


#Todas las rutas de la app login estan incluidas acá.
#'' me redirige
urlpatterns = [
    path('', views.inicio),
    path('inicio', views.inicio),
    path('agregar', views.agregar), #create
    path('leer', views.leer),
    path('actualizar', views.actualizar),
    path('eliminar', views.eliminar),
]