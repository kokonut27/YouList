from flask import Flask, render_template, request, url_for, redirect
import json
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/home')
def home():
  return render_template("home.html")

@app.route('/create', methods = ["GET", "POST"])
def create():
  if request.method == "GET":
    return render_template("create.html")
  if request.method == "POST":
    list_name = request.form["listname"]

    # flash("The playlist has successfully been created!")
    return redirect(url_for('home'))

@app.route('/edit', methods = ["GET", "POST"])
def edit():
  if request.method == "GET":
    return render_template("edit.html")
  if request.method == "POST":

    # flash("Your playlist has been successfully edited!")
    return redirect(url_for('home'))

app.run(host = "0.0.0.0", port = 3000, debug=True)