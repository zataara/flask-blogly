from flask_sqlalchemy import SQLAlchemy

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


class Post(db.Model):
    '''Post model'''

    __tablename__ = 'posts'

    def __repr__(self):
        '''Show additional info about posts for debuging purposes'''
        u = self

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(30),
                        nullable=False)
    content = db.Column(db.Text,
                        nullable=False)
    created_at = db.Column(db.DateTime,
                        nullable=False)
    user_id = db.Column(db.Text,
                        db.ForeignKey('user.id'))
    user = db.relationship('User', backref='posts')


    

