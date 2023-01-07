import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from helpers import find_similar
from datetime import datetime

# Configure application 
app = Flask(__name__)

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # Find a list of similar movies
        result = find_similar(request.form.get("movie"))

        print(result)
        for i in range(len(result)):
            if result[i].release_date != '':
                date_object = datetime.strptime(result[i].release_date, '%Y-%m-%d')
                string_date = date_object.strftime('%B %d, %Y')
                result[i].release_date = string_date
            

        return render_template("results.html", result=result)

