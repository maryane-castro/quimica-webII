from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect




def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def dash(request):
    return render(request, 'dash.html')







def new_exp_pratico():
    pass

def del_exp_pratico():
    pass

def new_exp_teorico():
    pass

def del_exp_teorico():
    pass