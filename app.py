from flask import Flask, url_for, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LogInForm, GraderForm


app = Flask(__name__)

# in cmd: import secrets
# secrets.token_hex(16) -- or whatever integer
app.config['SECRET_KEY'] = '54bd14cb2afe1e16185f9656e59ed4b6'

# forward slahses indiates a relative file path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# instance our database
db = SQLAlchemy(app)

# our user will just contain a username and password
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# we only want to get the person's username and password to sign-up
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	# specify the relationship to the ratings class -- one user to many ratings
	ratings = db.relationship('Ratings', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.username}')"

class Ratings(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# relates our rating to a specific user
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	clip_name = db.Column(db.String(), nullable=False)
	# user rating columns
	view = db.Column(db.String(), nullable=False)
	image_qual = db.Column(db.String(), nullable=False)
	path_normal = db.Column(db.String(), nullable=False)
	lv_dysfunc = db.Column(db.String(), nullable=False)
	rv_dysfunc = db.Column(db.String(), nullable=False)
	pericardial_eff = db.Column(db.String(), nullable=False)
	mass = db.Column(db.String(), nullable=False)
	path_other = db.Column(db.String(), nullable=False)
	wall_motion = db.Column(db.Integer(), nullable=False)
	orientation = db.Column(db.Integer(), nullable=False)
	ecg = db.Column(db.Integer(), nullable=False)
	color_doppler = db.Column(db.Integer(), nullable=False)
	depth = db.Column(db.Integer(), nullable=False)
	focus_lvl = db.Column(db.Integer(), nullable=False)

	# quick print out to see if we're actually recording the 1st, 2nd and last
	# values
	def __repr__(self):
		return f"Ratings({self.clip_name, self.view, self.focus_lvl})"

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

if __name__ == "__main__":
	app.run(debug=True)
