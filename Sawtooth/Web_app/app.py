from flask import Flask, render_template, url_for, flash, redirect
from forms import maintainenceForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '141242141424'
record = [
    {
        'date':'04/03/2018',
        'aircraft_id':'N12345',
        'aircraft_make':'2015 cessna 1725',
        'aircraft_owner':'charlie',
        'mechanic':'mike',
        'station':'aero aviation',
        'description':'owner reported',
        'part_supplier':'textron',
        'part_tracking_id':'a123456789'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', record=record)

@app.route("/add", methods=['GET','POST'])
def add():
    form = maintainenceForm()
    if form.validate_on_submit():
        flash(f'Data validated successfully!', 'success')
    return render_template('add.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)