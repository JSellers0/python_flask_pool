#!/usr/bin/python3
import sys
sys.path.insert(0, "/var/www/flask/python_flask_pool/")

from web import routes

application = routes.pool
