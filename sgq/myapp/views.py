from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aluno, Experimento_Pratico, Experimento_Teorico



def dash(request): 
    x = y = []
    value_teorico = Experimento_Teorico.objects.all()
    for c in value_teorico:
        tempo = 0.53 * c.concentracao_t
        y.append(round(tempo, 3))
        x.append(c.concentracao_t)


    return render(request, 'dash.html', {'tempo' : y, 'concen' : x})

















def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def new_exp_pratico():
    pass

def del_exp_pratico():
    pass

def new_exp_teorico():
    pass

def del_exp_teorico():
    pass