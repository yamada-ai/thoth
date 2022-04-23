from bottle import route, run, template
from bottle import get, post, request, run, error
import os

@route("/login")
def login():
    return template("login")

# @route("/login", method="POST")
@post("/login")
def do_login():
    username = request.forms.get("username")
    password = request.forms.get("password")
    if check_login(username, password):
        return template("success", username=username)
    else:
        return template("failure", username=username)

def check_login(username, password):
    if username == "user" and password == "pass":
        return True
    else:
        return False

@error(404)
def error404(error):
    return '<font size=6><left> You got lost?? <br><br/>\
    Here is the login URL ->> </left></font>\
    <a href = "http://localhost:8080/login">Click!!</a>'.format(error=error)

run(host='localhost',port=8080,debug=True)   