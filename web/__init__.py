from flask import Flask, render_template, request, redirect, url_for
from web.character import PraedorCharacter
import json

app = Flask(__name__)

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
    character = PraedorCharacter()
    character.set(name, role, archetype, idea)
    character.buy_skills()
    character.buy_equipment()
    return redirect(url_for("character_sheet", character=character.to_json()),code=307)

@app.route("/character_sheet", methods=["POST"])
def character_sheet():
    thejson = request.args.get("character")
    resultDict = json.loads(thejson)
    character = PraedorCharacter()
    character.copyFromjson(resultDict)
    return render_template("character_sheet.html",character=character,thejson=thejson)
    
@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        json =uploaded_file.read()
        return redirect(url_for("character_sheet", character=json),code=307)
    return redirect("index")