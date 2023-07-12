# Author: Sakthi Santhosh
# Created on: 22/04/2023
from flask_wtf import FlaskForm
from wtforms import EmailField, FloatField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class AddResponder(FlaskForm):
    first_name = StringField(
        label="First Name",
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    last_name = StringField(
        label="Last Name",
        validators=[Length(min=1, max=50)]
    )
    email_id = EmailField(
        label="Email ID",
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    phone = StringField(
        label="Phone",
        validators=[DataRequired(), Length(min=15, max=15)]
    )
    fr_type = RadioField(
        label="Responder Type",
        choices=[("VG", "Villager"), ("FO", "Forest Officer")],
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit")

class AddDevice(FlaskForm):
    name = StringField(
        label="Name",
        validators=[DataRequired()]
    )
    latitude = FloatField(
        label="Latitude",
        validators=[DataRequired(), NumberRange(min=-90.0, max=90.0)]
    )
    longitude = FloatField(
        label="Longitude",
        validators=[DataRequired(), NumberRange(min=-180.0, max=180.0)]
    )
    submit = SubmitField("Submit")
