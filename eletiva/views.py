from django.shortcuts import render
from django.views.generic import DetailView

from .models import EletivaConfiguracao


# Create your views here.

class EletivaList(DetailView):
    model = EletivaConfiguracao
    context_object_name = 'configuracao'
