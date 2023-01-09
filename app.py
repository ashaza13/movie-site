import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from helpers import find_similar, get_trending, get_upcoming, get_nowplaying, get_toprated
from datetime import datetime

# Configure application 
app = Flask(__name__)

DATE_UNFORMATTED = '%Y-%m-%d'
DATE_FORMATTED = '%B %d, %Y'

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        popular = get_trending()
        upcoming = get_upcoming()
        top = get_toprated()
        now = get_nowplaying()

        return render_template("index.html", popular=popular, upcoming=upcoming, top=top, now=now)
    else:
        # Find a list of similar movies
        result = find_similar(request.form.get("movie"))

        for i in range(len(result)):
            if result[i].release_date != '':
                date_object = datetime.strptime(result[i].release_date, DATE_UNFORMATTED)
                string_date = date_object.strftime(DATE_FORMATTED)
                result[i].release_date = string_date
        
        movie_name = request.form.get("movie")

        return render_template("results.html", result=result, movie_name=movie_name)

@app.route("/movie", methods=["GET", "POST"])
def movie():
    return render_template("movie.html")

if __name__ == '__main__':
    app.debug = True
    app.run()