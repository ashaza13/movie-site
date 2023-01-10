import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from helpers import find_similar, get_trending, get_upcoming, get_nowplaying, get_toprated, get_data
from datetime import datetime
from logging import FileHandler, WARNING

# Configure application 
app = Flask(__name__, template_folder="templates")

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

DATE_UNFORMATTED = '%Y-%m-%d'
DATE_FORMATTED = '%B %d, %Y'

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

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
        result = find_similar(request.form.get("movieName"))

        for i in range(len(result)):
            if result[i].release_date != '':
                date_object = datetime.strptime(result[i].release_date, DATE_UNFORMATTED)
                string_date = date_object.strftime(DATE_FORMATTED)
                result[i].release_date = string_date
        
        movie_name = request.form.get("movieName")

        return render_template("results.html", result=result, movie_name=movie_name)

@app.route("/movie/<int:movie_id>/")
def movie_page(movie_id):
    movie_obj = get_data(movie_id)
    return render_template("movie.html", movie_obj=movie_obj)

if __name__ == '__main__':
    app.debug = True
    app.run()