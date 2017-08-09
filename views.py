from flask import Blueprint, render_template
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from models import Pharmacist

# from models import User



views = Blueprint(
    'views',
    __name__,
    template_folder='templates',
    static_folder='static')

# front_end = Blueprint('front_end', __name__, template_folder='templates')

@views.route('/')

# Show all pharmacists

def index():
	pharmacists = session.query(Pharmacist).all()
	return render_template('index.html', pharmacists=pharmacists)

# @front_end.route('/')
# @login_required
# def index():
#     return render_template("index.html")



