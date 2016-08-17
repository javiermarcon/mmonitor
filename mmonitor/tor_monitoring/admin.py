from django.contrib import admin

# Register your models here.
from .models import Empresa, Maquina

admin.site.register(Empresa)
admin.site.register(Maquina)