from tkinter.tix import Select

from flask_wtf import FlaskForm
from nbformat.validator import validators
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField, FloatField
from wtforms.fields.simple import SubmitField, BooleanField
from wtforms.validators import DataRequired, InputRequired


class MarketingForm(FlaskForm):
    age = IntegerField('Age', validators=[InputRequired()])
    job = SelectField('Type of job', validators=[InputRequired()], choices=[
        ('unknown', 'Unknown'),
        ('admin.', 'Administrative'),
        ('blue-collar', 'Office worker'),
        ('entrepreneur', 'Entrepreneur'),
        ('housemaid', 'Housemaid'),
        ('management', 'Management'),
        ('retired', 'Retired'),
        ('self-employed', 'Self Employed'),
        ('services', 'Services'),
        ('student', 'Student'),
        ('technician', 'Technician'),
        ('unemployed', 'Unemployed')
    ], default='blue-collar')
    marital = SelectField('Marital status', validators=[InputRequired()], choices=[
        ('unknown', 'Unknown'),
        ('divorced', 'Divorced or widowed'),
        ('married', 'Married'),
        ('single', 'Single')
    ], default='married')
    education = SelectField('Education level', validators=[InputRequired()], choices=[
        ('unknown', 'Unknown'),
        ('secondary', 'Secondary'),
        ('primary', 'Primary'),
        ('tertiary', 'Tertiary')
    ], default='secondary')
    default = BooleanField('Has credit in default?', default=False)
    balance = IntegerField('Average yearly balance', validators=[InputRequired()])
    housing = BooleanField('Has housing loan?', default=True)
    loan = BooleanField('Has personal loan?', default=False)
    contact = SelectField('Contact method', validators=[InputRequired()], choices=[
        ('unknown', 'Unknown'),
        ('cellular', 'Cellular'),
        ('telephone', 'Telephone')
    ], default='cellular')
    day = IntegerField('Day of week', validators=[InputRequired()])
    month = SelectField('Month', validators=[InputRequired()], choices=[
        ('jan', 'January'),
        ('feb', 'February'),
        ('mar', 'March'),
        ('apr', 'April'),
        ('may', 'May'),
        ('jun', 'June'),
        ('jul', 'July'),
        ('aug', 'August'),
        ('sep', 'September'),
        ('oct', 'October'),
        ('nov', 'November'),
        ('dec', 'December')
    ], default='may')
    campaign = IntegerField('Contacts this campaign', validators=[InputRequired()])
    pdays = IntegerField('Days since last campaign contact', validators=[InputRequired()])
    previous = IntegerField('Pre-campaign contacts', validators=[InputRequired()])
    poutcome = SelectField("Previous campaign's outcome", validators=[InputRequired()], choices=[
        ('failure', 'Failure'),
        ('nonexistent', 'Non existent'),
        ('success', 'Success'),
        ('unknown', 'Unknown')
    ], default='unknown')

    submit = SubmitField('Submit')