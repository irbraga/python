#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
import numpy as np

app = Flask(__name__)

# Obtain application info
@app.route("/info", methods=['GET'])
def info():
    return jsonify({
        'name': 'Tic Tac Toe',
        'version': '0.0.1a'
    })

@app.route("/matrix", methods=['GET'])
def getMetrix():
    matrix = np.array([[np.str(' ') for rows in range(3)] for columns in range(3)])
    return jsonify(matrix.tolist())

@app.route("/play", methods=['POST'])
def play():
    return None