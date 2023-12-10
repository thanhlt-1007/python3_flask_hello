from flask import Flask, render_template, request
import sys

sys.path.append("./modules")

import vsearch

# create an instance of a Flask object
# and asign it to "app".

# The __name__ value is maintained by the Python interpreter and,
# when used anywhere within your program's code, is set to the name of the currently active module.
# It turns out that the Flask class needs to know the current value of the __name__ when creating a new Flask object,
# so it must be passed as an argument, which is whay we've used it here (even though its usage does look strange).
app = Flask(__name__)

# Here's the function decorator,
# which-like all decorators-is prefixed with the @ symbol.
# "/" This is the URL
@app.route("/")

# This is just a regular Python function
# which, when invoked, returns a string to its caller (note the -> str annotation)
def root() -> str:
  return "Hello, World!"

@app.route("/home")
def home() -> "html":
  return render_template("home.html", the_title = "Welcome to search4letters on the web!")

@app.route("/search4", methods = ["POST"])
def search4() -> str:
  phrase = request.form["phrase"]
  letters = request.form["letters"]
  return str(vsearch.search4leters(phrase = phrase, letters = letters))
