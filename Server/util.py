import json
import pickle
import numpy as np
import pandas as pd

__loc=None
__data_columns=None
__model=None
def get_loc_names():
    return __loc
def get_estimated_price(location,sqft,bhk,bath):
    global __data_columns
    try:
        loc_index=__data_columns.index(location.lower())
    except: 
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >=0:
        x[loc_index]=1  

    return round(__model.predict([x])[0],2)
def load_saved_artifacts():
    print("Loading saved artifacts.....")
    global __loc
    global __data_columns
    global __model
    with open("./artifacts/columns.json","r") as f:
        __data_columns=json.load(f)["data_columns"]
        __loc=__data_columns[3:]
    with open("./artifacts/Bangalore_house_price_prediction.pickle","rb") as f:
        __model=pickle.load(f)
    print("Done")

if __name__=="__main__":
    load_saved_artifacts()
    print(get_loc_names())  
    print(get_estimated_price("Indira Nagar",1500,2,2))