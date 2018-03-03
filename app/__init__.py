import os

from flask import Flask

from .api import api
from .database import db
from .views import views


# Create the app
app = Flask(__name__)


# Configure the app
config_path = os.environ.get('CONFIG_PATH', 'app.config.DevelopmentConfig')
app.config.from_object(config_path)


# Register the db
db.init_app(app)
db.app = app


# Register the api
api.init_app(app)
api.app = app


# Register the views
app.register_blueprint(views)
