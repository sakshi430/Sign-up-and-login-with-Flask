from flask import Flask, app, request, make_response, redirect, render_template

app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    user= request.form.get('name')
    print(user)
    return render_template('index.html',user=user)


@app.route('/user/<name>')
@app.route('/<name>')
def sayHello(name):
    return 'Hello, %s.'%name


@app.route('/header')
def reqHead():
    user_agent=request.headers.get('User-Agent')
    return 'Your Browser is %s'%user_agent


@app.route('/response')
def response():
    response=make_response('This doc carries cookies.')
    response.set_cookie('answer','42')
    return response


@app.route('/google')
def google():
    return redirect('')

if __name__=='__main__':
    app.run(debug=True)