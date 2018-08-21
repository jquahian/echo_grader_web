from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


# write python classes to create our forms
# instead of in html
class RegistrationForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Sign Up")

class LogInForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField("Password", validators=[DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Log In")

class GraderForm(FlaskForm):
	submit = SubmitField("Save")
	# need to scope out all of these forms...
	
	