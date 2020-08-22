from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import (DataRequired, Length, Email, EqualTo, ValidationError)

"""
activity
reporting
"""

class Chemical_New_Form(FlaskForm):
    name = StringField("Chemical Name", validators=[DataRequired(), Length(max=50)])
    brand = StringField("Chemical Brand", validators=[DataRequired(), Length(max=50)])
    units = StringField("Measure Unit", validators=[DataRequired(), Length(max=10)])
    submit = SubmitField("Add New Chemical")    

# ToDo: Probably build this with javascript natively so I can add more than one at a time.
# Will have to investigate if Flask can accomplish this.
class Chemical_Purchase_Form(FlaskForm):
    name = SelectField("Chemical Name", validators=[DataRequired()])
    store = SelectField("Store Name", validators=[DataRequired()])
    date = DateField("Purchase Date", validators=[DataRequired()])
    qty = StringField("Amount Purchased", validators=[DataRequired()])
    cost = StringField("Cost", validators=[DataRequired()])
    submit = SubmitField("Submit")

class Chemical_Use_Form(FlaskForm):
    name = SelectField("Chemical Name", validators=[DataRequired()])
    date = StringField("Date/Time Used")
    qty = StringField("Amount Used")
    submit = SubmitField("Submit")

class Test_Form(FlaskForm):
    name = SelectField("Test Used", choices=[(None, 'Choose a Test')], validators=[DataRequired()])
    chl_free = StringField("Free Chlorine", validators=[DataRequired()])
    ph = StringField("Ph Balance", validators=[DataRequired()])
    alk = StringField("Alkalinity")
    chl_tot = StringField("Total Chlorine")
    stab = StringField("Stabilizer")
    hrd = StringField("Hardness")
    submit = SubmitField("Submit Test")

class Test_New_Form(FlaskForm):
    name = StringField("Test Name", validators=[DataRequired()])
    submit = SubmitField("Create New Test")

class Water_Form(FlaskForm):
    date = DateField("Purchase Date")
    duration = StringField("Fill Duration")
    # gallons and cost will be calculated by the database
    submit = SubmitField("Submit")

class Service_Form(FlaskForm):
    date = DateField("Service Date")
    code = StringField("Service Code")
    desc = StringField("Description")
    company = StringField("Service Company")
    cost = StringField("Service Cost")
    submit = SubmitField("Submit")

class Clean_Form(FlaskForm):
    date = DateField("Clean Date")
    code = StringField("Activity Code")
    desc = StringField("Description")
    submit = SubmitField("Submit")
