# imports the __init__.py file in the package
from echo_grader_web import app


# grabs the actual app and runs it
if __name__ == "__main__":
	app.run(debug=True)
