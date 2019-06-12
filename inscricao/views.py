from django.shortcuts import render, redirect, get_object_or_404

from .models import Inscricao, Alternativa, Participante, InscricaError
from django.views.generic import ListView, DetailView

# Create your views here.

class ParticipanteDetail(DetailView):
    model = Participante

class InscricaoList(ListView):
    model = Inscricao

class InscricaoDetail(DetailView):
    model = Inscricao

class AlternativaDetail(DetailView):
    model = Alternativa

def realiza_inscricao(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')
        p = get_object_or_404(Participante, matricula=matricula, senha=senha)
        alternativa = get_object_or_404(Alternativa, pk=request.POST.get('alternativa'))
        try:
            alternativa.inscreve(p)
            return redirect('participante', pk=p.id)
        except InscricaError as error:
            flash('Looks like you have changed your name!')
            # sesison não tem mais vaga
            return redirect('alternativas')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
