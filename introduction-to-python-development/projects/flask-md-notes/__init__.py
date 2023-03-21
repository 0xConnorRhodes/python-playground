import os

from flask import Flask # import the Flask class

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

    return app

