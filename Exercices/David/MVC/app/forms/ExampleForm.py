from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ExampleForm(FlaskForm):
    class Meta:
        csrf = False
    
    firstname = StringField("firstname", validators=[DataRequired()])
    lastname = StringField("lastname", validators=[DataRequired()])