#!/usr/bin/python3

'''Flask web server'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown():
    storage.close()


@app.route('/states_list', strict_slashes=False)
def States_list():
    ess = storage.all(State)
    return render_template('7-states_list.html', ess=ess)
