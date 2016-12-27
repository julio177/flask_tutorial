from flask import Flask
from .blue import blue
from .views.red import red

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(blue)
app.register_blueprint(red)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from .views import hello