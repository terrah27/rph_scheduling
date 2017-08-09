"""App Config"""
import os



class Config(object):

	DATABASE = {
	    'drivername': 'postgres',
	    'host': 'localhost',
	    'port': '5432',
	    'username': 'postgres',
	    'password': 'postgres',
	    'database': 'pharmacist'
	}

	# Create dummy secrey key so we can use sessions
	SECRET_KEY = '123456790'

	# Flask-Security config
	SECURITY_URL_PREFIX = "/admin"
	SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
	SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

	# Flask-Security URLs, overridden because they don't put a / at the end
	SECURITY_LOGIN_URL = "/login/"
	SECURITY_LOGOUT_URL = "/logout/"
	SECURITY_REGISTER_URL = "/register/"

	SECURITY_POST_LOGIN_VIEW = "/admin/"
	SECURITY_POST_LOGOUT_VIEW = "/admin/"
	SECURITY_POST_REGISTER_VIEW = "/admin/"

	# Flask-Security features
	SECURITY_REGISTERABLE = True
	SECURITY_SEND_REGISTER_EMAIL = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Application threads. A common general assumption is
	# using 2 per available processor cores - to handle
	# incoming requests using one and performing background
	# operations using the other.
	THREADS_PER_PAGE = 2

	# Enable protection agains *Cross-site Request Forgery (CSRF)*
	CSRF_ENABLED     = True

	# Use a secure, unique and absolutely secret key for
	# signing the data. 
	CSRF_SESSION_KEY = "secret"