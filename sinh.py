import math

ITERATIONS = 21

def my_sinh(x):
    """
    Вычисление гиперболического синуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = x
    multiplier = 1
    partial_sum = x 
    for n in range(1, ITERATIONS):
        x_pow *= x**(2*n+1)  # В цикле постепенно считаем степень
        multiplier *= 1 / math.factorial(2*n+1)  # считаем факториал
        partial_sum += x_pow * multiplier
    
    return partial_sum

print(help(math.sinh), math.sinh(0.8))
print(help(my_sinh), my_sinh(0.8))

import cmath

complex_angle = cmath.asinh(2)
print('"Угол", на котором гиперболический синус достигает двух:', complex_angle)

print("Достигает ли двух наш гиперболический синус?", my_sinh(complex_angle))
print("А библиотечный?", cmath.sinh(complex_angle))

%matplotlib inline
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')


import matplotlib.pyplot as plt
import numpy as np

vs = np.vectorize(my_sinh)
print(my_sinh, vs)

angles = np.r_[-14.00:14.00:0.01]
plt.plot(angles, np.sinh(angles))
plt.plot(angles, vs(angles))
plt.show()
