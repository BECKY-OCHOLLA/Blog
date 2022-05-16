import os

class Config:
    '''
    parent configuration

    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
   

class ProdConfig(Config):
    '''
    child configuration to the parent
    '''
    pass

class DevConfig(Config):
    '''
    child configurations to the parent
    '''
    pass

DEBUG=True

config_options = {
'development':DevConfig,
 'production':ProdConfig,

 }