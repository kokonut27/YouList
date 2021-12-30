from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import sqlite3

app = Flask(__name__)

"""
def get_board():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    a = []
    num_max = 0
    for row in cur.execute('SELECT * FROM leaderboard ORDER BY score'):
      num_max+=1
      if num_max == 5:
        break
      else:
        a.append(row)
    return '\n\n'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]), a))

# print(get_board())

def add_leader(username2, score2):
  conn = sqlite3.connect('database.db')
  conn.execute("INSERT INTO leaderboard (username, score) VALUES (?, ?)", (username2, score2))
  conn.commit()
  conn.close()
"""

@app.route('/')
def index():
  return render_template("index.html")
    
@app.route('/home')
def home():
  con = sqlite3.connect('database.db')

  if con:
    playlist_exist = True
  else:
    playlist_exist = False
  return render_template("home.html", pe=playlist_exist)
    
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

if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = 8080, debug=True)