"""
Example blueprint file

Author: Michelle Chen
"""

from flask import Blueprint

# define blueprint
example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route('/')
def index():
    return "This is example blueprint registered to Flask app."
