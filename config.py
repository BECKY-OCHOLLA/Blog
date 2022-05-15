import os

class Config:
    '''
    parent configuration

    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'
   

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