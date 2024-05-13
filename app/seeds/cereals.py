from app.models import db,Cereal,environment, SCHEMA
from sqlalchemy.sql import text
from .cereal_json import arr_of_cereal_obj

def seed_cereals():
    arr_of_cereal = arr_of_cereal_obj(100)
    cereal_list = []
    for i in range(len(arr_of_cereal)):
        cereal = Cereal(
            name=arr_of_cereal[i]["name"],
            mfr=arr_of_cereal[i]["mfr"],
            isCold=True if arr_of_cereal[i]["type"] == "C" else False,
            calories=arr_of_cereal[i]["calories"],
            protein=arr_of_cereal[i]["protein"],
            fat=arr_of_cereal[i]["fat"],
            sodium=arr_of_cereal[i]["sodium"],
            fiber=arr_of_cereal[i]["fiber"],
            carbo=arr_of_cereal[i]["carbo"],
            sugars=arr_of_cereal[i]["sugars"],
            potass=arr_of_cereal[i]["potass"],
            vitamins=arr_of_cereal[i]["vitamins"],
            shelf=arr_of_cereal[i]["shelf"],
            weight=arr_of_cereal[i]["weight"],
            cup=arr_of_cereal[i]["cups"],
            rating=arr_of_cereal[i]["rating"],
        )
        cereal_list.append(cereal)
        
    [db.session.add(cereal) for cereal in cereal_list]
    db.session.commit()
    
    


def undo_cereals():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cereals RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cereals"))
        
    db.session.commit()
    
