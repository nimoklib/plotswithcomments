# -*- coding: utf-8 -*-
"""
Created on Sat May  1 00:36:07 2021

@author: Acer7
""" 

from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd


dftest = pd.read_csv('myseconddata.csv', sep=',')
print(dftest)

dfgraph = pd.DataFrame(data={
    'df': dftest['numeric'],
})

dfgraph.plot.kde()
plt.show()

d1 = dfgraph['df']

print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=len(d1)))
