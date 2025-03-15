from .base import *


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '4abb424121f68f'
EMAIL_HOST_PASSWORD = '2c6d0f57d28f41'
EMAIL_PORT = '2525'
DEFAULT_FROM_EMAIL = "info@real_estate.com"
DOMAIN = "localhost:8000"
SITE_NAME = "REAL ESTATE"


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
