import json
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2"


@app.route('/pokemon/<string:pokemon_name>')
def get_pokemon(pokemon_name):
    response = requests.get(f"{POKEAPI_BASE_URL}/pokemon/{pokemon_name.lower()}")
    
    if response.status_code == 200:
        pokemon_data = response.json()
        result = {
            "name": pokemon_data["name"],
            "weight": pokemon_data["weight"],
            "height": pokemon_data["height"],
            "types": [t["type"]["name"] for t in pokemon_data["types"]],
            "abilities": [a["ability"]["name"] for a in pokemon_data["abilities"]],
            "sprite": pokemon_data["sprites"]["front_default"],
            "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in pokemon_data["stats"]},
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Pokemon not found"}), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)