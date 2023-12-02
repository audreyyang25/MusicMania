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

@app.route("/composers/Chopin")
def chopin():
    return render_template("chopin.html")
