'''
File: config.py
Description: Global configuration for Bugzot project
'''
DEBUG = False
SECRET_KEY = 'your_application_secret_key'
BCRYPT_LOG_ROUNDS = 5  # Increase this value as required for your application
SQLALCHEMY_DATABASE_URI = "sqlite:///bugzot.db"
SQLALCHEMY_ECHO = False
STATIC_PATH = 'bugzot/static'
TEMPLATES_PATH = 'bugzot/templates'
SESSION_TYPE='filesystem'
