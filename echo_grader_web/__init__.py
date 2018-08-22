from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# in cmd: import secrets
# secrets.token_hex(16) -- or whatever integer
app.config['SECRET_KEY'] = '54bd14cb2afe1e16185f9656e59ed4b6'

# forward slahses indiates a relative file path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# instance our database
db = SQLAlchemy(app)

# import the routes AFTER  initialization

from echo_grader_web import routes