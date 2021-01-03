from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

app = Flask(__name__)

app.config['SECRET_KEY'] = 'n'

class NumForm(FlaskForm):
    num = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Track Phone Number')

@app.route('/', methods=['GET', 'POST'])
def index():

    form = NumForm()
    if form.validate_on_submit():
        session['num'] = form.num.data

        country_num = phonenumbers.parse(session['num'], "CH")
        country = geocoder.description_for_number(country_num, "en")

        service_num = phonenumbers.parse(session['num'], "RO")
        service = carrier.name_for_number(service_num, "en")

        return render_template('result.html', country=country, service=service)

    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
