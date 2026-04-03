from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FileField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    bedrooms = IntegerField('No. of Rooms', validators=[DataRequired(), NumberRange(min=1)])
    bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired(), NumberRange(min=1)])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=1)])
    property_type = SelectField(
        'Property Type',
        choices=[
            ('House', 'House'),
            ('Apartment', 'Apartment')
        ],
        validators=[DataRequired()]
    )
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField(
        'Photo',
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
        ]
    )
    submit = SubmitField('Add Property')