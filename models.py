
###n models imports app but app doesn't import models so no loop here!


from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, Boolean, DateTime, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.engine.url import URL
from config import Config
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


from flask_admin import helpers as admin_helpers



db = SQLAlchemy()
engine = create_engine(URL(**Config.DATABASE))

Session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = Session.query_property()
Base.metadata.create_all(bind=engine)







class RolesUsers(Base):
    __tablename__ = 'roles_users'

    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))

    @property
    def serialize(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'role_id':self.role_id
        }


class Role(Base, RoleMixin):
    __tablename__ = 'role'

    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name':self.name,
            'description':self.description
        }


class User(Base, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    active = Column(Boolean())
    roles = relationship('Role', secondary='roles_users', backref=backref('users', lazy='dynamic'))

    @property
    def serialize(self):
        return {
            'email': self.email,
            'password': self.password,
            'active': self.active,
            'roles': self.roles
        }

#pharmacist models
class Pharmacist(Base):
    __tablename__ = 'pharmacist'

    rph_id = Column(Integer, primary_key=True)
    rph_name = Column(String(50), nullable=False)
    rph_email = Column(String(50), nullable=False)
    rph_position = Column(String(3), nullable=False)
    pdos_year = Column(Integer, nullable=False)
    pdos_used = Column(Integer, nullable=False)

    @property
    def serialize(self):
        return {
            'rph_id': self.rph_id,
            'rph_name': self.rph_name,
            'rph_email': self.rph_email,
            'position':self.position,
            'pdos_year': self.pdos_year,
            'pdos_used': self.pdos_used
        }

# Configure Flask Security
# user_datastore = SQLAlchemyUserDatastore(Session, User, Role)
# security = Security(app, user_datastore)

# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='admin@admin.com', password='password')
#     db_session.commit()




# # This processor is added to all templates
# @security.context_processor
# def security_context_processor():
#     return dict(hello="world")

