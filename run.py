import os
import json
# from flask framework, import flask class
# from flask framework, import render_template to create a base template for html
# from flask framework, import request function to create backend for the contact form
# from flask framework, import flash function to provide feedback to the user
from flask import Flask, render_template, request, flash
# import env if the system can find an env.py file
if os.path.exists("env.py"):
    import env


app = Flask(__name__) #create an instance of this and store it in a variable called app. The argument is the name of the application's module - our package.
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/") #a decorator (pie-notation). we try to brouwse the root directory.
def index():
    return render_template("index.html") 


@app.route("/about")
def about():
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get('name'))) # by using get method, if there's no name key, it would return None
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
        