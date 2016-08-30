#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import bottle
from bottle import route, run, template, error

__author__ = 'fax'

app = application = bottle.Bottle()

bottle.debug(True)

@app.route('/')
def hello():
    return 'You Shall Not Pass!'

@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

@app.error(500)
def error500(error):
    return json.dumps({"result": "ko", "message": error.body})

@app.hook('before_request')
def strip_path():
    bottle.request.environ['PATH_INFO'] = bottle.request.environ[
        'PATH_INFO'].rstrip('/')

@app.route('/info')
def index():
    return 'teleBot v 0.0.0.0.0.1a'

@app.route('/math/<op>/<op1:int>/<op2:int>')
def index(op, op1, op2):

    def default():
        print ("Incorrect input!")
    dict = {'somma': '+',
            'più': '+',
            'addizione': '+',
            'add': '+',
            'sum': '+',
            '+': '+',
            'meno': '-',
            'minus': '-',
            'sottrazione': '-',
            'sub': '-',
            '-': '-',
            'per': '*',
            'moltiplicazione': '*',
            '*': '*',
            'moltiplication': '*',
            'diviso': '/',
            'divisione': '/',
            '/': '/',
            'div': '/',
            'iva': 'iva'}
    try:
        operazione=dict[op]
        print(operazione)
    except Exception as e:
        print (e)

    if operazione == '+':
        result = op1 + op2
    elif operazione == '-':
        result = op1 - op2
    elif operazione == '*':
        result = op1 * op2
    elif operazione == '/':
        result = op1 / op2
    elif operazione == 'iva':
        valore_iva = op1 * int(0, op2)
        result = op1 - valore_iva
    return template('<b>Se la matematica non è un\' opinione {{op1}} {{operazione}} {{op2}} fa {{result}} </b>', operazione=operazione, op1=op1, op2=op2, result=result)

if __name__ == "__main__":
        bottle.run(app=app, host='localhost', port=8080)
