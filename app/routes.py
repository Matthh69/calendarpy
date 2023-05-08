import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from . import db

# Création d'un Blueprint pour les routes
bp = Blueprint('routes', __name__)

# Routing pour la page d'accueil


@bp.route("/")
def hello_world():
    return render_template('index.html')

# Fonction pour récupérer le calendrier et les événements associés


def get_calendar_and_events(date, id=None):
    # On calcule le jour de la semaine de la date passée en paramètre et on soustrait le nombre de jours nécessaires pour obtenir le lundi
    delta = date.weekday() - 0  # 0 correspond au jour de la semaine pour le lundi
    monday = date - timedelta(days=delta)

    # Liste des jours de la semaine
    days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']

    # Liste des dates des cinq prochains jours à partir du lundi
    dates = []
    for i in range(5):
        date = monday + timedelta(days=i)
        dates.append(date.date())

    # Génération du calendrier
    calendar = [{'day': day, 'date': date} for day, date in zip(days, dates)]

    # Connexion à la base de données
    conn = db.get_db()
    cursor = conn.cursor()

    # Récupération de tous les événements associés au calendrier spécifié par l'identifiant 'id'
    if id is None:
        cursor.execute(
            'SELECT * FROM event WHERE id_cal = ? ORDER BY event_date ASC', (1,))
        events = cursor.fetchall()
    else:
        cursor.execute(
            'SELECT * FROM event WHERE id_cal = ? ORDER BY event_date ASC', (id,))  # Ajouter une condition si l'id n'existe pas dans database
        events = cursor.fetchall()

    events = [dict(event) for event in events]
    for event in events:
        event['color'] = '#' + hex(abs(hash(str(event['id']))))[2:8]

    # Fermeture de la connexion à la base de données
    db.close_db(conn)

    return calendar, events, monday

# http://127.0.0.1:5000/calendar/2/2023-05-16/

@bp.route('/calendar/<int:id>/<date>/')
def calendar(date=None, id=None):
    if date is None:
        date_obj = datetime.now()
    else:
        date_obj = datetime.strptime(date, '%Y-%m-%d')

    if id is None:
        # Récupération du calendrier et des événements associés à la date
        calendar, events, monday = get_calendar_and_events(date_obj)
    else:
        calendar, events, monday = get_calendar_and_events(date_obj, id)
        print('ID N EST PAS NULL')
    # Affichage de la page du calendrier avec les événements, le calendrier et la date de la semaine en cours
    return render_template('calendar.html', events=events, calendar=calendar, monday=monday, date=monday.strftime('%Y-%m-%d'), id=id)


@bp.route('/calendar/<int:id>/<date>/previous_week/')
def previous_week(id, date):
    # Récupération de la date passée en paramètre ou de la date actuelle
    date_obj = datetime.strptime(date, '%Y-%m-%d')

    # Soustraction de 7 jours pour obtenir la date de la semaine précédente
    new_date = date_obj - timedelta(days=7)

    # Construction de l'URL pour la semaine précédente en incluant l'identifiant 'id'
    url = url_for('routes.calendar', id=id, date=new_date.strftime('%Y-%m-%d'))

    # Redirection vers la page du calendrier pour la semaine précédente
    return redirect(url)


@bp.route('/calendar/<int:id>/<date>/next_week/')
def next_week(id, date):
    # Récupération de la date passée en paramètre ou de la date actuelle
    date_obj = datetime.strptime(date, '%Y-%m-%d')

    # Ajout de 7 jours à la date pour obtenir la date de la semaine suivante
    new_date = date_obj + timedelta(days=7)

    # Construction de l'URL pour la semaine suivante en incluant l'identifiant 'id'
    url = url_for('routes.calendar', id=id, date=new_date.strftime('%Y-%m-%d'))

    # Redirection vers la page du calendrier pour la semaine suivante
    return redirect(url)


@bp.route('/add_task/', methods=['POST'])
def add_task():
    task = request.form['task']
    date_str = request.form['data-date']
    idCal = request.form['idCal']
    date = datetime.strptime(date_str, '%Y-%m-%d')
    event_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    event_date = datetime.combine(date, datetime.strptime(
        event_date, '%Y-%m-%d %H:%M:%S').time())
    conn = sqlite3.connect('instance/database.sqlite')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO event (event_date, txt_content, id_cal) VALUES (?, ?, ?)", (event_date, task, idCal))
    conn.commit()
    conn.close()
    # Afficher la page du calendrier de la semaine correspondant à la date du champ caché
    url = url_for('routes.calendar', id=idCal, date=date_str)

    # Redirection vers la page du calendrier pour la semaine correspondant à la date du formulaire
    return redirect(url)


@bp.route('/update_event', methods=['POST'])
def update_event():
    # Récupération de la connexion à la base de données
    conn = db.get_db()

    # Récupération de l'identifiant de l'événement à mettre à jour et du nouveau contenu
    event_id = request.form.get('event_id')
    new_content = request.form.get('content')
    date_str = request.form['data-date']
    idCal = request.form['idCal']
    date = datetime.strptime(date_str, '%Y-%m-%d')

    # Exécution d'une requête SQL pour mettre à jour le contenu de l'événement
    conn.execute(
        'UPDATE event SET txt_content = ? WHERE id = ?', (
            new_content, event_id)
    )

    # Validation de la transaction
    conn.commit()

    # Redirection vers la page du calendrier pour la semaine correspondant à la date de l'événement
    url = url_for('routes.calendar', id=idCal, date=date.strftime('%Y-%m-%d'))
    return redirect(url)
