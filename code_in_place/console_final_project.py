import random
import time
import os


MAIN_DIALOG = os.path.join(os.path.dirname(__file__),'speech/dialog.txt')
BANDIT_SPEACH = os.path.join(os.path.dirname(__file__), "speech/bandit_speech.txt")
GOBLIN_SPEACH = os.path.join(os.path.dirname(__file__), "speech/goblin_speech.txt")
ORC_SPEACH = os.path.join(os.path.dirname(__file__), "speech/orc_speech.txt")
ELF_SPEACH = os.path.join(os.path.dirname(__file__), "speech/elf_speech.txt")
DRAGON_SPEACH = os.path.join(os.path.dirname(__file__), "speech/dragon_speech.txt")

TEXT_SPEED = 0.1


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

accessories = {
    "gold ring": {
        "speed": 1,
        "score": 3
    },
    "gold necklace": {
        "defense": 1,
        "score": 3
    },
    "sliver ring": {
        "speed": 2,
        "score": 1
    },
    "sliver necklace": {
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
    }
}

#main function
def main():
    
    dialog_selection(0, 4, MAIN_DIALOG)
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
    selection = input(":").lower()

    match selection:
        case "knife":
            add_eqipment("knife", weapons)
        case "sword":
            add_eqipment("sword", weapons)
        case "axe":
            add_eqipment("axe", weapons)
        case "hammer":
            add_eqipment("hammer", weapons)
        case TypeError:
            print(error_msg)
            choose_weapon()

    print("You've chosen {}, may it do you well on this quest. This weapon gives you the following stats {}".format(selection, weapons[selection]))
    add_stats(weapons, selection)

    #print(player)    
    
    return(selection)

#adds item to players equipment
def add_eqipment(choice, _dict):
    temp_choice = choice
    for key, val in dict.items(_dict):
        if key == temp_choice:
            player["equipment"][key] = val

def fate_select_enemy(enemy):
    #give options to select when encounter an enemy
    print("Sneak? Talk? Attack?")
    p_select = input(": ").lower()

    match p_select:
        case "sneak":
            if player["stats"]["speed"] > enemies[enemy]["speed"]: #compare player speed with enemy speed
            #if player speed is greater than enemy speed = you get away unscathed
                player["stats"]["score"] += 1
                print("you have succeeded in sneaking away")
                
        #else enemy attacks and you take damage
            else:
                print("You lost")
        case "talk":
            match enemy:
                case "bandit":
                    pass
                case "goblin":
                    pass
                case "orc":
                    pass
                case "elf":
                    pass
                case "dragon":
                    pass
        case "attack":
            result = combat_cycle(enemy)
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

    game_over = False


    dialog_selection(4, 10, MAIN_DIALOG)
    choice = input(": ").lower()

    while game_over == False:
           
        match choice:
            case "left":
                match num_selection:
                    case 0: #the beginning
                        dialog_selection(11, 20, MAIN_DIALOG)
                        decision_result = fate_select_enemy("goblin")
                    case 1: #blood on your hands
                        print("blood on your hands")
                        pass
                    case 2: #sparing the enemy
                        print("sparing the enemy")
                        pass
                    case 3: #supply chain
                        print("supply chain")
                        pass
            case "right":
                match num_selection:
                    case 0:
                        armor_selection = random.choice(list(armor.keys())) #randomly select a piece of armor
                        add_eqipment(armor_selection, armor)
                        add_stats(armor, armor_selection)
                        print("Congragulations, you found {}, which gives you the following stats {}".format(armor_selection.upper(), armor[armor_selection]))
                        num_selection = 2
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
            case TypeError:
                print(error_msg)
                print("Left? or Right?")
                fate_select()
        
        if decision_result == "combat":
            if num_selection == 0:
                num_selection = 1
        if decision_result == 'death':
            game_over = True

    #gives the player a choice

#adds the stats of the item on the player
def add_stats(i_dict, equipped):
    #add stats that match to player stats from equipment
    #bring in equipment stats
    for key, val in i_dict.items():
        for x, y in val.items():
            if key == equipped:
                player["stats"][x] += y #add the stat to the corrisponding state the item has
   

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
                    return 'death'
                    break
                if enemy_health <= 0:
                    match enemy:
                        case "goblin":
                            print("After defeating the goblin, you find a sliver necklace on the corpse and add it to your equipment")
                            add_eqipment("sliver ring", accessories)
                            add_stats(accessories, "silver ring")
                            return 'combat'
                        case "bandit":
                            return 'combat'
                        case "orc":
                            return 'combat'
                        case "elf":
                            return 'combat'
                        case "dragon":
                            pass
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


if __name__ == "__main__":
    main()