import random
import time
import os

DEBUG = False #change to false once in production

ENDING_DIALOG = os.path.join(os.path.dirname(__file__), "path/ending.txt")
HELP_DIALOG = os.path.join(os.path.dirname(__file__),'help.txt')
#NPC text
GOBLIN_DIALOG = os.path.join(os.path.dirname(__file__), "speech/goblin.txt")
ORC_DIALOG = os.path.join(os.path.dirname(__file__), "speech/orc.txt")
BANDIT_DIALOG = os.path.join(os.path.dirname(__file__), "speech/bandit.txt")
ELF_DIALOG = os.path.join(os.path.dirname(__file__), "speech/elf.txt")
OGRE_DIALOG = os.path.join(os.path.dirname(__file__), "speech/ogre.txt")
DRAGON_DIALOG = os.path.join(os.path.dirname(__file__), "speech/dragon.txt")
DEMON_DIALOG = os.path.join(os.path.dirname(__file__), "speech/demon.txt")
#PATH DIALOG
PATH_0 = os.path.join(os.path.dirname(__file__), "path/path_0.txt")
PATH_1 = os.path.join(os.path.dirname(__file__), "path/path_1.txt")
PATH_2 = os.path.join(os.path.dirname(__file__), "path/path_2.txt")
PATH_3 = os.path.join(os.path.dirname(__file__), "path/path_3.txt")


TEXT_SPEED = 0.1

#ending decision
combat_decision = 0
sneak_decision = 0
talk_decision = 0

error_msg = "You did not choose the right selection! "
selection_msg = "Left? Right? Help? "

#dictionary's
#default, uncomment once in production
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
        "score":2
    },
    "goblin":{
        "power":2,
        "health":6,
        "speed":7,
        "score":1
    },
    "orc":{
        "power":10,
        "health":15,
        "speed":4,
        "score":3
    },
    "elf":{
        "power":4,
        "health":8,
        "speed":15,
        "score":4
    },
    "ogre":{
        "power":18,
        "health":25,
        "speed":3,
        "score":10
    },
    "dragon":{
        "power":30,
        "health":100,
        "speed":2,
        "score":20
    },
    "demon":{
        "power":30,
        "health":100,
        "speed":2,
        "score":20
    }
}

weapons = {
    "knife": {
        "speed":4,
        "power":1,
        "score": 1
        },
    "sword":{
        "speed":3,
        "power":2,
        "score": 1
        },
    "axe":{
        "speed":2,
        "power":3,
        "score": 1
        },
    "hammer": {
        "speed":1,
        "power":4,
        "score": 1
        },
}
magic_weapons = {
    "magic axe":{
        "speed":10,
        "power":30,
        "score":25
        },
}

armor = {
    "cloth": {
        "defense": 1,
        "speed": 4,
        "score": 1
    },
    "leather": {
        "defense": 3,
        "speed": 2,
        "score": 1
    },
    "chainmail": {
        "defense": 5,
        "speed": -2,
        "score": 1
    },
    "plate": {
        "defense": 15,
        "speed": -7,
        "score": 1
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
        "score": 25
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
        "speed": 4,
        "score": 8
    },
    "ruby necklace": {
        "defense": 2,
        "speed": 4,
        "score": 13
    },
    "steel grieves": {
        "defense": 10,
        "score": 5
    },
    "steel bracers": {
        "defense":10,
        "speed": -1,
        "score": 5
    }
    
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
    },
    "magic nut": {
        "power": 30,
        "defense": 30,
        "speed": 30,
    }
}

#main function
def main():
    
    dialog_selection(1, 4, PATH_0)
    choose_weapon()
    choose_armor()
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
    #print("Your stats before gaining a weapon are {}".format(player["stats"]))
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
    #print("Your current stats are {}".format(player["stats"]))
    return(selection)

