# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:11:48 2021

@author: Acer7
"""
import math
import string

def my_exp(x):
    x_pow = x
    multiplier = 1
    partial_sum = x 
    for n in range(2, 25):
        x_pow = x**(n)  
        multiplier = 1 / math.factorial(n)  
        partial_sum += x_pow * multiplier
    return str(partial_sum)