from django.contrib import admin

# Importando a classe Person de models
from .models import Colaborador

# Register your models here.
admin.site.register(Colaborador)
