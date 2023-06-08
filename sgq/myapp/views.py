from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aluno, Experimento_Pratico
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as lg


from sklearn.linear_model import LinearRegression
import numpy as np

#auth
def regressao(dados):
    x_valores = np.array([dado['x'] for dado in dados]).reshape(-1, 1)
    y_valores = np.array([dado['y'] for dado in dados])

    regressao = LinearRegression()
    regressao.fit(x_valores, y_valores)
    y_previsto = regressao.predict(x_valores)
    pass #em construção










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
        lista_teorico = []
        
        #teorico
        value_teorico = Experimento_Pratico.objects.all()
        for c in value_teorico:
            tempo_1 = c.temp_ebulicao_p
            lista_dados.append({"x": c.concentracao_p, "y":tempo_1})

            tempo_2 = c.concentracao_p * 0.52
            lista_teorico.append({"x": c.concentracao_p, "y":tempo_2})

        #regressao...





        dados_json = json.dumps(lista_dados)
        teorico = json.dumps(lista_teorico)
        return render(request, 'dash.html', {"dados_json":dados_json, "dados_teorico":teorico})
    
    return HttpResponse('Vc precisa estar logado')



def addteorico():
    pass
def delteorico():
    pass

def addpratico():
    pass
def delpratico():
    pass
