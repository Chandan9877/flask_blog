from flaskblog.model import User,Post
from flaskblog import app ,db , bcrypt
from flask import Flask, render_template, url_for, flash,redirect ,request
from flaskblog.forms import RegistrationForm,LoginForm,UpdateAccountForm
from flask_login import login_user , current_user , logout_user , login_required
import secrets
from PIL import Image
import os

posts = [
    {
        'author' : 'Corey Schafer',
        'title' : "Blog post 1",
        'content' : 'First post content', 
        'date_posted' : 'jul 10 , 2026'
    },
    { 
        'author' : 'Jane Doe',
        'title' : "Blog post 2",
        'content' : 'Second post content',
        'date_posted' : 'jul 11 , 2026'
    },
    {
        'author' : 'Marry Joe',
        'title' : "Blog post 3",
        'content' : 'Third post content',
        'date_posted' : 'jul 12 , 2026'
    }
]

@app.route("/")
def home():
    return render_template("home.html",posts = posts,title = 'Home')

@app.route("/about")
def about():
    return render_template("about.html",title = 'About')

@app.route('/register',methods = ['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data,email = form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your acccount has been created now you can login !",'success')
        return redirect(url_for('login'))
    return render_template('register.html',title = 'Register',form = form)


@app.route('/login',methods = ['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login Uncessful. please check username and password",'danger')
    return render_template('login.html',title = 'Login',form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _ , f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path + '/static/profile_pics',picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/account',methods = ['POST','GET'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("your account has been updated",'successs')
        return redirect(url_for('account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename='profile_pics/' + current_user.image_file)
    return render_template('account.html',title="Account",image_file = image_file,form = form)