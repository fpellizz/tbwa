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
    return 'Hello World'


@app.error(404)
def error404(error):
    return 'Nothing here, sorry'


@app.error(500)
def error500(error):
    return json.dumps({"result": "ko", "message": error.body})


@app.route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@app.hook('before_request')
def strip_path():
    bottle.request.environ['PATH_INFO'] = bottle.request.environ[
        'PATH_INFO'].rstrip('/')


@app.route('/info')
def index():
    return 'teleBot v 0.0.0.0.0.1a'


@app.route('/math/<op>/<op1:int>/<op2:int>')
def index(op, op1, op2):
    valid = False
    if op == 'add':
        operazione = '+'
        valid = True
    elif op == 'sum':
        operazione = '+'
        valid = True
    elif op == 'più':
        operazione = '+'
        valid = True
    elif op == '+':
        operazione = '+'
        valid = True
    elif op == 'sub':
        operazione = '-'
        valid = True
    elif op == 'meno':
        operazione = '-'
        valid = True
    elif op == '-':
        operazione = '-'
        valid = True
    elif op == 'per':
        operazione = '*'
        valid = True
    elif op == 'mult':
        operazione = '*'
        valid = True
    elif op == '*':
        operazione = '*'
        valid = True
    elif op == 'div':
        operazione = '/'
        valid = True
    elif op == 'fratto':
        operazione = '/'
        valid = True
    elif op == '/':
        operazione = '/'
        valid = True
    elif op == 'iva':
        operazione = 'iva'
        valid = True
    elif op == 'vat':
        operazione = 'iva'
        valid = True
    elif op == 'tax':
        operazione = 'iva'
        valid = True
    else:
        operazione = 'storazzo'
        return template('<b>Hai inserito "{{op}}" Operazione non valida</b>!', op=operazione)

    if (valid):
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
