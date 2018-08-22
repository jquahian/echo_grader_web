from flask import url_for, render_template, flash, redirect
# specify the package name for imports
from echo_grader_web import app
from echo_grader_web.forms import RegistrationForm, LogInForm, GraderForm
from echo_grader_web.models import User, Ratings


@app.route("/")
def login():
	form = LogInForm()
	return render_template("login.html", title="Login", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# .data .data .data
		flash(f"Account Created for {form.username.data}")
		# redirects to our 'home' route which is defined by the function 'login'
		return redirect(url_for('login'))
	return render_template("registration.html", title="Register", form=form)

@app.route("/grader")
def grader():
	form = GraderForm()
	return render_template("grader.html", title="Grader", form=form)
