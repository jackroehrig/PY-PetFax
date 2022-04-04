# config
from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix='/pets')

# index route
@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

# show route
@bp.route('/<index>')
def showPet(index):
    pet = {}
    for currentPet in pets:
        if currentPet['pet_id'] == int(index):
            pet = currentPet

    # print(pet)
    return render_template('pet.html', pet=pet)
