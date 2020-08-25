#!/usr/bin/python3
import sys
sys.path.insert(0, "/var/www/flask/python_flask_pool/")

from api import config

application = config.app
