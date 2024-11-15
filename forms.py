from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
	album_name = StringField('album_name', validators=[DataRequired()])
	submit = SubmitField('Submit')