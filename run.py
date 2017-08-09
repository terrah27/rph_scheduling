"""
single entry-point that resolves the
import dependencies.  If you're using blueprints, you can import your
blueprints here too.

then when you want to run your app, you point to main.py or `main.app`
"""
from app import app

# from auth import *
from admin import admin
from models import *
from views import *

@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
        db.session.remove()
    db.session.remove()

#register blueprints
# from views import front_end
# # from admin.controllers import admin_bp
# app.register_blueprint(front_end, url_prefix='/')
# # app.register_blueprint(admin_bp, url_prefix='/admin')



if __name__ == '__main__':
	
	app.debug = True
	app.run(host='0.0.0.0', port=5000)