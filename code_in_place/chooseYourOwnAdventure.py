import random
import time
import os

DEBUG = True #change to false once in production

MAIN_DIALOG = os.path.join(os.path.dirname(__file__),'speech/dialog.txt')
COMBAT_DIALOG = os.path.join(os.path.dirname(__file__),'speech/combat.txt')
HELP_DIALOG = os.path.join(os.path.dirname(__file__),'help.txt')
#NPC text
GOBLIN_DIALOG = os.path.join(os.path.dirname(__file__), "speech/goblin.txt")
ORC_DIALOG = os.path.join(os.path.dirname(__file__), "speech/orc.txt")
BANDIT_DIALOG = os.path.join(os.path.dirname(__file__), "speech/bandit.txt")
ELF_DIALOG = os.path.join(os.path.dirname(__file__), "speech/elf.txt")
OGRE_DIALOG = os.path.join(os.path.dirname(__file__), "speech/ogre.txt")
DRAGON_DIALOG = os.path.join(os.path.dirname(__file__), "speech/dragon.txt")
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
    }
}

#main function
def main():
    
    dialog_selection(1, 4, PATH_0)
    choose_weapon()
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
                    return "talk"                    
                case "goblin":
                    player_score += 5
                    dialog_selection(15,22,GOBLIN_DIALOG)
                    add_equipment_and_stats("ruby ring",accessories)
                    print("The goblin gives you a 'Ruby ring'")
                    #dialog_selection(1,9,PATH_1) #REVISION NEEDED
                    return "talk"
                case "orc":
                    player_score += 5
                    dialog_selection(9,15,ORC_DIALOG)
                    return "talk"
                case "elf":
                    player_score += 5
                    dialog_selection(18,22,ELF_DIALOG)
                    return "talk"
                case "ogre":
                    player_score += 5
                    dialog_selection(18,22,OGRE_DIALOG)
                    return "talk"
                case "dragon":
                    player_score += 5
                    dialog_selection(23,27,DRAGON_DIALOG)
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

    player_stats = player['stats']
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
                        elif decision_result == "sneak":
                            print("After you sneak past")
                            sneak_decision += 1
                        dialog_selection(1, 8, PATH_1)
                        choice = "" #resets choice
                        choice = input(selection_msg).lower()
                    case 1: #path 2
                        dialog_selection(10, 15, PATH_1)
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
                        dialog_selection(1, 8, PATH_1)
                        choice = "" #resets choice
                        choice = input(selection_msg).lower()
                        
                    case 2:
                        pass
                    case 3:
                        pass
                
            case "right":
                match num_selection:
                    case 0:
                        #randomly select an accessory 
                        accessory_selection = random.choice(list(accessories.keys()))
                        add_equipment_and_stats(accessory_selection,accessories)
                        decision_result = "sneak" #as this is a non-com and no interaction, default to 'sneak'
                        num_selection = 1 #to allow progression to the next level
                        sneak_decision += 1
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
                        num_selection = 1 #to allow progression to the next level
                        sneak_decision += 1
                        dialog_selection(26, 31, PATH_0)
                        choice = ""
                        dialog_selection(1, 8, PATH_2)
                        choice = input(selection_msg).lower()
                    case 2:
                        pass
                    case 3:
                        pass
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

def end_game():
    pass

if __name__ == "__main__":
    main()