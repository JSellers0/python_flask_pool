from flask import Flask, render_template, url_for, redirect, request, flash

from forms import *


pool = Flask(__name__)
pool.secret_key = b';aeirja_)(_9u-a9jdfae90ej-e09!@aldjfa;'

@pool.route("/pool")
def home():
    return render_template("home.html")

@pool.route("/pool/test")
def test():
    form = Test_Form()
    return render_template("test.html", form=form)

@pool.route("/pool/maint")
def maint():
    return render_template("maint_root.html")

@pool.route("/pool/maint/chem")
def chem_root():
    return render_template("chem_root.html")

@pool.route("/pool/maint/chem/new")
def chem_new():
    form = Chemical_New_Form()
    return render_template("chem_new.html", form=form)

@pool.route("/pool/maint/chem/purch")
def chem_purch():
    form = Chemical_Purchase_Form()
    return render_template("chem_purch.html", form=form)

@pool.route("/pool/maint/chem/use")
def chem_use():
    form = Chemical_Use_Form()
    return render_template("chem_use.html", form=form)

@pool.route("/pool/maint/water")
def water():
    form = Water_Form()
    return render_template("water.html", form=form)

@pool.route("/pool/maint/service")
def service():
    form = Service_Form()
    return render_template("service.html", form=form)

@pool.route("/pool/maint/clean")
def clean():
    form = Clean_Form()
    return render_template("clean.html", form=form)

@pool.route("/pool/activity")
def activity():
    return render_template("activity.html")

@pool.route("/pool/report")
def report():
    return render_template("report_main.html")