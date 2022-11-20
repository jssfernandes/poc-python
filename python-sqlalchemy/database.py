from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, event
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///development.db', echo=True)
# engine = create_engine('mysql://<username>:<password>@<host>:<port>/<databasename>[?<options>]', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine
                                         )
                            )


def init_db():
    Model.metadata.create_all(bind=engine)


Model = declarative_base(name='Model')
# Model = declarative_base()
Model.query = db_session.query_property()

# class Customer(Model):
#     __tablename__ = 'customer'
#
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(140))
#     last_name = Column(String(140))
#     email = Column(String(140))
#
#     def __init__(self, first_name, last_name, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#
#     def to_json(self):
#         return dict(first_name=self.first_name, last_name=self.last_name)
#
#     @property
#     def __eq__(self, other):
#         return type(self) is type(other) and self.id == other.id
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
