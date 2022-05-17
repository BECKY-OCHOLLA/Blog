import os

class Config:
    
    '''
    parent configuration

    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'love1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
   

class ProdConfig(Config):
    '''
    child configuration to the parent
    '''
    pass

class DevConfig(Config):
    '''
    child configurations to the parent
    '''
    # SQLALCHEMY_DATABASE_URI = '"sqlite:///database.sqlite"://moringa:access@localhost/pitchy'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'
   
    DEBUG=True

config_options = {
'development':DevConfig,
 'production':ProdConfig,

 }