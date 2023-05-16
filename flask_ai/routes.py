


from flask_ai import app
from flask import render_template



@app.route("/")
def home():
    return render_template("main.html")






