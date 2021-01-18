import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '123'
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = os.path.join(BASE_DIR, 'db.sqlite3')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_OPTIONS = {}