import imp
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class userForm(FlaskForm):
    class Meta:
        csrf = True

    username = StringField("username",    validators=[DataRequired()])
    password = StringField("password",    validators=[DataRequired()])
    mail     = StringField("mail",        validators=[DataRequired()])
    description = StringField("description")