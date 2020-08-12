"""Minimal flask app"""

from flask import Flask, render_template

# make the application
app = Flask(__name__)


# make the route
@app.route("/")
# define a function
def hello():
    return render_template('home.html')


# make a second route
@app.route("/about")
# make another function
def preds():
    return render_template('about.html')
