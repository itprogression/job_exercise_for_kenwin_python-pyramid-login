import datetime #<- will be used to set default dates on models

from sqlalchemy import (
    Column,
    Integer,
    Unicode,     #<- will provide Unicode field
    UnicodeText, #<- will provide Unicode text field
    DateTime,    #<- time abstraction field
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


from passlib.apps import custom_app_context as blogger_pwd_context

from dashboard.models.meta import Base  #<- we need to import our sqlalchemy metadata from which model classes will inherit


class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    user_name = Column(Unicode(255), unique=True, nullable=False)
    password_salt = Column(Unicode(255), nullable=False)
    password_hash = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)
    related_id = Column(Integer, nullable=False)

    def verify_password(self, password):
        # is it cleartext?
        if password == self.password:
            self.set_password(password)

        return blogger_pwd_context.verify(password, self.password)

    def set_password(self, password):
        password_hash = blogger_pwd_context.encrypt(password)
        self.password = password_hash
