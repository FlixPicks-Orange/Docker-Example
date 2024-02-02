from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class InsertForm(FlaskForm):
    fname = StringField(validators=[InputRequired(), Length(min=1, max=200)], render_kw={"placeholder" : "First Name"})
    lname = StringField(validators=[InputRequired(), Length(min=1, max=200)], render_kw={"placeholder" : "Last Name"})
    submit = SubmitField("Add Person")