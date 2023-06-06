import random
import time
import os

FILE_NAME = os.path.join(os.path.dirname(__file__),'dialog.txt')

player = {
    "power":0,
    "health":10,
    "score":0,
    "speed":5
}

enemies = {
    "bandit":{
        "power":4,
        "health":10,
        "speed":6,
        "point":2
    },
    "goblin":{
        "power":2,
        "health":5,
        "speed":7,
        "point":1
    },
    "orc":{
        "power":10,
        "health":15,
        "speed":4,
        "point":3
    },
    "elf":{
        "power":4,
        "health":8,
        "speed":15,
        "point":4
    },
    "dragon":{
        "power":30,
        "health":100,
        "speed":25,
        "point":20
    },
}

weapons = {
    "knife": {
        "speed":4,
        "power":1,
        },
    "sword":{
        "speed":3,
        "power":2,
        },
    "axe":{
        "speed":2,
        "power":3,
        },
    "hammer": {
        "speed":1,
        "power":4,
        },
}

path_chosen = [
        
    ]

def main():
    
    dialog_selection(0, 3)
    weapon = choose_weapon()

    #print(player["power"])
    #print(player["speed"])
    dialog_selection(3, 8)
    fate_select()

def dialog_selection(start, end):
    dialog = clean_dialog_text()
    
    for i in dialog[start:end]:
        print(i)
        time.sleep(1)
    
def clean_dialog_text():
    f = open(FILE_NAME) #open the file
    lines = []
    #strip out spaces for use in the dialog call
    for line in f:
        line = line.strip()
        if line != "":
            lines.append(line)
    return lines

def choose_weapon():
    weapon_selection = ""
    
    for key in weapons.keys():
        weapon_selection += key.capitalize() + ": "
    print(weapon_selection)
    selection = input(":")
    print("You've chosen {}, may it do you well on this quest".format(selection))
    player["power"] += weapons[selection]["power"]
    player["speed"] += weapons[selection]["speed"]    
    
    return(selection)

def fate_select_enemy():
    #give options to select when encounter an enemy
    print("How would you like to proceed? Sneak? Talk? Attack?")
    p_select = input(": ").lower()
    print(p_select)

def fate_select():
    choice = input(": ")
    #gives the player a choice
    pass

def combat_cycle(enemy, player):
    #player goes first
    #damage is done based on power
    #if health equals 0 player/enemy dies
    #if player dies, game over
    #if enemy dies, score increase 
    pass

if __name__ == "__main__":
    main()