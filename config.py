import os

class Config:
    '''
    parent configuration

    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
   

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