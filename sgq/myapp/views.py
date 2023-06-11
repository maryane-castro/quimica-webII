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
    # x_valores = np.array([dado['x'] for dado in dados]).reshape(-1, 1)
    # y_valores = np.array([dado['y'] for dado in dados])

    # regressao = LinearRegression()
    # regressao.fit(x_valores, y_valores)
    # y_previsto = regressao.predict(x_valores)
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

def k_raul(request):
    value = Experimento_Pratico.objects.all()

    for c in value:
        k = c.concentracao_p * 0.52
    
    return k 

def k_otimo():
    value = Experimento_Pratico.objects.all()
    concentracao = []
    temp = []

    for c in value:
        concentracao.append([c.concentracao_p])
        temp.append(c.temp_ebulicao_p)

    concentracao = np.array(concentracao)
    temp = np.array(temp)
    regressao = LinearRegression().fit(concentracao, temp)
    
    return regressao.coef_

def teorico():
    value = Experimento_Pratico.objects.all()
    lista_dados = []

    for c in value:
        lista_dados.append({"x": c.concentracao_p, "y" : c.temp_ebulicao_p})

    return lista_dados






def dash(request): 
    if request.user.is_authenticated:

        k_Raul = k_raul()
        k_Otimo = k_otimo()
        dados = teorico()


        k_Raul_json = json.dumps(k_Raul)
        k_Otimo_json = json.dumps(k_Otimo)
        Dados_json = json.dumps(dados)

        return render(request, 'dash.html', {"dados_json":Dados_json, "k_otimo": k_Otimo_json, "k_raul" : k_Raul_json})
    
    return HttpResponse('Vc precisa estar logado')



def addteorico():
    pass
def delteorico():
    pass

def addpratico():
    pass
def delpratico():
    pass


# lista_teorico = []

#     value = Experimento_Pratico.objects.all()
#     for c in value:
#         tempo_2 = c.concentracao_p * 0.52
#         lista_teorico.append({"x": c.concentracao_p, "y":tempo_2})

#     teorico = json.dumps(lista_teorico)