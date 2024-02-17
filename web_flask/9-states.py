#!/usr/bin/python3
"""
States and state
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("states/<id>", strict_slashes=False)
def state_id(id):
    states = storage.all(State).values()
    state = (state for state in states if state.id == id)
    if state:
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
