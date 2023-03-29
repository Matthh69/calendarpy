import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def getdb():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def closedb(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = getdb()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init_db')
def initdb_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(closedb)
    app.cli.add_command(initdb_command)