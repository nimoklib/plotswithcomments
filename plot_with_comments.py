
#!/usr/bin/env python3 
# -*- coding: utf-8 -*- # здесь мы задаем кодировку нашей программе 

import math # подключаем модуль с математическими функциями
import numpy # подключаем модуль
import matplotlib.pyplot as mpp # подключаем модуль, который рисует график, и выбираем формат файла

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1] # определяем интервал и шаг  
    mpp.plot(               # задаем формулу нашего графика, используя синус из модуля математических функций
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )
    mpp.show()  #показываем файл с нашим графиком
    
    