from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap



# def create_app(config_name):
app = Flask(__name__,instance_relative_config=True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('Config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)


from .main import views