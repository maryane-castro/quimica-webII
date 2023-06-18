# dic = {"x":[10], "y":10 }
# dic["x"].append(1)

# data = []

# data.append(dic.copy())
# dic.clear()
# print(data, dic)
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
lista_dados = [
  {"x": 1, "y": 5},
  {"x": 2, "y": 8},
  {"x": 3, "y": 3},
  {"x": 4, "y": 6},
  {"x": 5, "y": 9}
]


# print(lista_dados)
# lista_dados.append({"x": 2, "y" : 3})
# print(lista_dados)

x_valores = [dado['x'] for dado in lista_dados]
y_valores = [dado['y'] for dado in lista_dados]



plt.scatter(x_valores, y_valores)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão')

plt.show()