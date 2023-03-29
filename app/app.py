import sqlite3
import os
from flask import g
from flask import Flask, render_template

app = Flask(__name__)
#app.config.from_object(__name__)

#app.config.from_pyfile('./config/settings.cfg')

# fonction pour accéder à la base de données


def get_events():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM event")
    events = cursor.fetchall()
    conn.close()
    return events


# Routing index
@app.route("/")
def hello_world():
    return render_template('index.html')

# Routing calendar


@app.route('/calendar')
def hello():
    if not os.path.isfile('database.db'):
        return render_template('noDatabase.html')
    else:
        # si la base de données existe déjà, récupérer les données de la table events
        events = get_events()
        return render_template('calendar.html', events=events)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404