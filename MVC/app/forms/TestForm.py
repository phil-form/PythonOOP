from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class TestForm(FlaskForm):
    class Meta:
        csrf = False
    
    testid = IntegerField("testid", validators=[DataRequired()])
    testtext = StringField("testtext", validators=[DataRequired()])