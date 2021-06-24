from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
        db.app = app
        db.init_app(app)


class User(db.Model):
    '''Database model for Users'''

    __tablename__ = 'users'

    def __repr__(self):
        '''Show additional info about the user'''
        u = self
        return f'<User {u.id} {u.first_name} {u.last_name} {u.img_url}'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(30),
                            nullable=False)
    last_name = db.Column(db.String(30),
                            nullable=False)
    img_url = db.Column(db.String)

    @property
    def full_name(self):
        '''Returns the full name of the user'''
        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    '''Post model'''

    __tablename__ = 'posts'

    def __repr__(self):
        '''Show additional info about posts for debuging purposes'''
        u = self

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.Text,
                        nullable=False)
    content = db.Column(db.Text,
                        nullable=False)
    created_at = db.Column(db.DateTime,
                        nullable=False,
                        default=datetime.datetime.now)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable = False)
    user = db.relationship('User', backref='posts')

    @property
    def friendly_date(self):
        '''return a nicely formatted date for human reading'''
        
        return self.created_at.strftime('%a %b %-d %Y, %-I:%M %p')


    

