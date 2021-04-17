# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 22:49:55 2021

@author: Acer7
"""
import expformod as ex
from flask import Flask

app = Flask(__name__)
@app.route("/")
def fdfdf():
    return ex.my_exp(10)
    
if __name__ == "__main__":
    app.run()