from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
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
		# check if the username is arleady in the databas
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
	# make our variables as wtfield classes
	focus_views = RadioField("FOCUS View", validators=[DataRequired()], choices=[("4C", "Apical Four Chamber"), 
		  ("5C", "Apical Five Chamber"),
		  ("PLX", "Parasternal Long Axis"),
		  ("AVSX", "Aortic Valve Short Axis"),
		  ("SXB", "Basal Short Axis"),
		  ("SXA", "Apical Short Axis"),
		  ("RIVC", "Right Ventricular Inflow/Outflow"),
		  ("SC", "Subcostal Four Chamber"),
		  ("PLX", "Parasternal Long Axis"),
		  ("lung", "Lung"),
		  ("unknown", "Unknown")])
	focus_view_other = StringField("Other: ")

	image_quality = RadioField("Image Quality", validators=[DataRequired()], choices=[("unrecognizable", "Most key structures not visible"),
				 ("poor", "Some key structures visible"),
				 ("good", "Most key structures visible"),
				 ("excellent", "All key structures visible")])
	submit = SubmitField("Save")

	normal_pathology = BooleanField("Normal")
	lv_dysfunc_pathology = BooleanField("LV Dysfunction")
	rv_dysfunc_pathology = BooleanField("RV Dysfunction")
	effusion_pathology = BooleanField("Pericardial Effusion")
	mass_pathology = BooleanField("Mass")
	other_pathology = StringField("Other: ")

	wall_motion = RadioField("Wall Motion Abnormality", validators=[DataRequired()], choices=[(0, "Absent"), (1, "Present")])
	orientation = RadioField("Image Orientation", validators=[DataRequired()], choices=[(0, "Unclear"), (1, "Correct")])
	ecg = RadioField("ECG", validators=[DataRequired()], choices=[(0, "Absent"), (1, "Identifiable R-spke")])
	color_doppler = RadioField("Color Doppler", validators=[DataRequired()], choices=[(0, "Absent"), (1, "Present")])
	depth = RadioField("Appropriate Depth", validators=[DataRequired()], choices=[(0, "No"), (1, "Yes")])
	focus_level = RadioField("Focus Level", validators=[DataRequired()], choices=[(0, "Bad"), (1, "Good")])

	next_btn = SubmitField("Next")
	prev_btn = SubmitField("Previous")


	
	
	
	