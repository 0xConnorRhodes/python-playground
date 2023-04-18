import os

from flask import Flask, render_template
from flask_migrate import Migrate # generates a db migration script if we change the db structure defined in models.py

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
            SECRET_KEY=os.environ.get('SECRET_KEY', default='dev')
    )

    # if you pass in a test_config use that, else use config.py
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from .models import db

    db.init_app(app)
    migrate = Migrate(app, db)

    # requires render_template in imports
    @app.route('/sign_up')
    def sign_up():
        return render_template('sign_up.html') # Flask will look for a template in the templates folder with this name

    return app

