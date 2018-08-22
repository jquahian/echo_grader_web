from echo_grader_web import db, login_manager
from flask_login import UserMixin


# reloads the user by id
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# our user will just contain a username and password
class User(db.Model, UserMixin):
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
		return f"Ratings('{self.clip_name, self.view, self.focus_lvl}'')"
