from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class URLForm(Form):
    url = StringField('url', id='url-field', validators=[DataRequired(message='Please enter a valid URL'), URL(require_tld=True, message='Enter a valid URL')])
    submit = SubmitField('Get Preview!')
