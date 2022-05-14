from flask import Flask
from config import DevConfig
from config import config_options
from flask_bootstrap import Bootstrap


def create_app(config_name):
  app = Flask(__name__)


# Creating the app configurations
  app.config.from_object(config_options)
    
    
# app = Flask(__name__,instance_relative_config=True)

# Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')


# Initializing Flask Extensions
bootstrap = Bootstrap()
# from .main import views