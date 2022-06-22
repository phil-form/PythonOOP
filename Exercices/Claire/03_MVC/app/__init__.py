from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf.csrf import CSRFProtect

import psycopg2


app = Flask("app")
app.config['SECRET_KEY'] = 'random'
app.debug = True

# enable CSRF protection globally
csrf = CSRFProtect(app)
toolbar = DebugToolbarExtension(app)

conn = psycopg2.connect(dbname='app', user='app', password='1234', host='127.0.0.1', port='5435')

from app.controllers import *
