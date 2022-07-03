# Flask configuration
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

TESTING = True
Debug = True

FLASK_APP = 'app.py'
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')

# Static Assets
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///data/users.db'
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
