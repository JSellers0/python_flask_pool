from datetime import datetime
from config import db, ma

class Chemical(db.Model):
    chemicalid = db.Column(db.Integer, primary_key=True)
    chemical_name = db.Column(db.String(50), nullable=False)
    chemical_brand = db.Column(db.String(50), nullable=False)
    chemical_units = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return "Chemical({}, {}, {})".format(chemical_id, chemical_name, chemical_brand)

class ChemSchema(ma.ModelSchema):
    class Meta:
        model = Chemicals
        sqla_session = db.session

class Chemical_Purchase(db.Model):
    chempurchid = db.Column(db.Integer, primary_key=True)
    chemicalid = db.Column(db.Integer, db.Foreign_Key("chemicals.chemicalid"), nullable=False)
    storeid = db.Column(db.Integer, db.Foreign_Key("store.storeid"), nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False)
    purchase_qty = db.Column(db.Integer, nullable=False)
    purchase_cost = db.Column(db.Numeric(precision=6, scale=2), nullable=False)

class ChemPurchSchema(ma.ModelSchema):
    class Meta:
        model = Chemicals_Purchases
        sqla_session = db.session

class Chemical_Use(db.Model):
    chemuseid = db.Column(db.Integer, primary_key=True)
    chemicalid = db.Column(db.Integer, db.Foreign_Key("chemicals.chemicalid"), nullable=False)
    used_date = db.Column(db.DateTime, nullable=False)
    used_qty = db.Column(db.Integer, nullable=False)

class Test(db.Model):
    chemtestid = db.Column(db.Integer, primary_key=True)
    test_type = db.Column(db.String(50), nullable=False)
    chl_free = db.Column(db.Float(precision=2), nullable=False)
    ph = db.Column(db.Float(precision=2), nullable=False)
    alk = db.Column(db.Integer, nullable=False)
    chl_tot = db.Column(db.Integer)
    stab = db.Column(db.Integer)
    hrd = db.Column(db.Integer)

class Water(db.Model):
    wateraddid = db.Column(db.Integer, primary_key=True)
    add_date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Numeric(precision=5, scale=2), nullable=False)
    cost = db.Column(db.Numeric(precision=6, scale=2), nullable=False)

class Service(db.Model):
    serviceid = db.Column(db.Integer, primary_key=True)
    service_date = db.Column(db.DateTime, nullable=False)
    service_code = db.Column(db.String(50), nullable=False)
    service_desc = db.Column(db.String(250))
    company = db.Column(db.String(150))
    cost = db.Column(db.Numeric(precision=7, scale=2), nullable=False)

class Clean(db.Model):
    cleanid = db.Column(db.Integer, primary_key=True)
    clean_date = db.Column(db.DateTime, nullable=False)
    clean_code = db.Column(db.String(50), nullable=False)
    clean_desc = db.Column(db.String(250))





