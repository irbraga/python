#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient(host='localhost',port=27017)
db = client['tictactoe']

