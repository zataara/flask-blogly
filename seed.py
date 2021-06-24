'''Seed file to make samaple data for Users Database'''

from models import User, Post, db
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

#Commit new objects
db.session.commit()


#Create some sample posts
post1 = Post(title='Judgement Day', content="It happened on July 3rd 1991, the day the machines have taken over" ,user_id=1)

post2 = Post(title='What is Skynet', content='What exactly is Skynet and how did it become aware?' ,user_id=1)

post3 = Post(title='Time Travel', content='Would it be possible for me to go back in time to stap the machines?' ,user_id=1)

post4 = Post(title='Fur Coats', content="I'm so obsessed with fur coats, I don't know what to do" ,user_id=2)

post5 = Post(title='New Assistant', content='Today I got a new assistant, her name is Anita, she is such a darling' ,user_id=2)

post6 = Post(title='Jailtime', content='I have been in jail now for sometime, I just miss my fur coats' ,user_id=2)

post7 = Post(title='Metal Mind', content='My mind feels like metal, I like it' ,user_id=3)

post8 = Post(title='Magnito', content='I have decided to call myself Magnito' ,user_id=3)

post9 = Post(title='Apocalypse', content='There is a new X Man in town named Apocalypse' ,user_id=3)


db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(post4)
db.session.add(post5)
db.session.add(post6)
db.session.add(post7)
db.session.add(post8)
db.session.add(post9)


db.session.commit()