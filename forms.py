from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange

class PetFormNew(FlaskForm):
    """ Form to add a new pet """
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species = SelectField("Species", choices=[
                            ('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')],
                            validators=[
                            InputRequired(message="Must select a species")])
    photo_url = StringField("Pet photo URL", validators=[Optional(),
                            URL(message="Must be a vaild URL")])
    age = IntegerField("Pet Age", validators=[Optional(),
                        NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")


class PetFormEdit(FlaskForm):
    """ Form to edit a pet """
    photo_url = StringField("Pet photo URL", validators=[Optional(),
                            URL(message="Must be a vaild URL")])
    notes = TextAreaField("Notes")
    available = BooleanField("Pet available")