from myapp import app
from flask_security import login_required
from myapp.models import db, user_datastore


@app.route('/')
@login_required
def index():
    return 'Hello World!'