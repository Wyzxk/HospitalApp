from django.contrib import admin
from .models import Doctores,Sedes,Pacientes
# Register your models here.
admin.site.register(Doctores)
admin.site.register(Sedes)
admin.site.register(Pacientes)