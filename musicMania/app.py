import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("layout.html")

# optimize later!!
@app.route("/home")
def home():
    return render_template("layout.html")

@app.route("/quiz")
def quiz():
    return render_template("mcquiz.html")

@app.route("/piece")
def pieceQuiz():
    return render_template("piece.html")

@app.route("/composers")
def composers():
    return render_template("composers.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/Chopin")
def chopin():
    return render_template("chopin.html")

@app.route("/Liszt")
def liszt():
    return render_template("liszt.html")

@app.route("/Mendelssohn")
def mendelssohn():
    return render_template("mendelssohn.html")

@app.route("/Debussy")
def debussy():
    return render_template("debussy.html")

@app.route("/Prokofiev")
def prokofiev():
    return render_template("prokofiev.html")

@app.route("/Gershwin")
def gershwin():
    return render_template("gershwin.html")

@app.route("/Bach")
def bach():
   return render_template("bach.html")

@app.route("/Handel")
def handel():
   return render_template("handel.html")

@app.route("/Vivaldi")
def vivaldi():
   return render_template("vivaldi.html")

@app.route("/Mozart")
def mozart():
   return render_template("mozart.html")

@app.route("/Beethoven")
def beethoven():
   return render_template("beethoven.html")

@app.route("/Schubert")
def schubert():
   return render_template("schubert.html")
