# config
from flask import (Blueprint, render_template)

bp = Blueprint('fact', __name__, url_prefix='/facts')

# fact form route
@bp.route('/new')
def index():
    return render_template('fact_form.html')