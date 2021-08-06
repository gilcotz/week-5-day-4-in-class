from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
  #Email, password, submit attributes
  email= StringField('Email', validators =[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit_button = SubmitField()
  
  
