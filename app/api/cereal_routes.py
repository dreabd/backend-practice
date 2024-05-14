from flask import Blueprint, jsonify, session, request
from app.models import db,Cereal

cereal_routes = Blueprint("cereal", __name__)

#---------- GET ALL CEREALS ----------
@cereal_routes.route("/")
def get_all_cereals():
    cereals = Cereal.query.all()
    response = [cereal.all_dict() for cereal in cereals]
    
    return response


@cereal_routes.route("/<int:id>")
def get_single_cereal(id):
    cereals = Cereal.query.get(id)
    if cereals is None:
        return {"error": "Cereal Not Found"},404
    response = cereals.to_dict()
    
    return response


