from flask_wtf import FlaskForm
from wtforms import IntegerField,TextAreaField,BooleanField
from wtforms.validators import DataRequired
from app.models import Cereal

class CerealForm(FlaskForm):
    name= TextAreaField("name",validators=[DataRequired()])
    mfr= IntegerField("mfr",validators=[DataRequired()])
    isCold= BooleanField("type",validators=[DataRequired()])
    calories= IntegerField("calories",validators=[DataRequired()])
    protein= IntegerField("protein",validators=[DataRequired()])
    fat= IntegerField("fat",validators=[DataRequired()])
    sodium= IntegerField("sodium",validators=[DataRequired()])
    fiber= IntegerField("fiber",validators=[DataRequired()])
    carbo= IntegerField("carbo",validators=[DataRequired()])
    sugars= IntegerField("sugars",validators=[DataRequired()])
    potass= IntegerField("potass",validators=[DataRequired()])
    vitamins= IntegerField("vitamins",validators=[DataRequired()])
    shelf= IntegerField("shelf",validators=[DataRequired()])
    weight= IntegerField("weight",validators=[DataRequired()])
    cups= IntegerField("cups",validators=[DataRequired()])
    rating= IntegerField("rating",validators=[DataRequired()])
    
