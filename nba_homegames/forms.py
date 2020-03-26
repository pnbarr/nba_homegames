from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from nba_homegames.models import User
from flask_login import current_user

# Class for Registration Form, inherits from FlaskForm
class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators = [DataRequired(), EqualTo('password')])
    submit =  SubmitField('Sign Up')

    def validate_username(self, username):
        #  Query database to see if username already exists
        user = User.query.filter_by(username = username.data).first()
        #  If username already exists, throw validation error
        if user:
            raise ValidationError('Username entered is already taken. Please choose another one.')

    def validate_email(self, email):
        #  Query database to see if email already exists
        user = User.query.filter_by(email = email.data).first()
        #  If email already exists, throw validation error
        if user:
            raise ValidationError('Email entered is alread taken. Please choose another one.')

# Class for Login Form, inherits from FlaskForm
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit =  SubmitField('Login')

# Class for Update Account Form, inherits from FlaskForm
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                            validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    submit =  SubmitField('Update')

    def validate_username(self, username):
        #  Validate only if new username is different than old username
        if username.data != current_user.username:
            #  Query database to see if username already exists
            user = User.query.filter_by(username = username.data).first()
            #  If username already exists, throw validation error
            if user:
                raise ValidationError('Username entered is already taken. Please choose another one.')

    def validate_email(self, email):
        #  Validate only if new email is different than old email
        if email.data != current_user.email:
            #  Query database to see if email already exists
            user = User.query.filter_by(email = email.data).first()
            #  If email already exists, throw validation error
            if user:
                raise ValidationError('Email entered is alread taken. Please choose another one.')