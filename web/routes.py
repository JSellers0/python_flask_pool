from flask import Flask, render_template, url_for, redirect, request, flash

from web.forms import *
from web.db import API

pool_api = API()

pool = Flask(__name__)
pool.secret_key = b';aeirja_)(_9u-a9jdfae90ej-e09!@aldjfa;'

@pool.route("/")
def home():
    return render_template("home.html")

@pool.route("/test")
def test():
    form = Test_Form()
    return render_template("test.html", form=form)

@pool.route("/test/new", methods=["GET", "POST"])
def test_new():
    form = Test_New_Form()
    if form.validate_on_submit():
        new_test = {"test_name": form.name.data}
        response = pool_api.create_test_type(new_test)
        if response == 200:
            flash("Test {} created successfully".format(form.name.data), "success")
            return redirect(url_for(test))
        elif response == 409:
            flash("Test Name already exists.", "danger")
        else:
            flash("Unknown Error.  I need to build error handling.", "danger")
    return render_template("test_new.html", form=form)

@pool.route("/maint")
def maint():
    return render_template("maint_root.html")

@pool.route("/maint/chem")
def chem_root():
    return render_template("chem_root.html")

@pool.route("/maint/chem/new")
def chem_new():
    form = Chemical_New_Form()
    return render_template("chem_new.html", form=form)

@pool.route("/maint/chem/purch")
def chem_purch():
    form = Chemical_Purchase_Form()
    return render_template("chem_purch.html", form=form)

@pool.route("/maint/chem/use")
def chem_use():
    form = Chemical_Use_Form()
    return render_template("chem_use.html", form=form)

@pool.route("/maint/water")
def water():
    form = Water_Form()
    return render_template("water.html", form=form)

@pool.route("/maint/service")
def service():
    form = Service_Form()
    return render_template("service.html", form=form)

@pool.route("/maint/clean")
def clean():
    form = Clean_Form()
    return render_template("clean.html", form=form)

@pool.route("/activity")
def activity():
    return render_template("activity.html")

@pool.route("/report")
def report():
    return render_template("report_main.html")
