import random
from Headers.Handlers.level_handler import *
from Headers.tools import *

def create(pokemon, to_next_level, stored_pokemon, level, name, nickname):
    copy = stored_pokemon[0].copy() # make a copy of the first stored pokemon
    for key in copy.keys(): # for key in copy
        copy[key] = int(0) # default every value to 0

    copy['ID'] = len(stored_pokemon) # store id

    pid = get_pid(pokemon, name)
    if pid == -1: # if could not find name in pokemon
        print("ERROR: Could not find",name,"in pokemon.")
        exit()
    copy['Pid'] = pid # pid
    copy['Tid'] = -1 # tid
    copy['Name'] = nickname # name
    copy['Status'] = ""
    
    moves = pokemon[pid]['Learnable Moves'].split(',') # set moves to list of possible moves
    res = ""
    if level < 3:
        num = 2
    elif level < 7:
        num = 3
    else:
        num = 4

    i = 0
    while i < num: # get random moves from list of options
        res += str(random.choice(moves))
        if i < num - 1:
            res += ","
        i += 1

    copy['Moves'] = res # store result
    copy['HP IV'] = random.randrange(1,32)
    copy['Defense IV'] = random.randrange(1,32)
    copy['SP Attack IV'] = random.randrange(1,32)
    copy['SP Defense IV'] = random.randrange(1,32)
    copy['Speed IV'] = random.randrange(1,32)
    
    i = 0
    while i < level:
        level_up(copy, pokemon[pid], to_next_level, False, False)
        i += 1

    copy['Curr HP'] = copy['HP']

    stored_pokemon.append(copy)

def get_pid(pokemon, name):

    i = 0
    for p in pokemon:
        try:
            if p['Name'] == name:
                return i
        except:
            pass
        i += 1

    return -1

def get_level(): # get level that user wants to make pokemon at
    subheader("Level")
    option(0, "Create random-leveled pokemon")
    option(1, "Create pokemon with level in given range")
    option(2, "Create pokemon with specified level")
    option(3, "Cancel")
    inp = input("--> ")

    try: # try turning inp into an integer
        inp = int(inp)
    except:
        inp = -1

    level = 1 # default level to 1
    if inp == 0: # Random-leveled
        level = random.randrange(1,99)
        
    elif inp == 1:
        range1 = input("From level: ")
        range2 = input("To level: ")

        try: # try turning inputs into integers
            range1 = int(range1)
            range2 = int(range2)
        except:
            print("ERROR: One or more of the inputs was not an integer")
            return -1

        if range1 < 1 or range1 >= range2 or range2 > 99: # out of range
            print("ERROR: One or more of the inputs was out of range")
            return -1

        if inp != 3: # if there were no errors
            level = random.randrange(range1, range2)

    elif inp == 2:
        level = input("Level: ")

        try: # check if given level is an integer
            level = int(level)
        except:
            print("ERROR:",level,"is not an integer")
            return -1
        
    elif inp == 3: # Cancel
        return -1

    else: # Out of range
        print("ERROR:",inp,"was not an option or the input wasn't an integer")
        return -1

    return level

def get_pokemon_name(pokemon):
    subheader("Pokemon Name")
    option(0, "Choose random Pokemon by biome")
    option(1, "Choose random Pokemon")
    option(2, "Specify Pokemon")
    option(3, "Cancel")
    inp = input("--> ")

    try: # check if inp is an integer
        inp = int(inp)
    except:
        print("ERROR:",inp,"is not an integer")
        return -1

    if inp == 0: # By biome
        print("Not configured yet")
        return -1

    elif inp == 1: # Random Pokemon
        return pokemon[random.randrange(1, len(pokemon) - 1)]['Name']

    elif inp == 2: # Specified name
        name = input("Name of Pokemon: ")

        pid = get_pid(pokemon, name) # try to find pokemon by name
        if pid == -1: # if not found
            print("ERROR:",name,"not found in Pokemon")
            return -1
        else:
            return name

    elif inp == 3: # Cancel
        return -1

    else: # Out of range
        print("ERROR:",inp,"was not an option or the input was not an integer")
        return -1

def get_pokemon_nickname():
    subheader("Nickname")
    option(0, "No nickname")
    option(1, "Set nickname")
    inp = input("--> ")

    try: # see if inp is an integer
        inp = int(inp)
    except:
        inp = -1

    if inp == 0:
        return ""

    elif inp == 1:
        nickname = input("Nickname: ")
        return nickname

    else:
        print("ERROR:",inp,"was not an option or the input was not an integer")
        return -1