
from flask import Flask, current_app, g
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from . import db
    db.init_app(app)
    return app