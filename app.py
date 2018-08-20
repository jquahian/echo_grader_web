from flask import Flask, url_for, render_template, redirect, session, logging
from wtforms import form, StringField, TextAreaField, PasswordField, validators


app = Flask(__name__)

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/grader")
def grader():
	return render_template("grader.html")

if __name__ == "__main__":
	app.run(debug=True)
