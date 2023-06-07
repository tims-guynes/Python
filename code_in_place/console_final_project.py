import random
import time
import os

FILE_NAME = os.path.join(os.path.dirname(__file__),'dialog.txt')
TEXT_SPEED = 0.1

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
    
    dialog_selection(0, 4)
    weapon = choose_weapon()
    

    #print(player["power"])
    #print(player["speed"])
    dialog_selection(4, 9)
    fate_select()

def dialog_selection(start, end):
    dialog = clean_dialog_text()
    
    for i in dialog[start:end]:
        print(i)
        time.sleep(TEXT_SPEED)
    
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

def fate_select_enemy(enemy):
    #give options to select when encounter an enemy
    print("Sneak? Talk? Attack?")
    p_select = input(": ").lower()

    if p_select.lower() == 'sneak':
        if player["speed"] > enemies[enemy]["speed"]:
            print(player["speed"])
            print(enemies[enemy]["speed"])
            player["score"] += 1
            print("you have succeeded in sneaking away")
        #compare player speed with enemy speed
        #if player speed is greater than enemy speed = you get away unscathed
        #else enemy attacks and you take damage
        else:
            print("You lost")
        
    elif p_select.lower() == 'talk':
        pass
    elif p_select.lower() == 'attack':
        pass

    #print(p_select)

def fate_select():
    choice = input("Left? Right?: ")

    if choice.lower() == 'left':
        dialog_selection(10, 20)
        fate_select_enemy("goblin")
        pass
    elif choice.lower() == 'right':
        pass
    #gives the player a choice
    pass

def combat_cycle(enemy, player):
    #attack
    #defend
    #run
    pass

if __name__ == "__main__":
    main()