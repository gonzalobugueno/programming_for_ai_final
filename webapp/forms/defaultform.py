from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import InputRequired, NumberRange


class DefaultForm(FlaskForm):
    limit_bal = IntegerField('Credit Limit', validators=[InputRequired(), NumberRange(min=0)])
    sex = SelectField('Sex', validators=[InputRequired()], choices=[
        (1, 'Male'),
        (2, 'Female')
    ])

    education = SelectField('Education', validators=[InputRequired()], choices=[
        (1, 'Graduate school'),
        (2, 'University'),
        (3, 'High school'),
        (4, 'Others'),
        (5, 'Unknown-5'),
        (6, 'Unknown-6'),
        (0, 'Missing (Inferred)')
    ])
    marriage     = SelectField('Marital status', validators=[InputRequired()], choices=[
        (1, 'Married'),
        (2, 'Single'),
        (3, 'Others'),
        (0, 'Missing (Inferred)')
    ])

    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=0)])

    pay_0 = SelectField('Repayment Status (September)', validators=[InputRequired()], choices=[
        (-1, 'Pay duly'),
        (1, 'Payment delay of one month'),
        (2, 'Payment delay of two months'),
        (3, 'Payment delay of three months'),
        (4, 'Payment delay of four months'),
        (5, 'Payment delay of five months'),
        (5, 'Payment delay of six months'),
        (5, 'Payment delay of seven months'),
        (8, 'Payment delay of eight months (and above, inferred)'),
        (0, 'Unknown (0)'),
        (-2, 'Unknown (-2)'),
    ])

    pay_2 = SelectField('Repayment Status (August)', validators=[InputRequired()], choices=[
        (-1, 'Pay duly'),
        (1, 'Payment delay of one month'),
        (2, 'Payment delay of two months'),
        (3, 'Payment delay of three months'),
        (4, 'Payment delay of four months'),
        (5, 'Payment delay of five months'),
        (5, 'Payment delay of six months'),
        (5, 'Payment delay of seven months'),
        (8, 'Payment delay of eight months (and above, inferred)'),
        (0, 'Unknown (0)'),
        (-2, 'Unknown (-2)'),
    ])
    pay_3 = SelectField('Repayment Status (July)', validators=[InputRequired()], choices=[
        (-1, 'Pay duly'),
        (1, 'Payment delay of one month'),
        (2, 'Payment delay of two months'),
        (3, 'Payment delay of three months'),
        (4, 'Payment delay of four months'),
        (5, 'Payment delay of five months'),
        (5, 'Payment delay of six months'),
        (5, 'Payment delay of seven months'),
        (8, 'Payment delay of eight months (and above, inferred)'),
        (0, 'Unknown (0)'),
        (-2, 'Unknown (-2)'),
    ])
    pay_4 = SelectField('Repayment Status (June)', validators=[InputRequired()], choices=[
        (-1, 'Pay duly'),
        (1, 'Payment delay of one month'),
        (2, 'Payment delay of two months'),
        (3, 'Payment delay of three months'),
        (4, 'Payment delay of four months'),
        (5, 'Payment delay of five months'),
        (5, 'Payment delay of six months'),
        (5, 'Payment delay of seven months'),
        (8, 'Payment delay of eight months (and above, inferred)'),
        (0, 'Unknown (0)'),
        (-2, 'Unknown (-2)'),
    ])
    pay_5 = SelectField('Repayment Status (May)', validators=[InputRequired()], choices=[
        (-1, 'Pay duly'),
        (1, 'Payment delay of one month'),
        (2, 'Payment delay of two months'),
        (3, 'Payment delay of three months'),
        (4, 'Payment delay of four months'),
        (5, 'Payment delay of five months'),
        (5, 'Payment delay of six months'),
        (5, 'Payment delay of seven months'),
        (8, 'Payment delay of eight months (and above, inferred)'),
        (0, 'Unknown (0)'),
        (-2, 'Unknown (-2)'),
    ])

    pay_6 = SelectField('Repayment Status (April)', validators=[InputRequired()], choices=[
        (-1, 'Pay duly'),
        (1, 'Payment delay of one month'),
        (2, 'Payment delay of two months'),
        (3, 'Payment delay of three months'),
        (4, 'Payment delay of four months'),
        (5, 'Payment delay of five months'),
        (5, 'Payment delay of six months'),
        (5, 'Payment delay of seven months'),
        (8, 'Payment delay of eight months (and above, inferred)'),
        (0, 'Unknown (0)'),
        (-2, 'Unknown (-2)'),
    ])

    bill_amt1 = IntegerField('Bill Amount (September)', validators=[InputRequired()])
    bill_amt2 = IntegerField('Bill Amount (August)', validators=[InputRequired()])
    bill_amt3 = IntegerField('Bill Amount (July)', validators=[InputRequired()])
    bill_amt4 = IntegerField('Bill Amount (June)', validators=[InputRequired()])
    bill_amt5 = IntegerField('Bill Amount (May)', validators=[InputRequired()])
    bill_amt6 = IntegerField('Bill Amount (April)', validators=[InputRequired()])

    pay_amt1 = IntegerField('Payment Amount (September)', validators=[InputRequired()])
    pay_amt2 = IntegerField('Payment Amount (August)', validators=[InputRequired()])
    pay_amt3 = IntegerField('Payment Amount (July)', validators=[InputRequired()])
    pay_amt4 = IntegerField('Payment Amount (June)', validators=[InputRequired()])
    pay_amt5 = IntegerField('Payment Amount (May)', validators=[InputRequired()])
    pay_amt6 = IntegerField('Payment Amount (April)', validators=[InputRequired()])

    submit = SubmitField('Submit')
