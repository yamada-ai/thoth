from bottle import get, post, request, run, error

@get('/test')
def input_area():
    return'''
        <form action='/result' method="post">
            Input string A = <input name="a" type="text" />
            <br><br/>
            Input string B = <input name="b" type="text" />
            <input value="joint" type="submit" />
        <form>
    '''

@post('/result')
def input_area():
    a=request.forms.get('a')
    b=request.forms.get('b')
    return '<font size=5><center> Result </center></font><br><br/>'\
           '<font size=5><center><p>{0}{1}</p></font></center>'.format(a,b)

@error(404)
def error404(error):
    return 'Oops, you may have the wrong URL...<br><br/>\
           try again>>  <a href= "http://localhost:8080/test">\
           localhost:8080/test</a>'.format(error=error)

run(host='localhost',port=8080,debug=True)   #debug=Trueでデバッグ出力機能有効