# setting the working directory
import os
path='C:/Users/user/Desktop/HOMELAND/fastapi'
os.chdir(path)
# libraries
import fastapi
from fastapi import FastAPI,Path


app=FastAPI()
# creating the end point
# get- returning information
# post- sending information to the post
# put- update something existing
#Delete- deleting something
@app.get("/")
def home():
    return {"data":"love"}

@app.get("/about")
def hey():
    return {"data":"About"}

inventory= {
    1:{
        "name": "Charles",
        "price": 123,
        "Brand": "Brokeside"
    },
    2:{
        "Kihii": "Charles",
        "price": 123,
        "Brand": "Brokeside"
    }
}

@app.get("/get_item/{id}")
def get_item(id:int=Path(None, description=" the id of the item")):
    return inventory[id]


