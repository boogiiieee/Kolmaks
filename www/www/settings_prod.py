# -*- coding: utf-8 -*-

from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MANAGERS = (
	('info', 'info@kolmaks.ru'),
	('kolmaks', 'kolmaks_tomsk@rambler.ru'),
	('POA', 'poa.webaspect@gmail.com'),
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'kolmaks',
        'USER': 'pgadmin',
        'PASSWORD': 'asdqwe123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['127.0.0.1:8000', 'localhost', 'kolmaks.ru', 'www.kolmaks.ru', 'kolmaks.stokoney.ru', 'www.kolmaks.stokoney.ru']

ROBOTS_SITEMAP_URLS = ['http://kolmaks.ru/sitemap.xml']
ROBOTS_SITEMAP_HOST = 'kolmaks.ru'

DEFAULT_FROM_EMAIL = 'info@kolmaks.ru'
AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'mail.tomuniversal.ru'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'info@kolmaks.ru'
EMAIL_HOST_PASSWORD = 'Ghbdtn!123'
EMAIL_USE_TLS = False
SERVER_EMAIL = 'info@kolmaks.ru'
