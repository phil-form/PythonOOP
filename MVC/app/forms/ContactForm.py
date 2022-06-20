from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    class Meta:
        csrf = False
    
    email = StringField("email", validators=[DataRequired()])
    text = StringField("text", validators=[DataRequired()])