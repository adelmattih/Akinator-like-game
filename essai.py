# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:15:23 2019

@author: paul
"""
"""
Ce programme permet d'afficher une page web en local, avec écrit 
projet de développement logiciel Akinator.

"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Projet de développement logiciel Akinator"

if __name__ == "__main__":
    app.run()