from django.contrib import admin

# Register your models here.
from .models import Escola, Periodo

admin.site.register(Escola)
admin.site.register(Periodo)
