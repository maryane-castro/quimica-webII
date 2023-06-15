import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
	x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
	
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
	intercept = SS_xy / SS_xx
	coef = m_y - intercept*m_x

	return (coef, intercept)


def mean_squared_error(y_true, y_pred):
    e = 0
    for yi, yj in zip(y_true, y_pred):
        e += (yi - yj)**2
    return e