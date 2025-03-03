#!/usr/bin/python3

'''
Flask Web server.
'''


from flask import Flask
from flask import render_template


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def Int_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
