from datetime import date
from .db import db

class Cereal(db.Model):
    __tablename__ ="cereals"
    
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(),nullable=False,unique=True)
    mfr = db.Column(db.String(1),nullable=False)
    isCold = db.Column(db.Boolean())
    calories = db.Column(db.Numeric(5,1))
    protein = db.Column(db.Numeric(5,1))
    fat = db.Column(db.Numeric(5,1))
    sodium = db.Column(db.Numeric(5,1))
    fiber = db.Column(db.Numeric(5,1))
    carbo = db.Column(db.Numeric(5,1))
    sugars = db.Column(db.Numeric(5,1))
    potass = db.Column(db.Numeric(5,1))
    vitamins = db.Column(db.Numeric(5,1))
    shelf = db.Column(db.Numeric(5,1))
    weight = db.Column(db.Numeric(10,2))
    cup = db.Column(db.Numeric(10,2))
    rating = db.Column(db.Numeric(10,2))