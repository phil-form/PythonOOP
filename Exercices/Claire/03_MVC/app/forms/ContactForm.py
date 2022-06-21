from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    class Meta:
        csrf = False

    first_name = StringField("first_name", validators=[DataRequired()])
    last_name = StringField("last_name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    submit = SubmitField('Submit')
