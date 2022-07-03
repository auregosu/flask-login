from flask import Flask, render_template, redirect, url_for
#from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Create and configure app object
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # Initialize plugins
    db.init_app(app)
    #Bootstrap(app)
    login_manager.init_app(app)

    with app.app_context():
        from .view import auth, routes

        # Register blueprints
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(routes.routes_bp)

        # Create database models
        db.create_all()


        return app