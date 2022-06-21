from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
import psycopg2

app = Flask("app")
app.config['SECRET_KEY'] = "Rg@O<z7Jd$C%j;C,aKD?O`8fwC(1$'E~"
app.debug = True

toolbar = DebugToolbarExtension(app)

conn = psycopg2.connect(dbname='app', user='app', password='1234', host='127.0.0.1', port='5435')

from app.controllers import *