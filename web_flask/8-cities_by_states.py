#!/usr/bin/python3
"""
List of states
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/cities_by_states/", strict_slashes=False)
def cities_by_states():
    from models.state import State
    states = storage.all(State).values()
    print(state.city.__dict__ for state in states)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
