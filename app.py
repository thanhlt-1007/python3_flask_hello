from flask import Flask
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
def home() -> str:
  return "Hello, World!"

@app.route("/search4")
def search4() -> str:
  return str(vsearch.search4leters(phrase = "life, the universe, and everything", letters = "eiru"))
