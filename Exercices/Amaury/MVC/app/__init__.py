from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
import psycopg2

app = Flask("app")
app.config['SECRET_KEY'] = 'random'
app.debug = True

toolbar = DebugToolbarExtension(app)

conn = psycopg2.connect(dbname='mvc', user='user', password='1234', host='127.0.0.1', port='5435')

from app.controllers import *