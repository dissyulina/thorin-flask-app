import os
import json
from flask import Flask, render_template #import flask class from flask framework


app = Flask(__name__) #create an instance of this and store it in a variable called app. The argument is the name of the application's module - our package.


@app.route("/") #a decorator (pie-notation). we try to brouwse the root directory.
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
        