from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aluno, Experimento_Pratico, Experimento_Teorico



def dash(request): 
    x = y = []
    
    value_teorico = Experimento_Teorico.objects.all()
    for c in value_teorico:
        tempo = 0.53 * c.concentracao_t
        y.append(tempo)
        x.append(c.concentracao_t)
        dict = {'z': x, 'w': y}
        print(dict)

    value_pratico = Experimento_Pratico.objects.all()
    for c in value_pratico:
        pass

    return render(request, 'dash.html', {'y' : dict['w'], 'x' : dict['z']})

















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