#!/usr/bin/env python
# coding: utf-8




import multiprocessing
import random
import sys
import math 

n = 1000

def findpi(u):
    incircle = 0
    for i in range (n):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        distance = math.sqrt(x**2+y**2)
        if distance < 1:
            incircle += 1
        return incircle
    
def test_all(pool):
    l = pool.map(findpi, [1] * n)
    return l

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    print(test_all(pool))
    k = sum(test_all(pool))
    pi = 4 * k / n
    print(pi)
else:
    print(__name__)