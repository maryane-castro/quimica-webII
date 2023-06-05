#Parte teorica
#pratica é o do calculo mesmo

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



plt.scatter(x_valores, y_valores)
plt.plot(x_valores, y_previsto, color='red')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão com Regressão Linear')
plt.show()
