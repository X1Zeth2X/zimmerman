from flask_security.utils import encrypt_password
from flask_security import roles_accepted, roles_required
from flask_admin import Admin, AdminIndexView
from flask_login import login_required
from app import app, api
from flask_restplus import Resource
from models import *
import os

admin = Admin(app, name='Admin Area', template_mode='bootstrap3', index_view=MainAdminIndexView())

""" 
This is to create tables and models in the database.
This should be commented out when the database models are created.
"""
@app.before_first_request
def before_first_request():
    db.create_all
    db.session.commit

@api.route('/hello')
class HelloKonishi(Resource):
    def get(self):
        return {'hello': 'konishi'}


""" Add Admin Views """
admin.add_view(ProtectedModelView(Role, db.session))
admin.add_view(ProtectedModelView(User, db.session))