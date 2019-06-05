from django.shortcuts import render

from .models import Inscricao
from django.views.generic import ListView


# Create your views here.

class InscricaoList(ListView):
    model = Inscricao
