#!/usr/bin/python3
"""
Starts a Flask web application
Routes:
/states
/states/<id>
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Returns a Html page contains a list of all states
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """
    Returns a Html page contains the state that matches the id provided
    """
    states = storage.all(State).values()
    state = (state for state in states if state.id == id)
    if state is not None:
        return render_template('9-states.html', state=state)
    return """
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>Not found!</H1>

    </BODY>
</HTML>"""


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
