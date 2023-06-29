import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
import locale

from . import db
import uuid
import hashlib

# http://127.0.0.1:5000/calendar/2023-05-29/4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5
# changer couleur sur demande
# mdp de confirmation quand on arrive sur calendrier

# Création d'un Blueprint pour les routes
bp = Blueprint('routes', __name__)
# modification


def getId():
    conn = sqlite3.connect('instance/database.sqlite')
    # créer un curseur pour exécuter des requêtes
    cur = conn.cursor()
    # récupérer le plus grand id_cal de la database
    cur.execute("SELECT MAX(id_cal) FROM event")
    resultat = cur.fetchone()
    print('Resultat id selectionné: ', resultat[0])
    conn.close()
    return resultat


def calculate_hash(id):
    hash_obj = hashlib.sha256(str(id).encode('utf-8'))
    hash_value = hash_obj.hexdigest()
    return hash_value


def calculate_idCal(hash):
    idTest = 0
    idCalSession = session.get('idCal')
    resultat = getId()
    # +1 normalement mais des fois les id ne sont pas bien detectés dans getId
    for idTest in range(int(resultat[0])+5):
        print(idTest)
        hash_value = calculate_hash(idTest)
        print("id: ", idTest, " hash de l'id: ", hash_value)
        if hash == hash_value:
            print("hash == hash_value:")

            session['idCal'] = idTest
            session['hash'] = hash_value
            break
        idTest += 1
    else:  # la boucle for a été terminée sans trouver d'id_cal correspondant
        print('false')
        return False
    print('false')
    return True


@bp.route("/")
def createCalender():
    return render_template('createCalendar.html')


@bp.route('/create_calendar', methods=['POST'])
def create_calendar():
    conn = sqlite3.connect('instance/database.sqlite')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO calendar DEFAULT VALUES")
    new_id = cursor.lastrowid
    conn.commit()

    # Générer le hash à partir de l'id généré
    hash_value = calculate_hash(new_id)

    conn.close()
    session['idCal'] = new_id
    session['hash'] = hash_value
    date_obj = datetime.now()

    # Redirection vers la page du nouveau calendrier créé, en incluant le hash dans l'URL
    url = url_for('routes.calendar', date=date_obj.strftime(
        '%Y-%m-%d'), hash=hash_value)
    return redirect(url)


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
    print(calendar[0]['date'].strftime('%B'))

    # Connexion à la base de données
    conn = db.get_db()
    cursor = conn.cursor()

    # Récupération de tous les événements associés au calendrier spécifié par l'identifiant 'id'
    cursor.execute(
        'SELECT * FROM event WHERE id_cal = ? ORDER BY event_date ASC', (id,))  # Ajouter une condition si l'id n'existe pas dans database
    events = cursor.fetchall()

    events = [dict(event) for event in events]
    for event in events:
        event['color'] = '#' + hex(abs(hash(str(event['id']))))[2:8]

    # Fermeture de la connexion à la base de données
    db.close_db(conn)

    return calendar, events, monday


@bp.route('/calendar/<string:hash>')
@bp.route('/calendar/<date>/<string:hash>')
def calendar(date=None, hash=None):

    # si la date n'est pas spécifiée en paramètre alors on affiche la semaine actuelle
    if date is None:
        date_obj = datetime.now()
    else:
        date_obj = datetime.strptime(date, '%Y-%m-%d')

    FindId = calculate_idCal(hash)
    if FindId == True:  # Si True alors id vient d'être défini dans la session
        idCalSession = session.get('idCal')
        print("id trouvé")
    elif FindId == False:  # Si false ca veut dire que le hash calculé avec tous les id_cal n'as jamais donné le hash affiché donc on affiche pas le calendrier
        return render_template('error.html')

    # Définir la localisation en français
    locale.setlocale(locale.LC_TIME, 'fr_FR')

    # Récupérer la localisation en cours
    current_locale = locale.getlocale()

    idCalSession = session.get('idCal')

    print('ID SESSION IS', idCalSession)
    print('HASH VERIFICATION IS GOOD', hash)

    # Conversion des mois en lettres en utilisant strftime avec locale
    months = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin',
              'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    current_month = months[date_obj.month - 1]

    calendar, events, monday = get_calendar_and_events(date_obj, idCalSession)

    current_year = date_obj.year

    if (hash):
        session['hash'] = hash

    month_number = date_obj.month
    background_class = ''
    if month_number in [12, 1, 2]:
        background_class = 'hiver'
    elif month_number in [3, 4, 5]:
        background_class = 'printemps'
    elif month_number in [6, 7, 8]:
        background_class = 'ete'
    elif month_number in [9, 10, 11]:
        background_class = 'automne'

    return render_template('calendar.html', events=events, calendar=calendar, monday=monday, date=monday.strftime('%Y-%m-%d'), id=idCalSession, current_locale=current_locale, current_year=current_year, current_month=current_month, months=months, hash=hash, background_class=background_class)


@bp.route('/previous_week/<date>')
def previous_week(date):
    # calcul de la date de la semaine précédente
    date_obj = datetime.strptime(date, '%Y-%m-%d') - timedelta(weeks=1)
    hash = session.get('hash')

    # redirection vers la page du calendrier correspondant à la date précédente
    return redirect(url_for('routes.calendar', date=date_obj.strftime('%Y-%m-%d'), hash=hash))


@bp.route('/next_week/<date>')
def next_week(date):
    # calcul de la date de la semaine suivante
    date_obj = datetime.strptime(date, '%Y-%m-%d') + timedelta(weeks=1)
    hash = session.get('hash')

    # redirection vers la page du calendrier correspondant à la date suivante
    return redirect(url_for('routes.calendar', date=date_obj.strftime('%Y-%m-%d'), hash=hash))


@bp.route('/add_task/', methods=['POST'])
def add_task():
    hash = session.get('hash')
    task = request.form['task']
    date_str = request.form['data-date']
    idCal = request.form['idCal']

    # Création d'une variable datetime avec la date sélectionnée par l'utilisateur et l'heure actuelle
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
    url = url_for('routes.calendar', date=date_str, hash=hash)
    return redirect(url)


@bp.route('/update_event', methods=['POST'])
def update_event():
    # Récupération de la connexion à la base de données
    conn = db.get_db()
    hash = session.get('hash')

    # Récupération de l'identifiant de l'événement à mettre à jour et du nouveau contenu
    event_id = request.form.get('event_id')
    new_content = request.form.get('content')
    date_str = request.form['data-date']
    date = datetime.strptime(date_str, '%Y-%m-%d')

    # Si le champ "content" est vide, on supprime l'événement
    if not new_content:
        conn.execute('DELETE FROM event WHERE id = ?', (event_id,))
    else:
        # Exécution d'une requête SQL pour mettre à jour le contenu de l'événement
        conn.execute('UPDATE event SET txt_content = ? WHERE id = ?',
                     (new_content, event_id))
    conn.commit()

    # Redirection vers la page du calendrier pour la semaine correspondant à la date de l'événement
    url = url_for('routes.calendar', date=date.strftime('%Y-%m-%d'), hash=hash)
    return redirect(url)


@bp.route('/apropos')
def apropos():
    return render_template('apropos.html')


@bp.route('/aide')
def aide():
    return render_template('aide.html')
