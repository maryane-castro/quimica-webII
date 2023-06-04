from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aluno, Experimento_Pratico, Experimento_Teorico
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as lg

#auth



def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuario com esse nome')
        
        user = User.objects.create_user(username=username, password=senha)
        user.save()
        return HttpResponse('Show!!')



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            lg(request, user)
            return redirect('dash')
        else: 
            return HttpResponse('erro')


#plataform


def dash(request): 
    if request.user.is_authenticated:
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
    
    return HttpResponse('Vc precisa estar logado')