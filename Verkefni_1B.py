from sys import argv
from bottle import *
@route('/')
def links():
    return '<a href=/sida2>Síða2</a> <a href=/sida3>Síða3</a> <a href=/sida4>Síða4</a>'
@route('/sida2')
def backlink():
    return '<a href=/>Síða1</a>'
@route('/sida3')
def backlink2():
    return '<a href=/>Síða1</a>'
@route('/sida4')
def backlink3():
    return '<a href=/>Síða1</a>'
run(host='0.0.0.0',port=argv[1],debug=True)
