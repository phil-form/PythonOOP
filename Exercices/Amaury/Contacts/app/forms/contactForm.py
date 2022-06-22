from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    class Meta:
        csrf = False
           
    firstname = StringField("firstname", validators=[DataRequired()])
    lastname = StringField("lastname", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])