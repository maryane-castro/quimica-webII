from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Aluno, Experimento_Pratico, Experimento_Teorico



def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def dash(request): 
    x = Aluno.objects.all()   
    return render(request, 'dash.html', {'aluno' : x})







def new_exp_pratico():
    pass

def del_exp_pratico():
    pass

def new_exp_teorico():
    pass

def del_exp_teorico():
    pass