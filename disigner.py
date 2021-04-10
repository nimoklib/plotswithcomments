# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:06:26 2021

@author: Acer7
"""
import string
import math
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import krasota


class Example(QMainWindow, krasota.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)
    def my_exp(self, x):
        x_pow = x
        multiplier = 1
        partial_sum = x 
        for n in range(2, 25):
            x_pow = x**(n)  
            multiplier = 1 / math.factorial(n)  
            partial_sum += x_pow * multiplier
        return str(partial_sum)
    def buttonClicked(self):
        self.textEdit.append(self.my_exp(10))
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    app.exec()