from django.db import models

# Create your models here.
from django.db import models

class argentinos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()


class extranjero(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40) 
    dni = models.IntegerField() 

class nacionalizado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()


