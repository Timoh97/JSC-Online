import os

class config:
    
    
    @staticmethod
    def init_app(app):
        pass

class TestConfig(config):
    pass

class ProdConfig(config):
    pass

class DevConfig(config):
    pass

config_options={
    'development': DevConfig,
    
    'production': ProdConfig,
    
        'test': TestConfig
}
