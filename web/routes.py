from flask import Flask, render_template, url_for, redirect, request, flash

from forms import *

app = Flask(__name__)
app.secret_key = b';aeirja_)(_9u-a9jdfae90ej-e09!@aldjfa;'

@app.route("/pool")
def home():
    return render_template("home.html")

@app.route("/pool/maint")
def maint():
    return render_template("maint_root.html")

@app.route("/pool/test")
def test():
    return render_template("test.html")

@app.route("/pool/maint/chem")
def chem_root():
    return render_template("chem_root.html")

@app.route("/pool/maint/chem/new")
def chem_new():
    return render_template("chem_new.html")

@app.route("/pool/maint/chem/purch")
def chem_purch():
    return render_template("chem_purch.html")

@app.route("/pool/maint/chem/use")
def chem_use():
    return render_template("chem_use.html")

@app.route("/pool/maint/water")
def water():
    return render_template("water.html")

@app.route("/pool/maint/service")
def service():
    return render_template("service.html")

@app.route("/pool/maint/clean")
def clean():
    return render_template("clean.html")

@app.route("/pool/activity")
def activity():
    return render_template("activity.html")
