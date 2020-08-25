from config import db
from api.models import (
    Chemical, 
    Chemical_Purchase, 
    Chemical_Use, 
    Test, 
    Test_Type,
    Service,
    Clean,
    Water)

db.create_all()