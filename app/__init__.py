# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
# db object which we will use to interact with the database.


# create_app functiongiven a configuration name, loads the correct
# configuration from the config.py file, as well as the configurations
# from the instance/config.py file.
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
