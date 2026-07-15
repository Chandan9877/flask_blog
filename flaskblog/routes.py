from flaskblog.model import User,Post
from flaskblog import app 
from flask import Flask, render_template, url_for, flash,redirect
from flaskblog.forms import RegistrationForm,LoginForm

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!",'success')
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register',form = form)

@app.route('/login',methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in !","sucess")
            return redirect(url_for('home'))
        else:
            flash("Login Uncessful. please check username and password",'danger')
    return render_template('login.html',title = 'Login',form = form)