from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import (DataRequired, Length, Email, EqualTo, ValidationError)

"""
test - common three on top: additional fields revealed with JS
water
clean
service
activity
reporting
"""

class Chemical_New(FlaskForm):
    name = StringField("Chemical Name", validators=[DataRequired(), Length(max=50)])
    brand = StringField("Chemical Brand", validators=[DataRequired(), Length(max=50)])
    units = StringField("Measure Unit", validators=[DataRequired(), Length(max=10)])
    submit = SubmitField("Add New Chemical")    

# ToDo: Probably build this with javascript natively so I can add more than one at a time.
# Will have to investigate if Flask can accomplish this.
class Chemical_Purchase(FlaskForm):
    name = SelectField("Chemical Name", validators=[DataRequired()])
    store = SelectField("Store Name", validators=[DataRequired()])
    date = DateField("Purchase Date")
    qty = StringField("Amount Purchased")
    cost = StringField("Cost")
    submit = SubmitField("Submit")

class Chemical_Use(FlaskForm):
    name = SelectField("Chemical Name", validators=[DataRequired()])
    date = StringField("Date/Time Used")
    qty = StringField("Amount Used")
    submit = SubmitField("Submit")

class Test(FlaskForm):
    name = SelectField("Test Used", validators=[DataRequired()])
    chl_free = StringField("Free Chlorine")
    ph = StringField("Ph Balance")
    alk = StringField("Alkalinity")
    chl_tot = StringField("Total Chlorine")
    stab = StringField("Stabalizer")
    hrd = StringField("Hardness")
    submit = SubmitField("Submit Test")

class Water(FlaskForm):
    date = DateField("Purchase Date")
    duration = StringField("Fill Duration")
    # gallons and cost will be calculated by the database
    submit = SubmitField("Submit")

class Service(FlaskForm):
    date = DateField("Service Date")
    code = StringField("Service Code")
    desc = StringField("Description")
    company = StringField("Service Company")
    cost = StringField("Service Cost")
    submit = SubmitField("Submit")

class Clean(FlaskForm):
    date = DateField("Clean Date")
    code = StringField("Activity Code")
    desc = StringField("Description")
    submit = SubmitField("Submit")
