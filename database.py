import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from model import *
import os
from dotenv import load_dotenv
from google.cloud.firestore import GeoPoint

load_dotenv()
DATABASE_KEY=os.getenv("DATABASE_KEY")
cred = credentials.Certificate(DATABASE_KEY)
app = firebase_admin.initialize_app(cred)
db = firestore.client()


def fetch_all_rooms() -> List:
    rooms = []
    docs = db.collection("rooms").stream()
    for doc in docs:
        rooms.append(doc.to_dict())
    return rooms

def fetch_one_room(room_name:str) -> dict:
    room_ref = db.collection("rooms").document(room_name)
    room = room_ref.get()
    return room.to_dict()

def create_room(room_name:str) -> dict:
    room = Room(**{"room_name":room_name})
    db.collection("rooms").document(room.room_name).set(room.to_dict())
    room_ref = db.collection("rooms").document(room.room_name)
    return room_ref.get().to_dict()


def remove_room(room_name) -> bool:
    room_ref = db.collection("rooms").document(room_name)
    players = room_ref.collection("rooms").stream()

    for player in players:
        player.delete()
    
    locations = room_ref.collection("rooms").stream()

    for location in locations:
        location.delete()
    
    room_ref.delete()

    return True
    
def create_location(room_name,latitude,longitude) -> dict:
    room_ref = db.collection("rooms").document(room_name)
    update_time,location_ref = room_ref.collection("locations").add({"location":GeoPoint(latitude,longitude)})
    return location_ref.get().to_dict()

def fetch_locations(room_name:str) -> GeoPoint:
    locations = []
    room_ref = db.collection("rooms").document(room_name)
    location_docs = room_ref.collection("locations").stream()
    for doc in location_docs:
        locations.append(doc.to_dict())
    return locations


def create_player(player,room_name) -> dict:
    room_ref = db.collection("rooms").document(room_name)
    update_time,player_ref = room_ref.collection("players").add(Player(**player).to_dict())
    room = room_ref.get().to_dict()
    player_names = room["player_names"]
    player_names.append(player["name"])
    room_ref.update({"player_names":player_names})
    return player_ref.get().to_dict()

def fetch_players(room_name:str) -> List:
    players = []
    room_ref = db.collection("rooms").document(room_name)
    player_docs = room_ref.collection("players").stream()
    for doc in player_docs:
        players.append(doc.to_dict())
    return players









    
