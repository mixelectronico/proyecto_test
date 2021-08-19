from django.db import models
import re

# Create your models here.
class ClienteManager(models.Manager):
    def validador_cliente(self, data):
        errores = {} #Diccionario de errores
        if len(data['nombre']) == 0:
            errores['nombre'] = 'Ingrese un nombre'
        if len(data['apellido']) == 0:
            errores['apellido'] = 'ingrese un apellido'
        if len(data['rut']) == 0:
            errores['rut'] = 'ingrese un rut'
        if len(data['dv']) == 0:
            errores['dv'] = 'ingrese un dv'
        #Esto es una expresion regular para validar los datos ingresados
        EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL.match(data['email']):
                errores['email'] = "email invalido"
        return errores

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido  = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    email  = models.CharField(max_length=50)
    direccion  = models.CharField(max_length=50)
    password  = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClienteManager()