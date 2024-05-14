from flask_wtf import FlaskForm
from wtforms import IntegerField,DecimalField,TextAreaField,BooleanField
from wtforms.validators import DataRequired,ValidationError
from app.models import Cereal

def cereal_exists(form,field):
    cereal_name = field.data
    
    name_check = Cereal.query.filter(Cereal.name == cereal_name).first()
    
    if name_check:
        raise ValidationError("Cereal name has been taken")

class CerealForm(FlaskForm):
    name= TextAreaField("name",validators=[DataRequired(),cereal_exists])
    mfr= TextAreaField("mfr",validators=[DataRequired()])
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
    cup= DecimalField("cup",validators=[DataRequired()])
    rating= DecimalField("rating",validators=[DataRequired()])
    
