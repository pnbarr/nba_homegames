from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import DateField

class DateEntryForm(FlaskForm):
    date = DateField(id='datepick')
    submit =  SubmitField('Search')