from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

### Main routes
@app.route('/')
def root():
    '''Homepage redirects to list of all users'''
    return redirect('/users')

##User Routes
@app.route('/users')
def users_index():
    '''Displays a page with all users on blogly'''
    
    users = User.query.order_by(User.last_name, User.first_name).all()
    
    return render_template('/users/index.html', users=users)


@app.route('/users/new', methods=["GET"])
def show_new_user_form():
    return render_template('/users/new.html')


@app.route('/users/new', methods=['POST'])
def add_user():
    '''Handle the form submission for creating a new user'''
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url'] or None

    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('/users/show.html', user=user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    '''Show a form to edit the current user'''
    user = User.query.get_or_404(user_id)
    return render_template('/users/edit.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.img_url = request.form['img_url'] or None

    
    db.session.add(user)
    db.session.commit()

    return redirect('/users')


@app.route('/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")



###Posts Routes
@app.route('/users/<int:user_id>/posts/new')
def posts_new_form(user_id):
    '''Show a form to create a new post for a specific user'''
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()

    return render_template('/posts/new.html',user=user, tags=tags)


@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_new_post(user_id):
    '''Show a form to create a new post for a specific user'''
    
    user = User.query.get_or_404(user_id)
    tag_ids = [num for num in request.form.getlist('tags')]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()


    new_post = Post(title = request.form['title'],
                    content = request.form['content'],
                    user = user,
                    tags=tags)
    
    db.session.add(new_post)
    db.session.commit()
    flash(f"Post '{new_post.title}' added!")

    return redirect(f'/users/{user_id}')


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    '''Show a page with details about a users post'''

    post = Post.query.get_or_404(post_id)

    return render_template('posts/show.html', post=post,)


@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):

    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()

    return render_template('/posts/edit.html', post=post, tags=tags)


@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def add_post(post_id):

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    
    tag_ids = [num for num in request.form.getlist('tags')]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    db.session.add(post)
    db.session.commit()
    flash(f"Post '{post.title}' updated!")

    return redirect(f'/users/{post.user.id}')


@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def posts_destroy(post_id):
    """Handle form submission for deleting an existing post"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post.title} deleted.")

    return redirect(f"/users/{post.user_id}")


##Tag Routes

@app.route('/tags')
def show_tags():
    
    tags = Tag.query.all()
    
    return render_template('/tags/index.html', tags=tags)

@app.route('/tags/<int:tag_id>')
def show_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    
    return render_template('tags/show.html', tag=tag)

@app.route('/tags/new')
def new_tag_form():

    return render_template('/tags/new.html')


@app.route('/tags/new', methods=['POST'])
def add_new_tag():

    new_tag = Tag(name = request.form['name'])
    db.session.add(new_tag)
    db.session.commit()
    flash(f"Tag created!")

    return redirect('/tags')

@app.route('/tags/<int:tag_id>/edit')
def edit_tag_form(tag_id):
    tag = Tag.query.get_or_404(tag_id)

    return render_template('/tags/edit.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def update_tag(tag_id):

    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['name']
    db.session.add(tag)
    db.session.commit()

    return redirect('/tags')


@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):

    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()

    return redirect('/tags')

