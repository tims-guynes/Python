import random
import time
import os

FILE_NAME = os.path.join(os.path.dirname(__file__),'dialog.txt')
TEXT_SPEED = 0.1

error_msg = "You did not choose the right selection! "

player = {
    "power":0,
    "health":10,
    "score":0,
    "speed":5,
    "defense": 0
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
        "speed":2,
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

    dialog_selection(4, 10)
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
    match selection:
        case "knife":
            pass
        case "sword":
            pass
        case "axe":
            pass
        case "hammer":
            pass
        case TypeError:
            print(error_msg)
            selection = input(":")
    print("You've chosen {}, may it do you well on this quest".format(selection))
    player["power"] += weapons[selection]["power"]
    player["speed"] += weapons[selection]["speed"]    
    
    return(selection)

def fate_select_enemy(enemy):
    #give options to select when encounter an enemy
    print("Sneak? Talk? Attack?")
    p_select = input(": ").lower()

    match p_select:
        case "sneak":
            pass
        case "talk":
            pass
        case "attack":
            pass
        case TypeError:
            print(error_msg)
            fate_select_enemy(enemy)

    if p_select.lower() == 'sneak':
        if player["speed"] > enemies[enemy]["speed"]: #compare player speed with enemy speed
            #if player speed is greater than enemy speed = you get away unscathed
            player["score"] += 1
            print("you have succeeded in sneaking away")
                
        #else enemy attacks and you take damage
        else:
            print("You lost")
        
    elif p_select.lower() == 'talk':
        pass
    elif p_select.lower() == 'attack':
        pass

    #print(p_select)

#options to select
def fate_select():
    num_selection = 0
    choice = input(": ")
    
    match num_selection:
        case 0:
            match choice.lower():
                case "left": 
                    dialog_selection(10, 20)
                    fate_select_enemy("goblin")
                    num_selection = 1
                case "right":
                    pass
                case TypeError:
                    print(error_msg )
                    #print("Left or Right?")
                    print("Left? or Right?")
                    fate_select()
          
        case 1:
            pass

        case 2:
            pass

    #gives the player a choice

def combat_cycle(enemy, player):
    #attack
    #defend
    #run
    pass

if __name__ == "__main__":
    main()