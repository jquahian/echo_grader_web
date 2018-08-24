from flask import url_for, render_template, flash, redirect
# specify the package name for imports
from echo_grader_web import app, db, bcrypt
from echo_grader_web.forms import RegistrationForm, LogInForm, GraderForm
from echo_grader_web.models import User, Ratings
# our logic file
import echo_grader_web.logic as logic
# will handle users logging in
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=['GET', 'POST'])
def login():
	form = LogInForm()
	if form.validate_on_submit():
		# check if the entered username is in the database
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			# call functions from the logic script here
			return redirect(url_for('grader'))
		else:
			flash('nope')
	return render_template("login.html", title="Login", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# next we hash the password that they enter and decode to string
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		# create new instance for a user
		user = User(username=form.username.data, password=hashed_password)
		# add the user to the database
		db.session.add(user)
		db.session.commit()
		flash(f"Account Created")
		# redirects to our 'home' route which is defined by the function 'login'
		return redirect(url_for('grader'))
	return render_template("registration.html", title="Register", form=form)

# add this decorator to make sure people are logged in to get to this page
@app.route("/grader", methods=['GET', 'POST'])
# this is working, but we need a logout function or else the user
# is perpertually logged in... which might be fine?
@login_required
def grader():
	form = GraderForm()
	counter = 0
	if form.validate_on_submit():
		counter += 1 
		next_clip = logic.video_list[counter]
		return redirect(url_for('login'))
	else:
		counter=3

	init_vid = logic.video_list[counter]
	return render_template("grader.html", title="Grader", form=form, clip=init_vid, counter=counter)
	# submit the form options to the database by making a new Ratings class
		
# need to put this into the HTML file
@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))