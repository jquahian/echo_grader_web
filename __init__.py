from flask import Flask


app = Flask(__name__)

from echo_grader_web import routes
