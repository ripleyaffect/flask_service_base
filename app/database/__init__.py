from flask_sqlalchemy import SQLAlchemy


# Initialize the database
db = SQLAlchemy()


# Import all models
from .models import Thing
