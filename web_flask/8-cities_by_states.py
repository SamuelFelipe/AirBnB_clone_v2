#!/usr/bin/python3

'''Flask web server'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(err):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def States_list():
    ess = storage.all(State)
    return render_template('8-cities_by_states.html', ess=ess)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
