import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from helpers import find_similar, get_trending, get_upcoming
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
        for i in range(len(popular)):
            if popular[i].release_date != '':
                date_object = datetime.strptime(popular[i].release_date, DATE_UNFORMATTED)
                string_date = date_object.strftime(DATE_FORMATTED)
                popular[i].release_date = string_date
        
        upcoming = get_upcoming()
        for i in range(len(upcoming)):
            if upcoming[i].release_date != '':
                date_object = datetime.strptime(upcoming[i].release_date, DATE_UNFORMATTED)
                string_date = date_object.strftime(DATE_FORMATTED)
                upcoming[i].release_date = string_date


        return render_template("index.html", popular=popular, upcoming=upcoming)
    else:
        # Find a list of similar movies
        result = find_similar(request.form.get("movie"))

        for i in range(len(result)):
            if result[i].release_date != '':
                date_object = datetime.strptime(result[i].release_date, DATE_UNFORMATTED)
                string_date = date_object.strftime(DATE_FORMATTED)
                result[i].release_date = string_date
            

        return render_template("results.html", result=result)

