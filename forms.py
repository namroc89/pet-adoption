from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, NumberRange, Optional, URL


class PetForm(FlaskForm):
    """Form for entering pet information"""

    name = StringField("Name", validators=[InputRequired(
        message="Name cannot be left empty")])
    species = SelectField("Species", choices=[
                          ("cat", "Cat"), ("dog", 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[
                            URL(message="Must be valid URL"), Optional()])

    age = IntegerField("Age", validators=[NumberRange(min=0,
                                                      max=30, message="Age must be betwwen 0 and 30"), Optional()])

    notes = TextAreaField("Notes")

    available = BooleanField(
        "Is this animal available for adoption?", default="checked")
