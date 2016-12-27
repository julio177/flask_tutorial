from flask import Flask
from .blue import blue

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(blue)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from .views import hello

