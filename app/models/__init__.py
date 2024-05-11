from .db import db
from .db import environment, SCHEMA
from datetime import date

class Report(db.Model):
    __tablename__ = "reports"
    
    report_id = db.Column(db.Integer(),primary_key=True)
    created_date = db.Column(db.Date(),default=date.today())
    aec_start_date = db.Column(db.Date())
    pri_product_role = db.Column(db.String())
    brand_name = db.Column(db.String())
    ci_age = db.Column(db.Integer())
    ci_gender = db.Column(db.String())
    aec_outcome = db.Column(db.Integer())
    results = db.Column(db.String())

