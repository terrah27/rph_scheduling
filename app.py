#app.py


### Keep me very thin - flask instance lives here! ###

from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config)
from models import db
db.init_app(app)

from flask_admin import Admin
admin = Admin(app, name='Pharmacist Scheduling', template_mode='bootstrap3')

import views
app.register_blueprint(views.views)



		




