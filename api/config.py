import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# Create connexion app instance
connex_app = connexion.App(__name__, specification_dir=basedir+"/objects")

# Get the Flask app instance
app = connex_app.app

# ToDo: Figure out how to set Env Variables and change poolAPI Password
db_uri = "mysql://poolAPI:" + "Os&3MQ5U&H8LdaN7R6mf2" + "@localhost/pool"

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)