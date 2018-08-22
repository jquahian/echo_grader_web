from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from echo_grader_web.models import User


# write python classes to create our forms instead of in html
class RegistrationForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Sign Up")

	# use this function to validate the fields
	def validate_username(self, username):
		# check if the username is arleady in the database
		user = User.query.filter_by(username=username.data).first()
		# if the username already exists...
		if user:
			raise ValidationError('User exists')

class LogInForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField("Password", validators=[DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Log In")

class GraderForm(FlaskForm):
	submit = SubmitField("Save")
	# need to scope out all of these forms...
	
	