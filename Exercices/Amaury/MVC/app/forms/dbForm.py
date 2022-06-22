from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class DbForm(FlaskForm):
    class Meta:
        csrf = False
    
    testid = IntegerField("id", validators=[DataRequired()])
    testtext = StringField("text", validators=[DataRequired()])