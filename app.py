"""
Practice Flask app

Requirements:
    - Python 3.*
    - PostgreSQL
    - Flask
    - SQLAlchemy
    - Pytest

Author: Michelle Chen
"""

from flask import Flask, Blueprint, render_template, request
from apis.example_blueprint import example_blueprint

# set up flask app
app = Flask(__name__)
app.secret_key = 'dev'

# Blueprints -------------------------------------
# Blueprints are objects that have resources, templates, views associated with routes
# register the blueprints to your Flask app, actually extending the app to the contents of blueprint
# key concept: they record operations to be executed later whe you register them on an application
#   - Flask records this association to be made in application when blueprint is registered
# Blueprint('blueprint name', import name to locate resources)
#   - static_folder -  where static files can be found for blueprint
#   - static_url_path - url to serve static files from
#   - template_folder - containing blueprint's templates
#   - url_prefix - path to prepend blueprint url
#   - subdomain - subdomain routes will match by default
#   - url_defaults - dictionary of values blueprint's view will receive
#   - root_path - blueprint root directory path, default obtained from import name
app.register_blueprint(example_blueprint, url_prefix='/examples')

@app.route('/', defaults={'path':''})
@app.route('/<string:path>')
@app.route('/<path:path>')
def catch_all(path):
    """Catch all route."""
    return "Welcome to homepage."

@app.route('/')
def index():
    """Render homepage."""
    return "Welcome to homepage."
