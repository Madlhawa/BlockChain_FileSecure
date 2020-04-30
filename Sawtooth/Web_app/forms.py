from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

class maintainenceForm(FlaskForm):
    date = StringField('date', validators = [DataRequired()])
    aircraft_id = StringField('aircraft_id', validators = [DataRequired()])
    aircraft_make = StringField('aircraft_make', validators = [DataRequired()])
    aircraft_owner = StringField('aircraft_owner', validators = [DataRequired()])
    mechanic = StringField('mechanic', validators = [DataRequired()])
    station = StringField('station', validators = [DataRequired()])
    description = StringField('description', validators = [DataRequired()])
    part_supplier = StringField('part_supplier', validators = [DataRequired()])
    part_tracking = StringField('part_tracking', validators = [DataRequired()])
    date_edited = StringField('date_edited', validators = [DataRequired()])
    submit = SubmitField('Submit')
