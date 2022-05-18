from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import InputRequired,Length
from ..models import User

class UpdateProfile(FlaskForm):
    username = StringField('New username',validators = [InputRequired])
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')