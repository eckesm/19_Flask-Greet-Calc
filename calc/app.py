# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

OPERATIONS = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}

OPERATIONS_map = {
    'add': 'add',
    'subtract': 'sub',
    'multiply': 'mult',
    'divide': 'div'
}


def calculator_path(operation, a, b):
    import socket
    # host=socket.getservbyname()
    return f"http://127.0.0.1:5000/{operation}?a={a}&b={b}"
    # return f"{host}/{operation}?a={a}&b={b}"
    # return f"{host}/{operation}?a={a}&b={b}"

#


def go_to_page(path):
    import webbrowser
    webbrowser.open(path)


@app.route('/', methods=['GET'])
def root_get():
    return f"""
    <h1>Calculate this for me real quick, hunnnnn...</h1>
    <form method="POST">
      <input list='operations' placeholder='select operation' name='operation'/>
      <input type='text' placeholder='number 1' name='a'/>
      <input type='text' placeholder='number 2' name='b'/>
      <button>Calculate plz!</button>
    </form>

    <datalist id="operations">
      <option value="add">
      <option value="subtract">
      <option value="multiply">
      <option value="divide">
    </datalist>
    """


@app.route('/', methods=['POST'])
def root_post():
    operation = request.form['operation']
    a = request.form['a']
    b = request.form['b']

    go_to_page(calculator_path(OPERATIONS_map[operation], a, b))
    # return calculator_path(OPERATIONS_map[operation], a, b)


@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = OPERATIONS[operation](a, b)
    return str(result)


@app.route('/add')
def operation_add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations.add(a, b)
    return str(result)


@app.route('/sub')
def sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations.sub(a, b)
    return str(result)


@app.route('/mult')
def mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations.mult(a, b)
    return str(result)


@app.route('/div')
def div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations.div(a, b)
    return str(result)
