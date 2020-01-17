import os

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}
