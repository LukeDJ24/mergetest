from items import *
from enemy import * 
room_home = {
    "name": "Home",

    "description":
    """You reside by your small home town, everything seems familiar, apart from one thing.
There is a notice on the billboard that outlines:

The Ancient Cinncinati Legend has rampaged the area north of the castle and may
have had his goons also take the princess in castle, he must be stopped.
a plentiful sum will be offered.

Kirill the Wisest.""",

    "exits": {"west": "General Store", "east": "Bar"},

    "items": [],

    "market": [],

    "combat": False, 
    
    "enemy": [],

    "max enemy": 0,

    "min enemy": 0,

    "check_item": [] 
}

room_bar = {
    "name": "Bar",

    "description":
    """It's a bar""",

    "exits": {"north": "Camp", "west": "Home"},

    "items": [],

    "market": [],

    "combat": False,

    "enemy": [],

    "max enemy": 0,

    "min enemy": 0,

    "check_item": [] 
    }

room_shop = {
    "name": "General Store",

    "description":
    """As you walk in, you hear the ting of the bell go off, you're in your local
store, it sells everything a regular person would need. The shopkeep grumbles and
raises his brow at you. "What you want?" """,

    "exits": {"north": "Bridge", "east": "Home"},

    "items": [],
    
    "market": [item_upg_sword, item_axe, item_chainmail, item_potion, item_clairvoyence],

    "combat": False,

    "enemy": [],

    "max enemy": 0,

    "min enemy": 0,

    "check_item": []  
    }

room_bridge = {
        "name": "Bridge",

        "description":
        """You come across a path, with beaten roads and snapped branches. You notice that
the bridge connecting you to the castle as been blocked, by a multitude of wood panes, they
don't look like too much of an issue to get rid of, with the right tools at least.""",

        "exits": {"south": "General Store", "north": "Castle"},

        "items": [],

        "market": [],

        "combat": True,

        "enemy": [enemy_kobold, enemy_bandit],

        "max enemy": 2,

        "min enemy": 1,

        "check_item": item_wood_block,

        "enemy_present": [] 

}
room_castle = {
        "name": "Castle",

        "description":
        """As you enter the castle, you can see a set pf armour scattered across the floor, chipped stone
on the walls and bloody arrows everywhere. There's clearly been a battle here.""",

        "exits": {"south": "Bridge", "north": "Cinncinati Zoo"},

        "items": [item_princess],

        "market": [],

        "combat": True,

        "enemy": [enemy_bandit, enemy_rufian, enemy_rogue_knight, enemy_castle_mage],

        "max enemy": 4,

        "min enemy": 3,

        "check_item": [],

        "enemy_present": []

        }

room_zoo = {
        "name": "Cinncinati Zoo",

        "description":
        """You've entered the entrance to the Zoo, you can sense your close to the source of the peril that
has purged your lands. All of the signs have been bent, written over and there seems to be recurring phrase
amongst the graffiti: "Dicks Out!". What this means is unknown to you.""",

        "exits": {"south": "Castle", "north": "Harambe's Pen"},

        "items": [],

        "market": [],

        "combat": True,

        "enemy": [enemy_kobold],

        "max enemy": 1,

        "min enemy": 1,

        "check_item": [],

        "enemy_present": [] 

        }

room_harambe = {
        "name": "Harambe's Pen",

        "description":
        """As you enter you can hear the snorts coming from who is known as Harambe. He sits in wait for challengers
on his thrown, the anarchy of the situation is clear, with blood and corpsers of previous challengers laiden on the ground.
There are cages to the left and right of him, with children caged up inside. It is no fake warlord you are fighting here.""",

        "exits": {},

        "items": [],

        "market": [],

        "combat": True,

        "enemy": [enemy_kobold, enemy_bandit],

        "max enemy": 3,

        "min enemy": 1,

        "check_item": [],

        "enemy_present": []  
}

room_forest = {
        "name": "Forest",

        "description":
        """This forest has a weird tinge to it, mist covers the ground, the trees bare no leaves
there is no life here. It feels cold and eary, once inside, escaping will be difficult.""",

        "exits": {"south": "Home", "east": "Camp"},

        "items": [item_wood_block],

        "market": [],

        "combat": True,

        "enemy": [enemy_kobold, enemy_test],

        "max enemy": 3,

        "min enemy": 2,

        "check_item": item_axe,

        "enemy_present": []

    }

room_camp = {
        "name": "Camp",

        "description":
        """The camp has been burnt to a crisp but you can still spot remnants of salvagable gear. Along with
some shady members.""",

        "exits": {"west": "Clearing", "north": "Clearing2", "south": "Bar"},

        "items": [],

        "market": [],

        "combat": True,

        "enemy": [enemy_bandit, enemy_kobold, enemy_rufian, enemy_test],

        "max enemy": 5,

        "min enemy": 2,

        "check_item": [],

        "enemy_present": []
}
room_clearing_two = {
        "name": "Clearing2",

        "description":
        """clearing""",

        "exits": {"south": "Camp"},

        "items": [],

        "market":[],

        "combat": False,

        "enemy": [],

        "max enemy": 0,

        "min enemy": 0,

        "check_item": item_princess 
}
room_clearing = {
        "name": "Clearing",

        "description":
        """ clearing""",

        "exits": {"west": "Forest", "east": "Camp"},

        "items": [],

        "market": [],

        "combat": False,

        "enemy": [],

        "max enemy": 0,

        "min enemy": 0,

        "check_item": [] 
}
rooms = {
        "Home": room_home,
        "Bar": room_bar,
        "General Store": room_shop,
        "Bridge": room_bridge,
        "Castle": room_castle,
        "Cinncinati Zoo": room_zoo,
        "Harambe's Pen": room_harambe,
        "Forest": room_forest,
        "Camp": room_camp,
        "Clearing": room_clearing,
        "Clearing2": room_clearing_two
}


    
        
        
