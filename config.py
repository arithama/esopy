import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ## alterar as variáveis abaixo (flasky) depois de criar nome para app
    ESOPY_MAIL_SUBJECT_PREFIX = '[Esopy]'
    ESOPY_MAIL_SENDER = 'Esopy Admin <esopy@example.com>'
    ESOPY_ADMIN = os.environ.get('ESOPY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ESOPY_POSTS_PER_PAGE = os.environ.get('ESOPY_POSTS_PER_PAGE')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')
        
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}