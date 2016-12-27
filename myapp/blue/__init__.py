from flask import Blueprint

blue = Blueprint(
    'site',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/blue'
)

from . import views