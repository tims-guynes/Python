import random
import time
import os

DEBUG = True #change to false once in production

MAIN_DIALOG = os.path.join(os.path.dirname(__file__),'speech/dialog.txt')
COMBAT_DIALOG = os.path.join(os.path.dirname(__file__),'speech/combat.txt')
GOBLIN_DIALOG = os.path.join(os.path.dirname(__file__), "speech/goblin.txt")
ORC_DIALOG = os.path.join(os.path.dirname(__file__), "speech/orc.txt")


TEXT_SPEED = 0.1

#ending decision
combat_decision = 0
sneak_decision = 0
talk_decision = 0

error_msg = "You did not choose the right selection! "

#dictionary's
player = {
    "stats": {
        "power":0,
        "health":10,
        "score":0,
        "speed":5,
        "defense": 0
    },
    "equipment": {
        
    }
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
        "health":6,
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

magic_weapons = {
    "magic axe":{
        "speed":10,
        "power":30,
        },
}
armor = {
    "cloth": {
        "defense": 1,
        "speed": 4,
    },
    "leather": {
        "defense": 3,
        "speed": 2,
    },
    "chainmail": {
        "defense": 5,
        "speed": -2,
    },
    "plate": {
        "defense": 15,
        "speed": -7,
    },
    
}

magic_armor = {
    "magic cloth": {
        "defense": 11,
        "speed": 6,
    },
    "magic leather": {
        "defense": 13,
        "speed": 4,
    },
    "magic chainmail": {
        "defense": 15,
        "speed": 2,
    },
}

accessories = {
    "gold ring": {
        "speed": 1,
        "score": 3
    },
    "gold necklace": {
        "defense": 1,
        "score": 3
    },
    "silver ring": {
        "speed": 2,
        "score": 1
    },
    "silver necklace": {
        "defense": 2,
        "score": 1
    },
    "ruby ring": {
        "power": 2,
        "score": 1
    },
    "ruby necklace": {
        "defense": 2,
        "score": 3
    },
    "steel grieves": {
        "defense": 10,
        "score": 5
    },
    
}

magic_accessories = {
    "magic grieves": {
        "health": 30,
        "score": 15
    },
    "magic earrings": {
        "health": 10,
        "score": 7
    },
    "magic necklace": {
        "health": 20,
        "score": 7
    },
    "magic ring": {
        "power": 10,
        "score": 10
    }
}

#main function
def main():
    
    dialog_selection(0, 3, MAIN_DIALOG)
    choose_weapon()
    #dialog_selection(4, 10, MAIN_DIALOG)
    fate_select()
    

def dialog_selection(start, end, file_sel):
    dialog = clean_dialog_text(file_sel)
    
    for i in dialog[start:end]:
        print(i)
        time.sleep(TEXT_SPEED)
    
def clean_dialog_text(file_sel):
    f = open(file_sel) #open the file
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

    #cycle through weapons to match and add item to equipment dictionary
    print("Your stats before gaining a weapon are {}".format(player["stats"]))
    selection = input(":").lower()

    match selection:
        case "knife":
            add_equipment_and_stats("knife", weapons)
        case "sword":
            add_equipment_and_stats("sword", weapons)
        case "axe":
            add_equipment_and_stats("axe", weapons)
        case "hammer":
            add_equipment_and_stats("hammer", weapons)
        case TypeError:
            print(error_msg)
            choose_weapon()

    print("You've chosen {}, may it do you well on this quest. This weapon gives you the following stats {}".format(selection, weapons[selection]))
    print("Your current stats are {}".format(player["stats"]))
    return(selection)


def fate_select_enemy(enemy):
    #player stats
    player_score = player["stats"]["score"]
    player_speed = player["stats"]["speed"]

    enemy_speed = enemies[enemy]["speed"] 

    print("Sneak? Talk? Combat?")
    p_select = input(": ").lower()

    #give options to select when encounter an enemy
    match p_select:
        case "sneak": 
            if player_speed > enemy_speed: #compare player speed with enemy speed
            #if player speed is greater than enemy speed = you get away unscathed
                player_score += 3
                print("you have succeeded in sneaking away")
                return "sneak"
                
        #else enemy attacks and you take damage
            else:
                print("You were noticed by the enemy, would you like to talk or fight?")
                print("Talk? Combat?")
                p_select = input(": ").lower()

        case "talk": 
            match enemy:
                case "bandit":
                    player_score += 5
                    dialog_selection(7,11,NPC_SPEACH)
                    return "talk"                    
                case "goblin":
                    player_score += 5
                    dialog_selection(15,20,GOBLIN_DIALOG)
                    return "talk"
                case "orc":
                    player_score += 5
                    dialog_selection(9,15,ORC_DIALOG)
                    return "talk"
                case "elf":
                    player_score += 5
                    dialog_selection(18,22,NPC_SPEACH)
                    return "talk"
                case "dragon":
                    player_score += 5
                    dialog_selection(23,27,NPC_SPEACH)
                    return "talk"
                
        case "combat":
            result = combat_cycle(enemy) 
            player_score += 1
            return result
        case TypeError:
            print(error_msg)
            fate_select_enemy(enemy)

    #print(p_select)

#options to select
def fate_select():
    num_selection = 0
    armor_selection = ""
    decision_result = ""
    """
    combat_decision = 0
    sneak_decision = 0
    talk_decision = 0
    """

    player_stats = player['stats']
    game_over = False


    dialog_selection(4, 10, MAIN_DIALOG)
    choice = input(": ").lower()

    while game_over == False:

        match num_selection:
            case 0:
                if choice == 'left':
                    #goblin encounter
                    #call enemy decision
                    #save result in variable
                    #pass variable through decision function and set num_selection to that number
                    
                    dialog_selection(0, 13, GOBLIN_DIALOG)
                    decision_result = fate_select_enemy("goblin")
                    #print("This is before {}".format(num_selection))
                    #dialog_selection(2, 12, COMBAT_DIALOG)
                    num_selection = path_tree(decision_result, num_selection)
                    choice = ""
                    choice = input(": ").lower()
                    #print("This is after the 'path tree' function {}".format(num_selection))
                    
                    pass
                elif choice == 'right':
                    accessory_selection = random.choice(list(accessories.keys()))
                    add_equipment_and_stats(accessory_selection,accessories)
                    decision_result = "sneak"
                    dialog_selection(25, 32, MAIN_DIALOG)
                    choice = ""
                    choice = input("Left? or Right?: ").lower()
            case 1:
                if choice == 'left':
                    #combat
                    print("This is a path test path 1")
                    test = input("press 1 for combat, press 2 for talk, press 3 for sneak")
                    if test == 1:
                        decision_result = "combat"
                    elif test == 2:
                        decision_result = "talk"
                    elif test == 3:
                        decision_result = "sneak"
                    choice = ""
                    pass
                elif choice == 'right':
                    #non-com
                    decision_result = "sneak"
                    choice = input("Left? or Right?: ").lower()
            case 2:
                if choice == 'left': #orc battle
                    dialog_selection(1, 8, ORC_DIALOG)
                    decision_result = fate_select_enemy("orc")
                    num_selection = path_tree(decision_result, num_selection)
                    print("This is after the 'path tree' function {}".format(num_selection))
                    pass
                elif choice == 'right':
                    decision_result = "sneak"
            case 3:
                if choice == 'left':
                    #combat
                    print("This is a path test, path 3")
                    test = input("press 1 for combat, press 2 for talk, press 3 for sneak")
                    if test == 1:
                        decision_result = "combat"
                    elif test == 2:
                        decision_result = "talk"
                    elif test == 3:
                        decision_result = "sneak"
                    choice = ""
                    pass
                elif choice == 'right':
                    #non-com
                    decision_result = "sneak"
                    pass
            case 4:
                if choice == 'left':
                    pass
                elif choice == 'right':
                    pass
            case 5:
                if choice == 'left':
                    pass
                elif choice == 'right':
                    pass
            case 6:
                if choice == 'left':
                    pass
                elif choice == 'right':
                    pass
            case 7:
                if choice == 'left':
                    pass
                elif choice == 'right':
                    pass
            case 8:
                if choice == 'left':
                    pass
                elif choice == 'right':
                    pass
            case 9:
                if choice == 'left':
                    pass
                elif choice == 'right':
                    pass
            case 10:
                if choice == 'left':
                    pass
                elif choice == 'right':
                    pass
       
        if decision_result == "game over":
            game_over = True

    #gives the player a choice

#adds the item to the player and it's stats
def add_equipment_and_stats(item, item_dict):
    #adds the item to the equipment list
    temp_choice = item
    for key, val in dict.items(item_dict):
        if key == temp_choice:
            player["equipment"][key] = val
    
    #adds the stats from the item to the players stats
    for key, val in item_dict.items():
        for x, y in val.items():
            if key == item:
                player["stats"][x] += y

def combat_cycle(enemy):
    
    print("You have decided to attack the {}".format(enemy))
    combat_msg = "Would you like to Attack? Defend? or Run? "
    results = input(combat_msg).lower()
    
    temp_def = 0 #placeholder for the 'defend' option

    #import player stats
    temp_player = player
    player_pwr = temp_player["stats"]['power']
    player_health = temp_player["stats"]['health']
    player_defense = temp_player["stats"]["defense"]

    #import enemy stats
    temp_enemy = enemies[enemy]
    enemy_pwr = temp_enemy['power']
    enemy_health = temp_enemy['health']

    
    match results:
        case 'attack':
            temp_result = ""
            while True:
                if temp_result == 'run' or temp_enemy["health"] <= 0: #check if option 'run' or enemies health is 0
                    break
                if temp_result == 'defend': #add extra defense when you set to defend.
                    temp_def = 1
                    player_health += 3
                if temp_result == 'attack':
                    temp_def = 0

                print("You have done {} damage to the {} you are fighting.".format(player_pwr, enemy))
                enemy_health -= player_pwr
                if player_health <= 0:
                    print("You died, you loose!")
                    game_over('death')
                    break
                if enemy_health <= 0:
                    match enemy:
                        case "goblin":
                            add_equipment_and_stats("silver ring", accessories)
                            print("You found a silver ring on the goblin")
                            dialog_selection(2, 12, COMBAT_DIALOG)
                            return 'combat'
                        case "bandit":
                            add_equipment_and_stats("gold ring", accessories)
                            print("You found a gold ring on the bandit")
                            dialog_selection(13, 19, COMBAT_DIALOG)
                            return 'combat'
                        case "orc":
                            add_equipment_and_stats("magic axe", magic_weapons)
                            print("You found a magic axe on the orc")
                            dialog_selection(20, 25, COMBAT_DIALOG)
                            return 'combat'
                        case "elf":
                            add_equipment_and_stats("magic necklace", accessories)
                            print("You found a magic necklace on the elf")
                            dialog_selection(26, 33, COMBAT_DIALOG)
                            return 'combat'
                        case "dragon":
                            dialog_selection(34, 40, COMBAT_DIALOG)
                            return 'combat'
                player_health -= enemy_pwr - temp_def - player_defense
                print("Your enemy the {} has done {} damage to you.".format(enemy, (enemy_pwr - temp_def - player_defense)))
                print("Your remaining health is: {}".format(player_health))
                temp_result = input(combat_msg).lower()

            print(temp_enemy)
            #player attacks enemy
            #subtract player power from enemy health
            #check if enemy health is 0, if greater than 0
            #enemy attacks player
            #subtract enemy power from defense, 
            # #if power < 0, result is 0 minus players health
            # #else subtract enemy power from player health
            #check to see if player health is 0, if greater than 0, start combat cycle again

            pass
        case 'defend':
            pass
        case 'run':
            print("You ran away")
        case TypeError:
            print("You have selected an invalid option, please try again!")
            combat_cycle(enemy)
    #attack
    #defend
    #run
    pass

def game_over(type):
    player_score = player["stats"]['score']
    match type:
        case 'death':
            print("You died")
            print("Your final score was {}".format(player_score))
        case 'combat':
            print('CONGRATULATIONS, you were able to win by Combat')
            print('There may be a different way to succeed, try again?')
            print("Your final score was {}".format(player_score))
        case 'sneak':
            pass
        case 'talk':
            pass

def path_tree(decision, path):
    match decision:
        case "combat":
            match path:
                #sets the path based on which path and choice made
                case 0:
                    return 2 #path 2
                case 1:
                    return 4 #path 4
                case 2:
                    return 6 #path 6 
                case 3:
                    return 8 #path 8
            
        case "sneak":
            match path:
                case 0:
                    return 1 #path 1
                case 1:
                    return 3 #path 3
                case 2:
                    return 5 #path 5
                case 3:
                    return 9 #path 9
        case "talk":
            match path:
                case 0:
                    return 4 #path 4
                case 1:
                    return 5 #path 5
                case 2:
                    return 7 #path 7
                case 3:
                    return 10 #path 10
        

def end_game():
    pass

if __name__ == "__main__":
    main()