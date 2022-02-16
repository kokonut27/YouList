from flask import Flask, render_template, request, url_for, redirect, flash
import json
import os
from replit import db

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config["SECRET_KEY"] = os.environ["secret"]

redirect_home = False

@app.route('/')
def index():
  if redirect_home:
    return render_template("home.html")
  else:
    return render_template("index.html")
    
@app.route('/home')
def home():
  global redirect_home
  try:
    playlists = db["playlists"]
  except:
    playlists = False

  if playlists:
    playlist_exist = True
  else:
    playlist_exist = False
  
  redirect_home = True
  return render_template("home.html", pe=playlist_exist)
    
@app.route('/create', methods = ["GET", "POST"])
def create():
  if request.method == "GET":
    return render_template("create.html")
  if request.method == "POST":
    list_name = request.form["listname"]
    
    db["playlists"] = {
      "playlist_name": list_name,
      "content": None,
    }
    # for x in db["playlists"].items():
    #  print(x)
    flash("The playlist has successfully been created!")
    return redirect(url_for('edit'))
    
@app.route('/edit', methods = ["GET", "POST"])
def edit():
  if request.method == "GET":
    return render_template("edit.html")
  if request.method == "POST":
    
    flash("Your playlist has been successfully edited!")
    return redirect(url_for('home'))


if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = 8080, debug=True)