import os


class DevelopmentConfig(object):
    DEBUG = True
    PORT = 5028
    # Replace w/ dev postgres
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:password@0.0.0.0:5432/my_service')


class ProductionConfig(object):
    PORT = os.environ.get('PORT')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
