'''Seed file to make samaple data for Users Database'''

from models import User, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

#If table isn't empty, empty it
User.query.delete()

#Create some sample users
john = User(first_name='John', last_name='Conner', img_url='https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/John_Connor_%28Jason_Clarke%29.jpg/150px-John_Connor_%28Jason_Clarke%29.jpg')

cruella = User(first_name='Cruella', last_name='Deville', img_url='https://lh3.googleusercontent.com/proxy/ONINH9F1fxwPzIPC66IX7AfHnS6FgubEczLhFWNjs0UHAOqLZMfiyWjMxmqJUEnQDcoYG73syQubbh1e6jSNEWW6ttDV1xsO3b6AzkReY8iD-lQ')

magnito = User(first_name='Erik', last_name='Lehnsherr', img_url='https://s3.tradingview.com/userpics/1486538-s46K_orig.png')

#Move new objects to session so they will persist
db.session.add(john)
db.session.add(cruella)
db.session.add(magnito)

#Commit new bojects
db.session.commit()