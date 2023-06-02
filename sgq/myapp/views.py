from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aluno, Experimento_Pratico, Experimento_Teorico
import json


def dash(request): 
    lista_dados = []
    
    value_teorico = Experimento_Teorico.objects.all()
    for c in value_teorico:
        tempo = 0.53 * c.concentracao_t
        lista_dados.append({"x": c.concentracao_t, "y":tempo})

    value_pratico = Experimento_Pratico.objects.all()
    for c in value_pratico:
        pass



    dados_json = json.dumps(lista_dados)
    return render(request, 'dash.html', {"dados_json":dados_json})

















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