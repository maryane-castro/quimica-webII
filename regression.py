import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([[0], [5], [10], [15], [20]])  #concentração
y = np.array([0, 10, 20, 30, 40])               #variação de temperatura
reg = LinearRegression().fit(X, y)
#reg.score(X, y)
print(reg.coef_)
print(reg.intercept_)
#reg.predict(np.array([[3, 5]]))

plt.scatter(X, y)

a = np.linspace(0, 20, 100)
b = reg.coef_  * a + reg.intercept_
plt.plot(a, b, 'r-')
plt.show()