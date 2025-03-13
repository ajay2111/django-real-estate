from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'estate',  # Name of your PostgreSQL database
        'USER': 'postgres',  # Username to use when connecting to your database
        'PASSWORD': 'lockhorns',  # Password to use when connecting to your database
        'HOST': 'localhost',  # Hostname or IP address of the database server
        'PORT': '5432',  # Port to use (default is 5432)
    }
}
