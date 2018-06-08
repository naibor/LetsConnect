import os

class Config(object):
    """parent configuration class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """configurations for development"""
    DEBUG = True

class TestingConfig(Config):
    """configuration for testing,with separate test database """
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """Configurations for staging"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for production"""
    DEBUG = False
    TESTING = False


app_config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'production':ProductionConfig,
}