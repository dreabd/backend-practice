import pandas as pandas

def arr_of_cereal_obj(rows):
    cereal_arr = []
    rows = 77 if rows > 77 else rows
    df = pandas.read_csv(
        filepath_or_buffer = "/home/abad_andre/projects/backend-practice/app/cereal.csv",
        header = 0,
        nrows=  77
    )
    mfr = {
        "A":"American Home Food Products",
        "G":"General Mills",
        "K":"Kelloggs",
        "N":"Nabisco",
        "P":"Post",
        "Q":"Quaker Oats",
        "R":"Ralston Purina"
    }
    for i in range(rows):
        cereal_arr.append(
            {
                "name":df.name[i],
                "mfr":mfr[df.mfr[i]], 
                "type":df.type[i],
                "calories":df.calories[i],
                "protein":df.protein[i],
                "fat":df.fat[i],
                "sodium":df.sodium[i],
                "fiber":df.fiber[i],
                "carbo":df.carbo[i],
                "sugars":df.sugars[i],
                "potass":df.potass[i],
                "vitamins":df.vitamins[i],
                "shelf":df.shelf[i],
                "weight":df.weight[i],
                "cups":df.cups[i],
                "rating":df.rating[i],
            }
        )
        
    return cereal_arr

    
