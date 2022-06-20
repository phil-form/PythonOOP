from flask              import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app                      = Flask("app")
app.config['SECRET_KEY'] = 'random'
app.debug                = True

toolbar = DebugToolbarExtension(app)

from app.controllers import *