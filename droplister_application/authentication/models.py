from werkzeug.security import generate_password_hash, check_password_hash

__author__ = 'bryan'

from droplister_application import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


# Many to Many Relationships

users_roles = db.Table('user_role',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    pwdhash = db.Column(db.String(255))
    admin = db.Column(db.Boolean, default=False)

    # country_id = db.Column(db.Integer, ForeignKey('country.id'))
    # country = relationship("Country", backref=backref("users", order_by=id))

    def __init__(self, name, last_name, email, password, admin=False):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.pwdhash = generate_password_hash(password)
        # self.country = country
        self.admin = admin

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def is_admin(self):
        return self.admin

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)

    # relationships
    users = relationship('User', secondary=users_roles, backref=backref('roles', lazy='dynamic'), lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW |
                     Permission.COMMENT |
                     Permission.WRITE_ARTICLES, True),
            'Moderator': (Permission.FOLLOW |
                          Permission.COMMENT |
                          Permission.WRITE_ARTICLES |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __str__(self):
        return self.name