def choose_armor():
    armor_selection = ""

    for key in armor.keys():
        armor_selection += key.capitalize() + ": "
    print(armor_selection)

    selection = input(":").lower()

    match selection:
        case "cloth":
            add_equipment_and_stats("knife", weapons)
        case "leather":
            add_equipment_and_stats("sword", weapons)
        case "chainmail":
            add_equipment_and_stats("axe", weapons)
        case "plate":
            add_equipment_and_stats("hammer", weapons)
        case TypeError:
            print(error_msg)
            choose_weapon()

    print("You've chosen {}, may it do you well on this quest. This armor gives you the following stats {}".format(selection, armor[selection]))
    #print("Your current stats are {}".format(player["stats"]))
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
                #print("you have succeeded in sneaking away")
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
                    dialog_selection(7,11,BANDIT_DIALOG)
                    add_equipment_and_stats("magic ring",accessories)
                    print("The bandit gives you a 'Magic ring'")

                    return "talk"                    
                case "goblin":
                    player_score += 5
                    dialog_selection(15,22,GOBLIN_DIALOG)
                    add_equipment_and_stats("ruby ring",accessories)
                    print("The goblin gives you a 'Ruby ring'")

                    return "talk"
                case "orc":
                    player_score += 5
                    dialog_selection(9,15,ORC_DIALOG)
                    add_equipment_and_stats("magic axe",magic_weapons)
                    print("The orc gives you a 'magic axe'")

                    return "talk"
                case "elf":
                    player_score += 5
                    dialog_selection(10,15,ELF_DIALOG)
                    add_equipment_and_stats("magic necklace",magic_accessories)
                    print("The elf gives you a 'Magic necklace'")

                    return "talk"
                case "ogre":
                    player_score += 5
                    dialog_selection(7,15,OGRE_DIALOG)
                    add_equipment_and_stats("magic nut",magic_accessories)
                    print("The ogre gives you a 'Magic nut'")

                    return "talk"
                case "dragon":
                    player_score += 5
                    dialog_selection(23,27,DRAGON_DIALOG)
                    return "talk"
                case "demon":
                    player_score += 5
                    dialog_selection(1,15,DEMON_DIALOG)
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
    
    combat_decision = 0
    sneak_decision = 0
    talk_decision = 0
    
    enemy = ""
    enemy_dialog = ""
    start_d = 0
    end_d = 0

    player_score = player["stats"]['score']
    game_over = False


    dialog_selection(4, 10, PATH_0)
    choice = input(selection_msg).lower()

    while game_over == False:

        match choice:
            case "left":
                match num_selection:
                    case 0:
                         #goblin encounter
                        dialog_selection(0, 13, GOBLIN_DIALOG) #call enemy decision
                        decision_result = fate_select_enemy("goblin") #save result in variable
                        num_selection = 1

                        if decision_result == "combat":
                            print("After your victory")
                            combat_decision +=1
                        elif decision_result == "talk":
                            talk_decision += 1
                            
                        elif decision_result == "sneak":
                            print("After you sneak past")
                            sneak_decision += 1
                        dialog_selection(1, 8, PATH_1)
                        choice = "" #resets choice
                        choice = input(selection_msg).lower()
                    case 1: #path 2
                        dialog_selection(10, 14, PATH_1)
                        if decision_result == "combat":
                            enemy = "orc"
                            enemy_dialog = ORC_DIALOG
                            start_d = 1
                            end_d = 8
                        else:
                            enemy = "bandit"
                            enemy_dialog = BANDIT_DIALOG
                            start_d = 1
                            end_d = 8
                        num_selection = 2
                        dialog_selection(start_d, end_d, enemy_dialog)
                        decision_result = fate_select_enemy(enemy)

                        #victory points awarded
                        if decision_result == "combat":
                            print("After your victory")
                            combat_decision +=1
                        elif decision_result == "sneak":
                            print("After you sneak past")
                            sneak_decision += 1
                        dialog_selection(1, 9, PATH_2)
                        choice = "" #resets choice
                        choice = input(selection_msg).lower()
                    case 2: #blue door
                        #NEEDS TO BE ALTERED
                        #randomly select an accessory 
                        accessory_selection = random.choice(list(magic_accessories.keys()))
                        add_equipment_and_stats(accessory_selection,magic_accessories)
                        decision_result = "sneak" #as this is a non-com and no interaction, default to 'sneak'
                        num_selection = 3 #to allow progression to the next level
                        sneak_decision += 1
                        dialog_selection(10, 15, PATH_2) #left door in path_2.txt
                        choice = ""
                        dialog_selection(1, 9, PATH_3) #begining intro to path 3
                        choice = input(selection_msg).lower()
                    case 3: #white door
                        enemy = "dragon"
                        enemy_dialog = DRAGON_DIALOG
                        start_d = 1
                        end_d = 12

                        num_selection = 2
                        dialog_selection(start_d, end_d, enemy_dialog)
                        decision_result = fate_select_enemy(enemy)

                        #victory points awarded
                        if decision_result == "combat":
                            print("After your victory")
                            combat_decision +=1
                        elif decision_result == "sneak":
                            print("After you sneak past")
                            sneak_decision += 1

                        #game over decision
                        final_decision_result = calculate_win_condition(combat_decision, sneak_decision, talk_decision)
                        if final_decision_result == combat_decision:
                            dialog_selection(1,9,ENDING_DIALOG)
                            print("Your final score was {}".format(player_score))
                            dialog_selection(37,39,ENDING_DIALOG) #final thought
                            exit()
                        elif final_decision_result == talk_decision:
                            dialog_selection(10,23,ENDING_DIALOG)
                            print("Your final score was {}".format(player_score))
                            dialog_selection(37,39,ENDING_DIALOG) #final thought
                            exit()
                        elif final_decision_result == sneak_decision:
                            dialog_selection(24,36,ENDING_DIALOG)
                            print("Your final score was {}".format(player_score))
                            dialog_selection(37,39,ENDING_DIALOG) #final thought
                            exit()
                
            case "right":
                match num_selection:
                    case 0:
                        #randomly select an accessory 
                        accessory_selection = random.choice(list(accessories.keys()))
                        add_equipment_and_stats(accessory_selection,accessories)
                        decision_result = "sneak" #as this is a non-com and no interaction, default to 'sneak'
                        sneak_decision += 1
                        num_selection = 1 #to allow progression to the next level
                        
                        dialog_selection(26, 30, PATH_0)
                        print("{} that you put on.".format(accessory_selection))
                        choice = ""
                        dialog_selection(1, 8, PATH_1)
                        choice = input(selection_msg).lower()
                    case 1:
                        #randomly select an accessory 
                        accessory_selection = random.choice(list(magic_accessories.keys()))
                        add_equipment_and_stats(accessory_selection,magic_accessories)
                        decision_result = "sneak" #as this is a non-com and no interaction, default to 'sneak'
                        num_selection = 2 #to allow progression to the next level
                        sneak_decision += 1
                        dialog_selection(16, 20, PATH_1)
                        choice = ""
                        dialog_selection(1, 9, PATH_2) #opening path message
                        choice = input(selection_msg).lower()
                    case 2: #green door
                        #dialog_selection(1, 9, PATH_2)
                        if decision_result == "combat":
                            enemy = "elf"
                            enemy_dialog = ELF_DIALOG
                            start_d = 1
                            end_d = 9
                        else:
                            enemy = "ogre"
                            enemy_dialog = OGRE_DIALOG
                            start_d = 1
                            end_d = 8
                        num_selection = 3
                        dialog_selection(start_d, end_d, enemy_dialog)
                        decision_result = fate_select_enemy(enemy)

                        #victory points awarded
                        if decision_result == "combat":
                            print("After your victory")
                            combat_decision +=1
                        elif decision_result == "sneak":
                            print("After you sneak past")
                            sneak_decision += 1
                        dialog_selection(1, 13, PATH_3)
                        choice = "" #resets choice
                        choice = input(selection_msg).lower()
                    case 3: #black door     
                        enemy = "demon"
                        enemy_dialog = DEMON_DIALOG
                        start_d = 1
                        end_d = 15

                        num_selection = 2
                        dialog_selection(start_d, end_d, enemy_dialog)
                        decision_result = fate_select_enemy(enemy)

                        #victory points awarded
                        if decision_result == "combat":
                            print("After your victory")
                            combat_decision +=1
                        elif decision_result == "sneak":
                            print("After you sneak past")
                            sneak_decision += 1
                        
                        #game over decision
                        final_decision_result = calculate_win_condition(combat_decision, sneak_decision, talk_decision)
                        if final_decision_result == combat_decision:
                            dialog_selection(1,9,ENDING_DIALOG)
                            print("Your final score was {}".format(player_score))
                            dialog_selection(37,39,ENDING_DIALOG) #final thought
                            exit()
                        elif final_decision_result == talk_decision:
                            dialog_selection(10,23,ENDING_DIALOG)
                            print("Your final score was {}".format(player_score))
                            dialog_selection(37,39,ENDING_DIALOG) #final thought
                            exit()
                        elif final_decision_result == sneak_decision:
                            dialog_selection(24,36,ENDING_DIALOG)
                            print("Your final score was {}".format(player_score))
                            dialog_selection(37,39,ENDING_DIALOG) #final thought
                            exit()

            case "help":
                dialog_selection(0, 8, HELP_DIALOG)
                choice = input(selection_msg).lower()
            case "player":
                player_input = input("Stats or Equipment? ")
                if player_input == "stats":
                    for key, value in player["stats"].items():
                        print("{}: {}".format(key, value))
                    #print("Your current stats are {}".format(player["stats"]))
                    choice = input(selection_msg).lower()
                elif player_input == "equipment":
                    print("You are equipmed with:")
                    for key, value in player["equipment"].items():
                        print(key.capitalize())
                        for x, y in value.items():
                            print("   {}: {}".format(x, y))
                    #print("Your current equipment is {}".format(player["equipment"]))
                    choice = input(selection_msg).lower()
                else:
                    print("That was not a valid selection")
                    choice = input(selection_msg).lower()
            case "repeat":
                match num_selection:
                    case 0:
                        dialog_selection(4, 10, PATH_0)
                        choice = input(selection_msg).lower()
                    case 1:
                        dialog_selection(1, 9, PATH_1)
                        choice = input(selection_msg).lower()
                    case 2:
                        dialog_selection(1, 9, PATH_2)
                        choice = input(selection_msg).lower()
                    case 3:
                        dialog_selection(1, 13, PATH_3)
                        choice = input(selection_msg).lower()
            case "debug":
                if DEBUG == True:
                    debug_msg = "Path? Progression? "
                    debug_input = input(debug_msg).lower()
                    if debug_input == "path":
                        print("The current path number is {}".format(num_selection))
                        choice = input(selection_msg).lower()
                    elif debug_input == "progression":
                        print("Your combat score is {}".format(combat_decision))
                        print("Your sneak score is {}".format(sneak_decision))
                        print("Your talk score is {}".format(talk_decision))
                    else:
                        print("you have exited debug mode")
                        choice = input(selection_msg).lower()
                else: 
                    print("Please make a valid selection.")
                    choice = input(selection_msg).lower()
            case "exit":
                confirm = input("leaving so soon? Are you sure? Yes or No? ").lower()
                match confirm:
                    case 'yes':
                        print("Thank you for playing, come and play again soon")
                        break
                    case 'no':
                        print("I'm glad you decided to stay")
                        choice = input(selection_msg).lower()
            case TypeError:
                print("Please make a valid selection.")
                choice = input(selection_msg).lower()
       
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

    enemy_dmg = (temp_def + player_defense) - enemy_pwr

    player_check = ""


    while True:
        match results:
            case "attack":                
                #initial attack player hits
                enemy_health -= player_pwr #player always attacks first
                if enemy_health <= 0:
                    match enemy:
                        case "goblin":
                            add_equipment_and_stats("silver ring", accessories)
                            print("You found a silver ring on the goblin")
                            return 'combat'
                        case "bandit":
                            add_equipment_and_stats("gold ring", accessories)
                            print("You found a gold ring on the bandit")
                            return 'combat'
                        case "orc":
                            add_equipment_and_stats("magic axe", magic_weapons)
                            print("You found a magic axe on the orc")
                            return 'combat'
                        case "elf":
                            add_equipment_and_stats("magic necklace", accessories)
                            print("You found a magic necklace on the elf")
                            return 'combat'
                        case "ogre":
                            add_equipment_and_stats("magic nut", magic_accessories)
                            return 'combat'
                        case "dragon":
                            return 'combat'
                else:
                    #print(enemy_dmg)
                    if enemy_dmg <= 0:
                        #print("less than 0")
                        temp_def = 0
                        player_health -= temp_def
                        print("Your enemy the {} has done {} damage to you.".format(enemy, temp_def))
                        #player_health -= enemy_dmg
                    elif enemy_dmg > 0:
                        player_health -= enemy_dmg
                        print("Your enemy the {} has done {} damage to you.".format(enemy, enemy_dmg))
                    #print(enemy_dmg)

                    
                    print(player_health)
                    if player_health <= 0:
                        print("You died, you loose!")
                        exit()
                    else:
                        print("Your remaining health is: {}".format(player_health))
                        results = input(combat_msg).lower()
            case "defend":
                healed_for = health_restore(1, 4) #randomly heal
                if player["stats"]["health"] == player_health: #heal up to maximum health
                    print("You are already at maximum health, you cannot heal anymore.")
                else:
                    player_health += healed_for
                    print("You healed for {}".format(healed_for))
                print("Your health is now at {}".format(player_health))
                #if the damage is less than 0, set value to 0, otherwise subtract value from the players health
                if enemy_dmg <= 0:
                        temp_def = 0
                        player_health = (player_health - temp_def)
                        print("Your enemy the {} has done {} damage to you.".format(enemy, temp_def))
                elif enemy_dmg > 0:
                    player_health = (player_health - enemy_dmg)
                    print("Your enemy the {} has done {} damage to you.".format(enemy, enemy_dmg))

                
                if player_health <= 0:
                        print("You died, you loose!")
                        game_over('death')
                else:
                    results = input(combat_msg).lower()
               
            case "run":
                success = random.randint(1, 6)
                if success > 2:
                    print("You have successfully run away")
                    return "combat"
                else:
                    print("You have failed to run away and now {} has attacked".format(enemy))
                    if enemy_dmg <= 0:
                        #print("less than 0")
                        temp_def = 0
                        player_health -= temp_def
                        print("Your enemy the {} has done {} damage to you.".format(enemy, temp_def))
                        #player_health -= enemy_dmg
                    elif enemy_dmg > 0:
                        player_health -= enemy_dmg
                        print("Your enemy the {} has done {} damage to you.".format(enemy, enemy_dmg))
                    #player_health -= enemy_pwr - temp_def - player_defense
                    print("Doing {} damage to you".format((enemy_pwr - temp_def - player_defense)))
                    print("You are now down to {} health.".format(player_health))
                    if player_health <= 0:
                        print("You died, you loose!")
                        game_over('death')
                    else:
                        results = input(combat_msg).lower()
            case "help":
                dialog_selection(0, 5, HELP_DIALOG)
                dialog_selection(6, 8, HELP_DIALOG)
                results = input(selection_msg).lower()
            case "player":
                player_info_msg = "What player info did you want? Health? Defense? Power? Enemy damage(enemy)?"
                player_info = input(player_info_msg).lower()
                #enemy_dmg = enemy_pwr - temp_def - player_defense
                enemy_dmg =  (temp_def + player_defense) - enemy_pwr
                match player_info:
                    case "health":
                        print("Your current health is {}".format(player_health))
                    case "defense":
                        print("Your current health is {}".format(player_defense))
                    case "power":
                        print("Your current health is {}".format(player_pwr))
                    case "enemy":
                        print("The amount of damage this enemy will produce is {}".format(enemy_dmg))
                    case "exit":
                        results = input(combat_msg).lower()
                    case TypeError:
                        print("Please select a valid response")
                        player_info = input(player_info_msg).lower()
            case TypeError:
                print("Please select a valid response")
                results = input(combat_msg).lower()

def health_restore(start_num, end_num):
    restore = random.randint(start_num, end_num)
    return restore

def game_over(type):
    player_score = player["stats"]['score']
    match type:
        case "death":
            print("You died")
            print("Your final score was {}".format(player_score))
            exit()
        case "combat":
            print('CONGRATULATIONS, you were able to win by Combat')
            print('There may be a different way to succeed, try again?')
            print("Your final score was {}".format(player_score))
            exit()
        case "sneak":
            print("CONGRAGULATIONS, you were able to avoid everything")
            print('There may be a different way to succeed, try again?')
            print("Your final score was {}".format(player_score))
            exit()
        case "talk":
            print("CONGRAGULATIONS, you were able to avoid everything")
            print('There may be a different way to succeed, try again?')
            print("Your final score was {}".format(player_score))
            exit()

def calculate_win_condition(combat, sneak, talk):
    win_condition = [combat, sneak, talk]
    return max(win_condition)


if __name__ == "__main__":
    main()