from datetime import date
from .db import db

class Cereal(db.Model):
    __tablename__ ="cereals"
    
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(),nullable=False,unique=True)
    mfr = db.Column(db.String(1),nullable=False)
    isCold = db.Column(db.Boolean())
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    sodium = db.Column(db.Integer)
    fiber = db.Column(db.Integer)
    carbo = db.Column(db.Integer)
    sugars = db.Column(db.Integer)
    potass = db.Column(db.Integer)
    vitamins = db.Column(db.Integer)
    shelf = db.Column(db.Integer)
    weight = db.Column(db.Numeric(10,2))
    cup = db.Column(db.Numeric(10,2))
    rating = db.Column(db.Numeric(10,2))