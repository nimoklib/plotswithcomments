import math

ITERATIONS = 21

def my_exp(x):
    """
    Вычисление гиперболического синуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = x
    multiplier = 1
    partial_sum = x 
    for n in range(2, ITERATIONS):
        x_pow *= x**(n)  # В цикле постепенно считаем степень
        multiplier *= 1 / math.factorial(n)  # считаем факториал
        partial_sum += x_pow * multiplier
    
    return partial_sum

print(help(math.exp), math.exp(10))
print(help(my_exp), my_exp(10))


