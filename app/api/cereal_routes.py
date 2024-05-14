from flask import Blueprint, jsonify, session, request
from app.models import db,Cereal
from app.forms import CerealForm

cereal_routes = Blueprint("cereal", __name__)

#---------- GET ALL CEREALS ----------
@cereal_routes.route("/")
def get_all_cereals():
    cereals = Cereal.query.all()
    response = [cereal.all_dict() for cereal in cereals]
    
    return {"data": response, "message":"Success"},200


@cereal_routes.route("/<int:id>")
def get_single_cereal(id):
    cereals = Cereal.query.get(id)
    if cereals is None:
        return {"error": "Cereal Not Found"},404
    response = cereals.to_dict()
    
    return {"data": response, "message":"Success"},200

@cereal_routes.route("/",methods=["POST"])
def post_new_cereal():
    print("I am in the post cereal route")    
    
    form = CerealForm()
    
    if form.validate_on_submit():
        data = form.data
    
    if form.errors:
       print("There were some form errors", form.errors)
       return {"errors": form.errors}, 400, {"Content-Type": "application/json"}

