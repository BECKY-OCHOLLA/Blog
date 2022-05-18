import os

class Config:
    
    '''
    parent configuration

    '''
  

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get(' SQLALCHEMY_DATABASE_URI')
    QUOTE_API_BASE_URL=os.environ.get('QUOTE_API_BASE_URL')

   
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
    
    DEBUG=True

config_options = {
'development':DevConfig,
 'production':ProdConfig,

 }