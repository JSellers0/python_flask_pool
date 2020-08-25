from flask import abort
from api.models import TestType, TestTypeSchema, Test
from api.config import db

def get_types():
    test_types = TestType.query.order_by(TestType.testtypeid).all()

    test_type_schema = TestTypeSchema(many=True)
    data = test_type_schema.dump(test_types)

    return data