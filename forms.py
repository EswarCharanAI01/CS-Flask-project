from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length , Email, EqualTo


# if DataRequired() is mentioned, then it can't be empty


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=6,max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=6,max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')                        
    submit = SubmitField('Login')    