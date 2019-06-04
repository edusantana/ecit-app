from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Escola


class IndexView(generic.ListView):
    model = Escola
    template_name = 'index.html'

class DetailView(generic.DetailView):
    model = Escola
