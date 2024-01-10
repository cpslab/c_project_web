from fastapi import FastAPI
from model import *
from database import *
from google.cloud.firestore import GeoPoint

app = FastAPI()

@app.get("/room",response_model=List)
def get_rooms():
    response = fetch_all_rooms()
    return response

@app.get("/room/{room_name}",response_model=dict)
def get_room_by_name(room_name:str):
    response = fetch_one_room(room_name)
    return response

@app.post("/room",response_model=Room)
def post_room(room_name:str):
    response = create_room(room_name)
    return response

@app.delete("/room")
def delete_room(room_name):
    response = remove_room(room_name)
    return response

@app.post("/location")
def post_location(longitude:float,latitude:float,room_name:str):
    response = create_location(room_name,latitude,longitude)
    return response

@app.get("/location/{room_name}")
def get_locations(room_name:str):
    response = fetch_locations(room_name)
    return response

@app.get("/player/{room_name}")
def get_players(room_name:str):
    response = fetch_players(room_name)
    return response

@app.post("/player",response_model=Player)
def post_player(player:Create_player,room_name:str):
    response = create_player(player.to_dict(),room_name)
    return response