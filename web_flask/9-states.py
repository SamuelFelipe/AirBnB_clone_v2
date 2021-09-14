#!/usr/bin/python3

'''Flask web server'''

from flask import Flask, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(err):
    storage.close()


@app.route('/states', strict_slashes=False)
def States_list():
    ess = storage.all(State)
    return render_template('9-states.html', ess=ess)


@app.route('/states/<string:id>', strict_slashes=False)
def State_id(id):
    ess = storage.all(State)
    for state in ess.values():
        if state.id == id:
            return render_template('9-states.html', obj=state)
    return abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
