from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "mykey"

class SimpleForm(FlaskForm):
    breed = StringField("What's the breed of your dog?", validators=[DataRequired()])
    submit = SubmitField('SUBMIT')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SimpleForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        #flash("Your dog breed is: ")
        return redirect(url_for('home'))

    return render_template("home.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
