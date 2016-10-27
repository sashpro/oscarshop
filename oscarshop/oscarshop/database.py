import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DBCONNECT = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'oscar_db',
        'USER': 'psql_sash',
        'PASSWORD': 'blue1965',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    },
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

