import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Routing index
    @app.route("/")
    def hello_world():
        return render_template('index.html')

    # Routing calendar
    @app.route('/calendar')
    def hello():
        return render_template('calendar.html')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

    """
        DATABASE
    """

    from . import db
    db.init_app(app)

    return app