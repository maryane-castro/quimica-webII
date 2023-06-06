import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

lista_dados = [
    {"x": 1, "y": 3},
    {"x": 0, "y": 4},
    {"x": 7, "y": 5},
    {"x": 4, "y": 7},
    {"x": 3, "y": 4}
]

x_valores = np.array([dado['x'] for dado in lista_dados]).reshape(-1, 1)
y_valores = np.array([dado['y'] for dado in lista_dados])

regressao = LinearRegression()
regressao.fit(x_valores, y_valores)
y_previsto = regressao.predict(x_valores)

#dados
plt.scatter(x_valores, y_valores)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão')
#plt.show()

#regressão linear
#plt.scatter(x_valores, y_valores)  #dados
plt.plot(x_valores, y_previsto, color='red')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Regressão Linear')
plt.show()
x_previstos1 = []
y_previsto1 = []



for i in range(len(lista_dados)):
    x_previstos1.append(lista_dados[i]['x'])
    y_previsto1.append(round(y_previsto[i], 2))

print(x_previstos1[0])


lista_regressao = []
for c in range(len(x_previstos1)):
    print(c)
    lista_regressao.append({"x": x_previstos1[c], "y" : y_previsto1[c]})
#para retornar ao dashboard
print(lista_regressao[0]['x'])


x_valores = np.array([dado['x'] for dado in lista_regressao]).reshape(-1, 1)
y_valores = np.array([dado['y'] for dado in lista_regressao])


#printar tudo igualzinho
#print(x_previstos1)
#print(y_previsto1)
