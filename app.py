from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    '''Show the home page'''
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)


@app.route('/new', methods=["GET"])
def show_new_user_form():
    return render_template('create_user.html')

@app.route('/new', methods=['POST'])
def add_user():
    '''Handle the form submission for creating a new user'''
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url'] or None

    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')