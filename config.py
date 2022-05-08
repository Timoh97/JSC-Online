import os

class config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    @staticmethod
    def init_app(app):
        pass

class TestConfig(config):
    pass

class ProdConfig(config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Tim:P@ssword@localhost/timothy'
    DEBUG = True

config_options={
    'development': DevConfig,
    
    'production': ProdConfig,
    
        'test': TestConfig
}
