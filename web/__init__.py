from flask import Flask, render_template, request, redirect, url_for
import random
import json
app = Flask(__name__)


attribute_names = ["Strength", "Constitution", "Agility", "Awareness", "Bravery", "Charisma"]
skill_attributes = {
    'Alchemy': 6,
    'Bartering': 'Charisma',
    'Blunt Weapons': 'Strength',
    'Bows': 'Agility',
    'Books & Science': 6,
    'Brawl': 'Strength',
    'Building': 6,
    'Climbing & Jumping': 'Agility',
    'Crafts': 6,
    'Cursed Lands': 6,
    'Dodge': 'Agility',
    'Gambling': 'Awareness',
    'Healing': 'Awareness',
    'Heraldry': 6,
    'Herbs & Poisons': 6,
    'History': 6,
    'Hunting': 'Awareness',
    'Insight': 'Awareness',
    'Intimidation': 'Bravery',
    'Knives': 'Agility',
    'Languages': 6,
    'Leadership': 'Bravery',
    'Lock picking': 6,
    'Lore & Legends': 6,
    'Management': 'Awareness',
    'Occult': 6,
    'Performing': 'Charisma',
    'Poetry': 'Charisma',
    'Reading': 6,
    'Religion': 6,
    'Riding': 'Agility',
    'Sailing': 6,
    'Scheming': 'Awareness',
    'Seduction': 'Charisma',
    'Shields': 'Strength',
    'Singing & Playing': 'Charisma',
    'Sleight of Hand': 6,
    'Sneak': 'Agility',
    'Spears': 'Agility',
    'Streetwise': 'Awareness',
    'Survival': 'Awareness',
    'Swimming': 'Strength',
    'Swords': 'Strength',
    'Tactics': 'Awareness',
    'Throwing': 'Agility',
    'Trade Routes': 6
}
equipment_prices={
    "Barge": {"Weight":"10000","Price":900000},
    "Sail Boat": {"Weight":"5000","Price":120000},
    "War Galleon": {"Weight":"40000","Price":18000000},
    "Longboat": {"Weight":"2000","Price":60000},
    "Wagon": {"Weight":"4000","Price":140000},
    "Chariot": {"Weight":"1400","Price":400000},
    "Donkey": {"Weight":"-","Price":1500},
    "Ox": {"Weight":"-","Price":10000},
    "Bloodhound": {"Weight":"-","Price":30000},
    "Pony": {"Weight":"-","Price":4500},
    "Riding Horse": {"Weight":"-","Price":70000},
    "Warhorse": {"Weight":"-","Price":150000},
    "Workhorse": {"Weight":"-","Price":50000},
    "Oar": {"Weight":"70","Price":800},
    "Alchemist Kit": {"Weight":"250","Price":200000},
    "Portable Alchemist Kit": {"Weight":"100","Price":100000,"Special":"Contains: heating lamp, 1 bottle of oil, 2x beakers, sealing wax, flint & tinder, measuring weights, small00ale, parchment, 10 wooden sticks, 4 glass bottles, small chest."},
    "Alchemy Bag - Small": {"Weight":"5","Price":300,"Special":"Bag made to carry 8 vials, waterproof."},
    "Alchemy Bag - Large":{"Weight":"10","Price":600,"Special":"Bag made to carry 16 vials, waterproof."},
    "Armored Alchemy Bag":{"Weight":"10","Price":800,"Special":"Bag made to carry 12 vials, armored 6, waterproof."},
    "Beaker": {"Weight":"2","Price":500},
    "Blanket": {"Weight":"15","Price":100},
    "Canteen/Water skin": {"Weight":"4","Price":300,"Special":"Satisfies thirst for 1 day when filled."},
    "Map Case": {"Weight":"3","Price":400,"Special":"Can carry: 30"},
    "Spyglass": {"Weight":"5","Price":100000},
    "Small Chest": {"Weight":"50","Price":10000,"Special":"Can carry: 150"},
    "Large Chest": {"Weight":"130","Price":20000,"Special":"Can carry: 250"},
    "Compass": {"Weight":"5","Price":2500},
    "Lamp, Candle": {"Weight":"5","Price":300},
    "Candles (12)": {"Weight":"10","Price":2},
    "Rope, Hemp, 10 m": {"Weight":"25","Price":400},
    "Keg, Medium": {"Weight":"90","Price":10000,"Special":"Can carry: 550 waterproof"},
    "Keg, Small": {"Weight":"60","Price":800,"Special":"Can carry: 350 waterproof"},
    "Sleeping Bag": {"Weight":"20","Price":300,"Special":"Can carry: 200"},
    "Paddle": {"Weight":"40","Price":200},
    "Pickaxe": {"Weight":"150","Price":500},
    "Shovel": {"Weight":"200","Price":500},
    "Fishing Net": {"Weight":"30","Price":800},
    "Fishing Rod": {"Weight":"80","Price":500},
    "Fishing Tackle": {"Weight":"10","Price":200},
    "Grappling Hook": {"Weight":"100","Price":10000},
    "Hammer": {"Weight":"50","Price":500},
    "Hunting Trap": {"Weight":"50","Price":20000},
    "Lock": {"Weight":"20","Price":100000},
    "Manacles": {"Weight":"80","Price":150000},
    "Metal File": {"Weight":"100","Price":20000},
    "Mirror, Small Steel": {"Weight":"30","Price":100000},
    "Mirror, Small Silvered": {"Weight":"30","Price":250000},
    "Mirror, Large Steel": {"Weight":"100","Price":500000},
    "Mirror, Large Silvered": {"Weight":"100","Price":1000000},
    "Piton": {"Weight":"10","Price":5},
    "Rations, Trail (1 day)": {"Weight":"20","Price":5,"Special":"Satisfies hunger for 1 day."},
    "Tent, Large": {"Weight":"200","Price":100000,"Special":"Can accommodate 4 people."},
    "Tent, Small": {"Weight":"80","Price":50000,"Special":"Can accommodate 2 people."},
    "Thieves' Tools": {"Weight":"100","Price":250000},
    "Torch": {"Weight":"20","Price":1},
    "Waterskin": {"Weight":"20","Price":100,"Special":"Satisfies thirst for 1 day when filled."},
    "Whetstone": {"Weight":"10","Price":200}
}
class PraedorCharacter:
    def __init__(self, name, role, archetype, idea):
        self.name = name
        self.role = role
        self.archetype = archetype
        self.idea = idea
        self.attributes = self.roll_attributes()
        self.skills = {}
        self.wealth = 0
        self.background = self.roll_background()
        self.advantages = []
        self.disadvantages = []
        self.equipment = []

    def roll_attributes(self):
        attribute_values = []
        for i in range(6):
            rolls = [random.randint(1, 6) for _ in range(3)]
            attribute_values.append(sum(sorted(rolls)[1:]))
        return dict(zip(attribute_names, attribute_values))

    def roll_background(self):
        region_roll = random.randint(1, 6)
        if region_roll == 1 or region_roll == 2:
            background_roll = random.randint(11, 66)
            if background_roll >= 11 and background_roll <= 22:
                return "Holrus"
            elif background_roll >= 23 and background_roll <= 25:
                return "Sunia"
            elif background_roll >= 26 and background_roll <= 32:
                return "Justia"
            elif background_roll >= 33 and background_roll <= 35:
                return "Tutus"
            elif background_roll >= 36 and background_roll <= 43:
                return "Galth"
            elif background_roll >= 44 and background_roll <= 54:
                return "Piperia"
            elif background_roll >= 55 and background_roll <= 66:
                return "Farrignia"
        elif region_roll == 3:
            return "Western Jaconia"
        elif region_roll == 4:
            return "Southern Jaconia"
        elif region_roll == 5:
            return "Eastern Jaconia"
        else:
            return "Barbarian"

    def buy_skills(self):
        for skill, attribute in skill_attributes.items():
            if(attribute!=6):
                self.skills[skill] = self.attributes[attribute] + \
                    random.randint(1, 6)
            else:
                self.skills[skill] = 6 + \
                    random.randint(1, 6)
    def buy_equipment(self):
        self.wealth = self.starting_wealth()
        self.wealth -= 100  # basic 100 silver pieces
        self.equipment.append("Clothes")
        self.equipment.append("Rucksack")
        for item, cost in equipment_prices.items():
            if cost["Price"] <= self.wealth:
                self.equipment.append(item)
                self.wealth -= cost

    def starting_wealth(self):
        if self.background == "Noble":
            return 2000
        elif self.background == "Knight":
            return 1000
        elif self.background == "Priest":
            return 500
        elif self.background == "Patrician":
            return 500
        elif self.background == "Burgher":
            return 100
        elif self.background == "Peasant":
            return 50
        elif self.background == "Vagabond":
            return 50
        else:
            return 50


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new_character")
def new_character():
    return render_template("new_character.html")


@app.route("/create_character", methods=["POST"])
def create_character():
    name = request.form["name"]
    role = request.form["role"]
    archetype = request.form["archetype"]
    idea = request.form["idea"]
    character = PraedorCharacter(name, role, archetype, idea)
    character.buy_skills()
    character.buy_equipment()
    print(json.dumps(character.__dict__))
    return render_template("character_sheet.html", character=character)


@app.route("/character_sheet")
def character_sheet():
    character = request.args.get("character")
   # return render_template("character_sheet.html", character=character)
    return render_template("new_character.html")


