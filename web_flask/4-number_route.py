#!/usr/bin/python3

'''
Flask Web server.
'''


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def Text(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<string:text>', strict_slashes=False)
def Python(text):
    if text:
        return 'Python ' + text.replace('_', ' ')
    return 'Python is cool'


@app.route('/number/<int:n>', strict_slashes=False)
def Ints(n):
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
