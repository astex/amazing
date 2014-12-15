from flask import Flask
from flask.ext.cors import CORS


def create_app(config):
    app = Flask(__name__)
    app.config.from_pyfile(config)

    CORS(app, headers='Content-Type')

    from amazing.lib.database import db
    db.init_app(app)

    from amazing import views
    views.register(app)

    with app.app_context():
        db.create_all()

    return app
