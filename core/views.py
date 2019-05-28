from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Escola


class IndexView(generic.ListView):
    template_name = 'index.html'

def index(request):
    escolas = Escola.objects.all()
    context = {'escolas': escolas}
    return render(request, 'index.html', context)

def escola(request, escola_id):
    e = get_object_or_404(Escola, pk=escola_id)
    context = {'escola': e}
    return render(request, 'escola.html', context)
