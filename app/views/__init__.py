from flask import Blueprint


# Create the Blueprint
views = Blueprint('views', __name__)


@views.route('/')
def index():
    """App index"""
    return 'Hello world'
