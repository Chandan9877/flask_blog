from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField , BooleanField, SubmitField
from wtforms.validators import DataRequired, Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators = [DataRequired(),
                                         Length(min=2,max=20)])
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min = 8,max = 100)])
    confirm_password = PasswordField('confirm Password',validators=[DataRequired(),Length(min = 8,max = 100),EqualTo('password')])
    submit = SubmitField('sign up')

class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min = 8,max = 100)])
    remember = BooleanField('remember Me')
    submit = SubmitField('Login')
