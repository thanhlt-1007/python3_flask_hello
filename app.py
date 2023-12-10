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

def log_request(request, response: str = "") -> None:
  with open("app.log", "a") as file:
    print("request:", request, file = file)
    print("response:", response, file = file)

# Here's the function decorator,
# which-like all decorators-is prefixed with the @ symbol.
# "/" This is the URL
@app.route("/")
@app.route("/home")
def home() -> "html":
  return render_template("home.html", the_title = "Welcome to search4letters on the web!")

@app.route("/search4", methods = ["POST"])
def search4() -> "html":
  phrase = request.form["phrase"]
  letters = request.form["letters"]
  title = "Here are your results:"
  results = vsearch.search4leters(phrase = phrase, letters = letters)
  log_request(request = request, response = results)
  return render_template("search4.html",
                         the_phrase = phrase,
                         the_letters = letters,
                         the_title = title,
                         the_results = str(results))

@app.route("/logs")
def logs() -> str:
  with open("app.log") as logs:
    contents = logs.read()
  return contents
