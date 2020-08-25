"""
This is the chemical module and supports all REST actions for the chemical table
"""

from flask import abort
from models import Chemical, ChemicalSchema
from config import db

def read_all():
    chemicals = Chemical.query.order_by(Chemical.chemical_name).all()

    chemical_schema = ChemicalSchema(many=True)
    data = chemical_schema.dump(chemicals)
    return data

def read_id(chemical_id):
    pass

def read_name(chemical_name):
    pass

def read_brand(chemical_brand):
    pass

def create():
    # ToDo: Filter by name and brand
    existing_chemical = Chemical.query.filter(Chemical.chemical_name == chemical_name).one_or_none()

    if existing_chemical is None:
        schema = ChemicalSchema()
        new_chemical = schema.load({"chemical_name": chemical_name}, session=db.session)

        db.session.add(new_chemical)
        db.session.commit()

        return 201

    else:
        abort(
            409,
            "Chemical {} already exists.".format(chemical_name)
        )

def update(chemical_id, chemical):
    pass

def delete(chemical_id, chemcial):
    pass