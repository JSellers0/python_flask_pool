from flask import abort
from api.models import TestType, TestTypeSchema, Test
from api.config import db

def get_types():
    test_types = TestType.query.order_by(TestType.testtypeid).all()

    test_type_schema = TestTypeSchema(many=True)
    data = test_type_schema.dump(test_types)

    return data

def create_type(test_type):
    test_name = test_type.get("test_name")

    existing_type = TestType.query.filter(TestType.test_name == test_name).one_or_none()

    if existing_type is None:
        ttschema = TestTypeSchema()
        new_test = ttschema.load(test_type, session=db.session)

        db.session.add(new_test)
        db.session.commit()

        return 201
        
    else:
        abort(
            409,
            "Test {} already exists.".format(test_name)
        )