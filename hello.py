from bottle import route, run, template
from bottle import get, post, request, run, error

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>', name=name)

run(host='localhost', port=8080)