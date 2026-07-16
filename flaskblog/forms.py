from flask_wtf  import FlaskForm
from flask_wtf.file import FileAllowed , FileField
from wtforms import StringField, PasswordField , BooleanField, SubmitField, ValidationError , TextAreaField
from wtforms.validators import DataRequired, Length,Email,EqualTo
from flaskblog.model import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators = [DataRequired(),
                                         Length(min=2,max=20)])
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min = 8,max = 100)])
    confirm_password = PasswordField('confirm Password',validators=[DataRequired(),Length(min = 8,max = 100),EqualTo('password')])
    submit = SubmitField('sign up')
    def validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("This username is taken. Please choose a different username.")
    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("This email is taken. Please login or choose another email.") 

class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min = 8,max = 100)])
    remember = BooleanField('remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('username',
                           validators = [DataRequired(),
                                         Length(min=2,max=20)])
    email = StringField('email',validators=[DataRequired(),Email()])
    picture = FileField('update profile picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')


    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError("This username is taken. Please choose a different username.")
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError("This email is taken. Please login or choose another email.") 
            

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('content',validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError("There is no account with this email . You must register first to access") 
        

class ResetPasswordForm(FlaskForm):
    password = PasswordField('password',validators=[DataRequired(),Length(min = 8,max = 100)])
    confirm_password = PasswordField('confirm Password',validators=[DataRequired(),Length(min = 8,max = 100),EqualTo('password')])
    submit = SubmitField('Reset password')