"""
This is the chemical module and supports all REST actions for the chemical table
"""

from flask import abort, make_response
from api.models import Chemicals, ChemSchema
from api.config import db

def read_all():
    chemicals = Chemicals.query.order_by(Chemicals.chemicalid).all()

    chemical_schema = ChemSchema(many=True)
    data = chemical_schema.dump(chemicals)
    return data

def read_id(chemical_id):
    chemical = Chemicals.query.filter(Chemicals.chemicalid == chemical_id).one_or_none()

    if chemical is not None:
        chem_schema = ChemSchema()
        data = chem_schema.dump(chemical)
        return data, 200
    else:
        abort(
            404,
            "Chemical record not found for {}.".format(chemical_id)
        )

def read_name(chemical_name):
    chemical = Chemicals.query.filter(Chemicals.chemicalid == chemical_name).one_or_none()

    if chemical is not None:
        chem_schema = ChemSchema()
        data = chem_schema.dump(chemical)
        return data, 200
    else:
        abort(
            404,
            "Chemical record not found for {}.".format(chemical_name)
        )

def read_brand(chemical_brand):
    chemical = Chemicals.query.filter(Chemicals.chemicalid == chemical_brand).one_or_none()

    if chemical is not None:
        chem_schema = ChemSchema()
        data = chem_schema.dump(chemical)
        return data, 200
    else:
        abort(
            404,
            "Chemical record not found for {}.".format(chemical_brand)
        )

def create(chemical):
    chem_name = chemical.get("name")
    chem_brand = chemical.get("chemical_brand")

    existing_chemical = Chemicals.query.filter(
        Chemicals.chemical_name == chem_name
        ).filter(
            Chemicals.chemical_brand == chem_brand
        ).one_or_none()

    if existing_chemical is None:
        schema = ChemSchema()
        new_chemical = schema.load(chemical, session=db.session)

        db.session.add(chemical)
        db.session.commit()

        return 201

    else:
        abort(
            409,
            "Chemical {} already exists.".format(chem_name)
        )

def update(chemical_id, chemical):
    # Check for Chemical by ID
    update_chem = Chemicals.query.filter(Chemicals.chemicalid == chemical_id).one_or_none()

    # Check for Chemical by Name and Brand so we don't create a duplicate
    chem_name = chemical.get("chemical_name")
    chem_brand = chemical.get("chemical_brand")

    exist_chem = Chemicals.query.filter(
        Chemicals.chemical_name == chem_name
    ).filter (
        Chemicals.chemical_brand == chem_brand
    ).one_or_none()

    # Handle existing chem denial first
    if exist_chem is not None:
        abort(
            409,
            "Chemical already exists for {} - {}.".format(chem_brand, chem_name)
        )
    # Handle no ChemID next
    elif update_chem is None:
        abort(
            404,
            "Chemical record not found for {}.".format(chemical_id)
        )
    # Otherwise, update record
    else:
        chem_schema = ChemSchema()
        update = chem_schema.load(chemical, session=db.session)

        db.session.merge(update)
        db.session.commit()

        data = chem_schema.dump(chemical)

        return data, 200

def delete(chemical_id):
    chemical = Chemicals.query.filter(Chemicals.chemicalid == chemical_id).one_or_none()

    if chemical is not None:
        db.session.delete(chemical)
        db.session.commit()
        return make_response(
            "Chemical {} deleted.".format(chemical_id), 200
        )
    else:
        abort(
            404,
            "Chemical record not found for {}.".format(chemical_id)
        )