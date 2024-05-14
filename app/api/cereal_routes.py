from flask import Blueprint, jsonify, session, request
from app.models import db,Cereal
from app.forms import CerealForm

cereal_routes = Blueprint("cereal", __name__)

#---------- GET ALL CEREALS ----------
@cereal_routes.route("/")
def get_all_cereals():
    cereals = Cereal.query.all()

    if not len(cereals):
        return {"errors":"Cereals could not be found"}, 404
    
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
    
    form = CerealForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    
    if form.validate_on_submit():
        data = form.data
        new_cereal = Cereal(
            name=data["name"],
            mfr=data["mfr"],
            isCold=data["isCold"],
            calories=data["calories"],
            protein=data["protein"],
            fat=data["fat"],
            sodium=data["sodium"],
            fiber=data["fiber"],
            carbo=data["carbo"],
            sugars=data["sugars"],
            potass=data["potass"],
            vitamins=data["vitamins"],
            shelf=data["shelf"],
            weight=data["weight"],
            cup=data["cup"],
            rating=data["rating"],
        )        
        
        db.session.add(new_cereal)
        db.session.commit()
        return {"message":"success","data":new_cereal.to_dict()},200
    
    if form.errors:
       print("There were some form errors", form.errors)
       return {"errors": form.errors}, 400, {"Content-Type": "application/json"}


@cereal_routes.route("/<int:id>",methods=["DELETE"])
def delete_single_cereal(id):
    deleted_cereal = Cereal.query.get(id)
    
    if deleted_cereal is None:
        return{"errors":"Cereal could not be found"},404
    
    db.session.delete(deleted_cereal)
    db.session.commit()
    return {"message":"Cereal Successfully delelted"}

