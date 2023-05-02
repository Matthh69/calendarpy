import sqlite3
from flask import Blueprint, render_template, request, redirect
from datetime import datetime, timedelta

# Création d'un Blueprint pour les routes
bp = Blueprint('routes', __name__)

# Routing pour la page d'accueil


@bp.route("/")
def hello_world():
    return render_template('index.html')


# Fonction pour récupérer le calendrier et les événements associés

def get_calendar_and_events(date):
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
    conn = sqlite3.connect('instance/database.sqlite')
    cursor = conn.cursor()

    # Récupération de tous les événements associés au calendrier spécifié par l'identifiant 'id'
    cursor.execute(
        'SELECT * FROM event WHERE id_cal = ? ORDER BY event_date ASC', (1,))
    events = cursor.fetchall()

    # Fermeture de la connexion à la base de données
    conn.close()

    return calendar, events, monday


@bp.route('/calendar/<int:id>/')
@bp.route('/calendar/')
def calendar(id=None):
    # Récupération de la date passée en paramètre de l'url de la date actuelle
    date_str = request.args.get('date')
    if date_str is not None:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    else:
        # si l'url n'a pas de parametre de date, on affiche la semaine actuelle
        date = datetime.now()

    # Récupération du calendrier et des événements associés à la date
    calendar, events, monday = get_calendar_and_events(date)

    # Affichage de la page du calendrier avec les événements, le calendrier et la date de la semaine en cours
    return render_template('calendar.html', events=events, calendar=calendar, monday=monday)


@bp.route('/calendar/previous_week/')
def previous_week():
    # Récupération de la date passée en paramètre ou de la date actuelle
    date_str = request.args.get('date')
    if date_str is not None:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    else:
        date = datetime.now()

    # Soustraction de 7 jours pour obtenir la date de la semaine précédente
    new_date = date - timedelta(days=7)

    # Récupération du calendrier et des événements associés à la semaine précédente
    calendar, events, _ = get_calendar_and_events(new_date)

    # Affichage de la page du calendrier avec les événements et le calendrier de la semaine précédente
    return render_template('calendar.html', events=events, calendar=calendar)


@bp.route('/calendar/next_week/')
def next_week():
    # Récupération de la date passée en paramètre ou de la date actuelle
    date_str = request.args.get('date')
    if date_str is not None:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    else:
        date = datetime.now()

    # Ajout de 7 jours à la date pour obtenir la date de la semaine suivante
    new_date = date + timedelta(days=7)

    # Récupération du calendrier et des événements associés à la semaine suivante
    calendar, events, _ = get_calendar_and_events(new_date)

    # Affichage de la page du calendrier avec les événements et le calendrier de la semaine suivante
    return render_template('calendar.html', events=events, calendar=calendar)


'''
@bp.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    date_str = request.form['data-date']
    date = datetime.strptime(date_str, '%Y-%m-%d')
    event_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    event_date = datetime.combine(date, datetime.strptime(
        event_date, '%Y-%m-%d %H:%M:%S').time())
    conn = sqlite3.connect('instance/database.sqlite')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO event (event_date, txt_content, id_cal) VALUES (?, ?, ?)", (event_date, task, 1))
    conn.commit()
    conn.close()
    return render_template('adddata.html', task=task, date=event_date)
'''


@bp.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    date_str = request.form['data-date']
    date = datetime.strptime(date_str, '%Y-%m-%d')
    event_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    event_date = datetime.combine(date, datetime.strptime(
        event_date, '%Y-%m-%d %H:%M:%S').time())
    conn = sqlite3.connect('instance/database.sqlite')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO event (event_date, txt_content, id_cal) VALUES (?, ?, ?)", (event_date, task, 1))
    conn.commit()
    conn.close()

    # Calcul de la date du lundi de la semaine correspondant à la date du champ caché

    # Afficher la page du calendrier de la semaine correspondant à la date du champ caché
    calendar, events, date = get_calendar_and_events(date)
    return render_template('calendar.html', events=events, calendar=calendar, date=date)
