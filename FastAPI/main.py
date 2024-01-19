from fastapi import FastAPI
from model import *
from database import *
from google.cloud.firestore import GeoPoint
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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


@app.post("/simple/location")
def post_location(location:Location):
    response = create_simple_location(location.latitude,location.longitude)
    return response

@app.get("/simple/location")
def get_locations():
    response = fetch_simple_locations()
    return response

@app.delete("/simple/location/{id}")
def delete_simple_location(id:str):
    response = remove_simple_location(id)
    return response