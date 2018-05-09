from flask import Flask
from flask_security import UserMixin, RoleMixin
from flask_mongoengine import MongoEngine
from ..core import db

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)

class User(db.Document, UserMixin):
    first_name = db.StringField()
    last_name = db.StringField()
    email = db.StringField(max_length=255, unique=True)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def __eq__(self, other):
        return self.id == other.id

    def addRoles(self, new_roles):
        for role in new_roles:
            if not role in self.roles:
                self.roles.append(role)
        self.save()

class Submission(db.Document):
    user = db.ReferenceField(User)
    time = db.DateTimeField()
    data = db.DictField()
