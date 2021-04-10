# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:36:21 2021

@author: Acer7
"""


import expformod as unt
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
    
    def buttonClicked(self):
        self.textEdit.append(unt.my_exp(10))
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    app.exec()