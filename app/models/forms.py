from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email


class GetLead(FlaskForm):
	email = StringField('Email address', validators=[DataRequired(),Email()])

