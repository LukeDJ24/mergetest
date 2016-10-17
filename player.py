from items import *
from map import rooms

warrior = {
    "inventory": [item_sword],
    #"gold": int(50),
    "hp": int(150),
    "temp_hp": int(150)
    }
mage = {
    "inventory": [item_fireball],
    #"gold" = int(50),
    "hp": int(80),
    "temp_hp": int(150)
    }
rogue = { 
    "inventory": [item_dagger, item_helping_hand],
    #"gold" = int(50),
    "hp": int(70),
    "temp_hp": int(70)
    } 
cleric = { 
    "inventory":[item_mace, item_restoration],
    #"gold" = int(50),
    "hp": int(80),
    "temp_hp": int(80)
    } 

current_room = rooms["Home"]
gold = int(50) 
    

