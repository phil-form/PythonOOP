from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    userpassword = PasswordField("userpassword", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    userdescription = StringField("userdescription")
    submit = SubmitField('Submit')
