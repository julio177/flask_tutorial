from flask import Blueprint

red = Blueprint(
    'other',
    __name__,
    url_prefix='/red'
)

@red.route('/')
def index():
	return 'Red!'