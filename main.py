from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import sqlite3

app = Flask(__name__)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)


@app.route('/')
def index():
    # if not session.get("name"):
    #     return redirect("/login")
    title = "DreamList"
    return render_template("home.html", title=title)


if __name__ == "__main__":
    app.run(debug=True)
