from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from application import db
from datetime import datetime


class Base(db.Document):
    __abstract__ = True
    meta = {'allow_inheritance': True}
    id = db.IntField(primary_key=True, autoincrement=True)
    date_created = db.DateTimeField(nullable=False, default=datetime.utcnow)
    date_modified = db.DateTimeField(nullable=False, default=datetime.utcnow,
                              onupdate=lambda: datetime.utcnow())

    def to_dict(self):
        return {'id': self.id,
                'date_created': self.date_created,
                'date_modified': self.date_modified}


class User(UserMixin, Base):
    # UserClass inherits methods from UserMixin and  is extending from columns in Base (id,date_created, date_modified)
    __tablename__ = 'user'
    name = db.StringField(max_length=50)
    email = db.StringField(max_length=120, unique=True)
    password = db.StringField(nullable=False)
    authenticated = db.BooleanField(default=False)

    def set_password(self, password):  # method to hash password
        self.password = generate_password_hash(password)

    def get_password(self, password):  # method to unhash password and make readable
        return check_password_hash(self.password, password)

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated
