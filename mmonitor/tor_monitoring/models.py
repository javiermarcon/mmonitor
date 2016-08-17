from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create your models here.

STATUSES = (
        (u'R', u'Rojo'),
        (u'A', u'Amarillo'),
        (u'V', u'Verde'),
        (u'D', u'Desconocido'),
    )

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    last_status = models.CharField(max_length=1, default='N', choices=STATUSES)
    last_check = models.DateTimeField('ultimo chequeo', default=None) #datetime.now)
    
    def __str__(self):
        return self.nombre

class Maquina(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    puerto = models.IntegerField(default=522)
    password = models.CharField(max_length=200)
    last_pc_status = models.CharField(max_length=1, default='N', choices=STATUSES)
    last_vps_status = models.CharField(max_length=1, default='N', choices=STATUSES)
    last_check = models.DateTimeField('ultimo chequeo', default=None) #datetime.now)
    
    def __str__(self):
        return "%s (%s)" % (self.nombre, self.host) 