from . import blue

@blue.route('/')
def index():
	return 'Blue!'