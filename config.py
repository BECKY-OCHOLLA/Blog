import os

class config:
    '''
    parent configuration

    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
   

class ProdConfig(config):
    '''
    child configuration to the parent
    '''
    pass

class DevConfig(config):
    '''
    child configurations to the parent
    '''
    pass

DEBUG=True