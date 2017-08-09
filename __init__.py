# #__init__.py

# from flask import Flask
# import config
# from utils import get_instance_folder_path




# app = Flask(__name__, instance_path=get_instance_folder_path(),
# 	instance_relative_config=True,
# 	template_folder='templates')
# app.config.from_object(config)

# # create a Admin class instance and associate it with the Flask application instance:
# from flask.ext.admin import Admin
# from models import MyView
# admin = Admin(app, name='Pharmacist Scheduling', template_mode='bootstrap3', url='/admin', endpoint='admin')
# admin.add_view(MyView(name='Hello'))

# #register blueprints
# from front_end.controllers import front_end
# # from admin.controllers import admin_bp
# app.register_blueprint(front_end, url_prefix='/')
# # app.register_blueprint(admin_bp, url_prefix='/admin')


