from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class AccountTransfertForm(FlaskForm):    
    fromaccount = IntegerField("fromaccount", validators=[DataRequired()])
    toaccount = IntegerField("toaccount", validators=[DataRequired()])
    amount = IntegerField("amount", validators=[DataRequired()])