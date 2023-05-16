import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

X = np.array([[0], [5], [10], [15], [20]])  #concentração
y = np.array([0, 10, 25, 30, 40])               #variação de temperatura
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))
print(reg.coef_)
print(reg.intercept_)
#reg.predict(np.array([[3, 5]]))
plt.scatter(X, y)


meu_y = reg.coef_ * X + reg.intercept_
print('meu erro1', mean_squared_error(y, meu_y))
y_raul = 2*X
print('meu erro2', mean_squared_error(y, y_raul))


a = np.linspace(0, 20, 100)
b = reg.coef_  * a + reg.intercept_
plt.plot(a, b, 'r-')
plt.show()