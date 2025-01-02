from flask import Flask, render_template, request, redirect, url_for
from forms.hmeqform import HmeqForm
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import logging

from forms.marketing import MarketingForm

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'hi'

with open('../training/hmeq/pickled/classifier.pkl', 'rb') as f:
    classifier_hmeq: RandomForestClassifier = pickle.load(f)

with open('../training/hmeq/pickled/job_encoder.pkl', 'rb') as f:
    job_encoder_hmeq: LabelEncoder = pickle.load(f)

with open('../training/hmeq/pickled/reason_encoder.pkl', 'rb') as f:
    reason_encoder_hmeq: LabelEncoder = pickle.load(f)

with open('../training/marketing/pickled/job_encoder.pkl', 'rb') as file:
    job_encoder_marketing: LabelEncoder = pickle.load(file)

with open('../training/marketing/pickled/marital_encoder.pkl', 'rb') as file:
    marital_encoder_marketing: LabelEncoder = pickle.load(file)

with open('../training/marketing/pickled/poutcome_encoder.pkl', 'rb') as file:
    poutcome_encoder_marketing: LabelEncoder = pickle.load(file)

with open('../training/marketing/pickled/month_encoder.pkl', 'rb') as file:
    month_encoder_marketing: LabelEncoder = pickle.load(file)

with open('../training/marketing/pickled/contact_encoder.pkl', 'rb') as file:
    contact_encoder_marketing: LabelEncoder = pickle.load(file)

with open('../training/marketing/pickled/education_encoder.pkl', 'rb') as file:
    education_encoder_marketing: LabelEncoder = pickle.load(file)

with open('../training/marketing/pickled/classifier.pkl', 'rb') as file:
    classifier_marketing: RandomForestClassifier = pickle.load(file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hmeq', methods=['GET', 'POST'])
def hmeq():
    form = HmeqForm()
    if request.method == 'GET' or not form.validate_on_submit():
        return render_template('hmeq.html', form=form)

    pred = classifier_hmeq.predict([
        [
            form.loan.data,
            form.mortdue.data,
            form.value.data,
            reason_encoder_hmeq.fit_transform([form.reason.data])[0],
            job_encoder_hmeq.fit_transform([form.job.data])[0],
            form.yoj.data,
            form.derog.data,
            form.clage.data,
            form.ninq.data,
            form.clno.data,
            form.debtinc.data
        ]
    ])

    return render_template('hmeq.html', form=form, result=pred[0])


@app.route('/marketing', methods=['GET', 'POST'])
def marketing():
    form = MarketingForm()
    if request.method == 'GET' or not form.validate_on_submit():
        return render_template('marketing.html', form=form)

    pred = classifier_marketing.predict([[
        form.age.data,
        job_encoder_marketing.fit_transform([form.job.data])[0],
        marital_encoder_marketing.fit_transform([form.marital.data])[0],
        education_encoder_marketing.fit_transform([form.education.data])[0],
        form.default.data,
        form.balance.data,
        form.housing.data,
        form.loan.data,
        contact_encoder_marketing.fit_transform([form.contact.data])[0],
        form.day.data,
        month_encoder_marketing.fit_transform([form.month.data])[0],
        form.campaign.data,
        form.pdays.data,
        form.previous.data,
        poutcome_encoder_marketing.fit_transform([form.poutcome.data])[0]
    ]])

    return render_template('marketing.html', form=form, result=pred[0])
