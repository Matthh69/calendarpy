
import sqlite3
from flask import Blueprint, render_template

bp = Blueprint('routes', __name__)

# Routing index
@bp.route("/")
def hello_world():
    return render_template('index.html')


# Routing calendar
@bp.route('/calendar/<int:id>')
def calendar(id):
    conn = sqlite3.connect('instance/database.sqlite')
    cursor = conn.cursor()

    # Récupération de tous les événements
    cursor.execute('SELECT * FROM event WHERE id_cal = ? ORDER BY event_date ASC', (id,))
    events = cursor.fetchall()
    return render_template('calendar.html', events=events)


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404