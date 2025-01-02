from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField, FloatField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, InputRequired


class HmeqForm(FlaskForm):
    loan = IntegerField('Loan amount', validators=[InputRequired()])
    mortdue = IntegerField('Amount due in existing mortgage', validators=[InputRequired()])
    value = IntegerField('Value of current property', validators=[InputRequired()])

    reason = SelectField('Reason for loan', validators=[InputRequired()], choices=[
        ('HomeImp', 'Home improvement'),
        ('DebtCon', 'Debt consolidation')
    ], default='DebtCon')

    job = SelectField('Occupational category', validators=[InputRequired()], choices=[
        ('Other', 'Other'),
        ('ProfExe', 'Professional or Executive'),
        ('Office', 'Office'),
        ('Mgr', 'Manager'),
        ('Self', 'Self-employed'),
        ('Sales', 'Sales')
    ], default='Other')

    yoj = IntegerField('Years present at job', validators=[InputRequired()])
    derog = IntegerField('Number of major derogatory reports', validators=[InputRequired()])
    delinq = IntegerField('Number of delinquent credit lines', validators=[InputRequired()])
    clage = FloatField('Age of oldest credit line', validators=[InputRequired()])
    ninq = IntegerField('Number of recent credit inquiries', validators=[InputRequired()])
    clno = IntegerField('Number of credit lines', validators=[InputRequired()])
    debtinc = IntegerField('Debt to income ratio', validators=[InputRequired()])

    submit = SubmitField('Submit')
