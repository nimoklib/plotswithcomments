# -*- coding: utf-8 -*-
"""
Created on Sat May  1 00:36:07 2021

@author: Acer7
"""
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'ntry': [i for i in range(49)],
    'numeric': [1.99, 1.57, 1.48, 1.64, 1.35, 1.53, 1.33, 1.3, 1.55, 1.58, 1.41, 1.48, 1.36, 1.47, 1.36, 1.34, 1.36, 1.32, 1.35, 1.33, 1.29, 1.4, 1.26, 1.32, 1.3, 1.33, 1.3, 1.24, 1.21, 1.13, 1.16, 1.2, 1.11, 1.04, 1.23, 1.12, 1.31, 1.14, 1.07, 1.13, 1.16,1.14, 1.17, 1.1, 1.13, 1.04, 1.09, 1.08, 1.15]
})

df.to_csv('myseconddata.csv')
dftest = pd.read_csv('myseconddata.csv', sep=',')
print(dftest)

dfgraph = pd.DataFrame(data={
    'df': df['numeric'],
})

dfgraph.plot.kde()

d1 = dfgraph['df']

print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=len(d1)))