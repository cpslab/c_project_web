from pydantic import BaseModel
from typing import List

class Room(BaseModel):
    room_name : str
    player_names : List = []
    def to_dict(self):
        return{
            "room_name":self.room_name,
            "player_names":self.player_names
        }

class Base_player(BaseModel):
    name:str

class Player(Base_player):
    number_of_discovery:int = 0

    def to_dict(self):
        return{
            "name":self.name,
            "number_of_discovery":self.number_of_discovery
        }

class Create_player(Base_player):

    def to_dict(self):
        return{
            "name":self.name
        }

