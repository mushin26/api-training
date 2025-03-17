#!/usr/bin/env python3
from pprint import pprint

# Pikachu dictionary
pikachu = {"name": "Pikachu", "type": "Electric", "level": 25}
pikachu["trainer"] = "Ash"

# Geodude dictionary with a list for types
geodude = {"name": "Geodude", "types": ["Rock", "Ground"], "level": 16}

# List of starter Pokémon dictionaries
starters = [
{"name": "Bulbasaur", "type": "Grass", "level": 5},
{"name": "Squirtle", "type": "Water", "level": 5},
{"name": "Charmander", "type": "Fire", "level": 5},
]

starters[0]["type"]=["Grass", "Poison"]

# Print statements
print(f"{pikachu['name']} is a level {pikachu['level']} Pokémon.")
print(f"{pikachu['name']} trainer is {pikachu['trainer']} Pokémon.")
print(f"{geodude['name']}'s first type is {geodude['types'][0]}.")
print(f"{starters[2]['name']} is a {starters[2]['type']} type starter.")
print(f"{starters[0]['name']} has a {starters[0]['type']} as new type starter.")

