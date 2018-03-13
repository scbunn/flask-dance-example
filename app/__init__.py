from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_login import (
    LoginManager, current_user)
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
google_auth_bp = make_google_blueprint(scope=['email', 'profile'])


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    app.register_blueprint(google_auth_bp, url_prefix='/auth')

    from app.main import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setup SQLAlchemy flask-dance backend
    google_auth_bp.backend = SQLAlchemyBackend(
        models.OAuth, db.session, user=current_user)

    return app


from app import models
