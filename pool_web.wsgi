activate_this = "/var/www/flask/flask_env/bin/activate_this.py"
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, "/var/www/flask/python_flask_pool/")

from web import routes

application = routes.pool
