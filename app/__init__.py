from flask import Flask



def create_app(config_name):
   app=Flask(__name__)

from app import views