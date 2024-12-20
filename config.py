"""
[General Configuration Params]
"""
from os import path, environ
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    PATH_FILES = 'E:\\python-services\\colf_simulator_core_api\\'
    MODE = 'PRODUCTION'

class TestConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    PATH_FILES = 'E:\\python-services\\colf_simulator_core_api\\'
    MODE = 'TESTING'

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    PATH_FILES = 'D:\\Developer\\Proyectos\\DeberDobleAsesoria\\Proyecto\\'
    MODE = 'DEVELOPMENT'
