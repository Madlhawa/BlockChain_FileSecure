from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import maintainenceForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '141242141424'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

print(db)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    aircraft_id = db.Column(db.String(20))
    aircraft_make = db.Column(db.String(20))
    aircraft_owner = db.Column(db.String(20))
    mechanic = db.Column(db.String(20))
    station = db.Column(db.String(20))
    description = db.Column(db.String(20))
    date_edited = db.Column(db.DateTime, default=datetime.utcnow)
    Part = db.relationship('Part', backref='author', lazy=True)
    part_supplier = db.Column(db.String(100))
    part_tracking_id = db.Column(db.String)

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_supplier = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    part_tracking_id = db.Column(db.String)
    record_id = db.Column(db.Integer, db.ForeignKey('record.id'), nullable=False)


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
        flash(f'Data validated, and added successfully!', 'success')
        record = Record(date=form.date.data,
                        aircraft_id = form.aircraft_id.data,
                        aircraft_make = form.aircraft_make.data,
                        aircraft_owner = form.aircraft_owner.data,
                        mechanic = form.mechanic.data,
                        station = form.station.data,
                        description = form.description.data,
                        date_edited = datetime.utcnow()
                        )
        db.session.add(record)
        db.session.commit()
    return render_template('add.html', form = form)

@app.route("/all", methods=['GET','POST'])
def all():
    records = Record.query.all()
    return render_template('all.html', records = records)

@app.route("/edit", methods=['GET','POST'])
def edit():
    form = maintainenceForm()
    record_id = request.form['id']
    print('recordID'+record_id)
    records = Record.query.filter_by(id=record_id)
    return render_template('change.html', records = records, form = form)

@app.route("/change", methods=['GET','POST'])
def change():
    form = maintainenceForm()
    flash(f'Data validated, and added successfully!', 'success')
    record = Record(date=form.date.data,
                    aircraft_id = form.aircraft_id.data,
                    aircraft_make = form.aircraft_make.data,
                    aircraft_owner = form.aircraft_owner.data,
                    mechanic = form.mechanic.data,
                    station = form.station.data,
                    description = form.description.data,
                    date_edited = datetime.utcnow()
                    )
    db.session.add(record)
    db.session.commit()
    return render_template('all.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)