

from flask_admin.contrib.sqla import ModelView
from models import Pharmacist, Session, User
from app import app, admin


		



#flask admin model views
admin.add_view(ModelView(User, Session))
admin.add_view(ModelView(Pharmacist, Session))

# from flask.ext.admin import Admin, BaseView, expose
# from app import admin

# class MyView(BaseView):
#     @expose('/')
#     def index(self):
#         return self.render('admin.html')
# admin.add_view(MyView(name='Hello'))