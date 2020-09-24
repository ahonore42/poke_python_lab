from random import *

########################################################################################
#                 Pokemon Class
# the main class being used in this simulator

class Pokemon:
    # PART 1 ########### TO DO ###################
    # Initialize the Pokemon Class with an __init__() method
    # This class takes in 10 variable parameters in addition to self
    #
    # HINT: Take a look at some of the instances of this pokemon class below along with some of the pre-built
    # class methods to get an idea of what you might want to call these variables along with their ordering
    # to call  these parameters
    # 
    # Define a revive(???, ???): method for the Pokemon class. This will allow pokemon to revive after a battle
    # later on in the simulation
    #
    # HINT: the revive(???, ???): function takes in one other parameter besides self. To get a better idea of 
    # what the ONE other parameter is, take a look at the Save Class below
    #
    # The revive function is also one line. It starts with self.__init__() which has strictly 10 variable parameters
    # One variable parameter passed into this function is not like the others, what might it be???
    


    ################ POKEMON ATTACK METHOD ################
    # This class method allows a pokemon to make an attack from the list of its moves
    # Besides self, it takes in the parameter 'choice', which is an integer value in the range of the
    # length of its moves list
    # It will return the 3 of the dictionary values for a pokemon's move, the pokemon's
    # attacking stat depending on the 'phys_special' value, and a boolean value for whether or not
    # the move is a STAB move (Same Type Attack Boost)

    def attack(self, choice):
        # print(selection)
        strength = 0
        move = self.moves[choice]
        is_STAB = False
        if self.type1 == move['movetype']:
            is_STAB = True
        elif self.type2 == move['movetype']:
            is_STAB = True
        
        if move['phys_special'] == 'special':
            strength = self.sp_attack
        elif move['phys_special'] == 'physical':
            strength = self.ph_attack

        return move['damage'], move['movetype'], move['phys_special'], strength, is_STAB

    ############## POKEMON DAMAGE METHOD ####################
    # This class method allows for a pokemon to take damage from another pokemon's move and is fairly complex. All 
    # values and ratios within it are pokemon damage calculations according to the canon gen 7 mechanics.
    #
    # Besides self, it takes in the 5 parameters returned from another pokemon's attack() method
    # amount is the integer value for the damage of the specific move
    # movetype is the pokemon movetype associated with the move
    # phys_special is the string value for whether or not the incoming move was a physical or special move
    # strength is the integer value of the attacking pokemon's ph_attack or sp_attack stat
    # stab is the boolean value for whether or not the move made by the attacking pokemon was a STAB move
    # 
    # This method calculates the initial damage the pokemon will recieve from the initial integer values of the
    # incoming attack and the ratio of the attacking pokemon's attack stat with the current pokemon's defense stat
    #
    # After finding the initial damage, it will calculate type effectiveness bonuses, followed by STAB bonus,
    # then rnd (A random integer value between 0.85 and 1), critical hit chance / bonus, and finally will round
    # to the nearest integer value, which will then be subtracted from the pokemon's hp (Hit Points).
    #
    # Lastly, it will print out how much hp the pokemon lost and check to see if the pokemon fainted (hp went below 0)
    # by firing the faint() class method below

    def damage(self, amount, movetype, phys_special, strength, stab):
        print(f'damage: {amount}, movetype: {movetype}, phys_special: {phys_special}, attack stat: {strength}')
        

        if phys_special == 'special':
            amount = (((((2 * 100)/5) + 2) * amount * (strength / self.sp_defense) )/50) + 2
        elif phys_special == 'physical':
            amount = (((((2 * 100)/5) + 2) * amount * (strength / self.defense) )/50) + 2

        print(f'damage before type effectiveness, STAB, critical hit, and RND: {round(amount)}')

        if (movetype == 'grass' and (self.type1 in ['water', 'ground', 'rock'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'grass' and (self.type2 in ['water', 'ground', 'rock'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'grass' and (self.type1 in ['flying', 'fire', 'bug', 'poison', 'steel', 'grass', 'dragon'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'grass' and (self.type2 in ['flying', 'fire', 'bug', 'poison', 'steel', 'grass', 'dragon'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'fire' and (self.type1 in ['bug', 'grass', 'steel', 'ice'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'fire' and (self.type2 in ['bug', 'grass', 'steel', 'ice'])):
            amount *=2
            print("It's super effective!")
        if (movetype == 'fire' and (self.type1 in ['rock', 'fire', 'water', 'dragon'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'fire' and (self.type2 in ['rock', 'fire', 'water', 'dragon'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'water' and (self.type1 in ['ground','rock','fire'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'water' and (self.type2 in ['ground', 'rock', 'fire'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'water' and (self.type1 in ['water','grass','dragon'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'water' and (self.type2 in ['water','grass','dragon'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'normal' and (self.type1 in ['rock','steel'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'normal' and (self.type2 in ['rock','steel'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'normal' and (self.type1 in ['ghost'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'normal' and (self.type2 in ['ghost'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'fighting' and (self.type1 in ['normal','rock','steel','ice','dark'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'fighting' and (self.type2 in ['normal','rock','steel','ice','dark'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'fighting' and (self.type1 in ['flying','poison','bug','psychic','fairy'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'fighting' and (self.type2 in ['flying','poison','bug','psychic','fairy'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'fighting' and (self.type1 in ['ghost'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'fighting' and (self.type2 in ['ghost'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'flying' and (self.type1 in ['fighting','bug','grass'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'flying' and (self.type2 in ['fighting', 'bug', 'grass'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'flying' and (self.type1 in ['rock','steel','electric'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'flying' and (self.type2 in ['rock','steel','electric'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'poison' and (self.type1 in ['grass','fairy'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'poison' and (self.type2 in ['grass', 'fairy'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'poison' and (self.type1 in ['poison','ground','rock','ghost'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'poison' and (self.type2 in ['poison','ground','rock','ghost'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'poison' and (self.type1 in ['steel'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'poison' and (self.type2 in ['steel'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'ground' and (self.type1 in ['poison','rock','steel','fire','electric'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'ground' and (self.type2 in ['poison', 'rock','steel','fire','electric'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'ground' and (self.type1 in ['bug','grass'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'ground' and (self.type2 in ['bug','grass'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'ground' and (self.type1 in ['flying'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'ground' and (self.type2 in ['flying'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'rock' and (self.type1 in ['flying','bug','fire','ice'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'rock' and (self.type2 in ['flying','bug','fire','ice'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'rock' and (self.type1 in ['fighting','ground','steel'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'rock' and (self.type2 in ['fighting','ground','steel'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'bug' and (self.type1 in ['grass','psychic','dark'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'bug' and (self.type2 in ['grass','psychic','dark'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'bug' and (self.type1 in ['fighting','flying','poison','ghost','steel','fire','fairy'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'bug' and (self.type2 in ['fighting','flying','poison','ghost','steel','fire','fairy'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'ghost' and (self.type1 in ['ghost','psychic'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'ghost' and (self.type2 in ['ghost','psychic'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'ghost' and (self.type1 in ['dark'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'ghost' and (self.type2 in ['dark'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'ghost' and (self.type1 in ['normal'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'ghost' and (self.type2 in ['normal'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'steel' and (self.type1 in ['rock','ice','fairy'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'steel' and (self.type2 in ['rock','ice','fairy'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'steel' and (self.type1 in ['steel','fire','water','electric',])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'steel' and (self.type2 in ['steel','fire','water','electric'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'electric' and (self.type1 in ['flying','water'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'electric' and (self.type2 in ['flying','water'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'electric' and (self.type1 in ['grass','electric','dragon'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'electric' and (self.type2 in ['grass','electric','dragon'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'electric' and (self.type1 in ['ground'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'electric' and (self.type2 in ['ground'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'psychic' and (self.type1 in ['fighting','poison'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'psychic' and (self.type2 in ['fighting','poison'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'psychic' and (self.type1 in ['steel','psychic'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'psychic' and (self.type2 in ['steel','psychic'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'psychic' and (self.type1 in ['dark'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'psychic' and (self.type2 in ['dark'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'ice' and (self.type1 in ['flying','ground','grass','dragon'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'ice' and (self.type2 in ['flying','ground','grass','dragon'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'ice' and (self.type1 in ['steel','fire','water','ice'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'ice' and (self.type2 in ['steel','fire','water','ice'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'dragon' and (self.type1 in ['dragon'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'dragon' and (self.type2 in ['dragon'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'dragon' and (self.type1 in ['steel'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'dragon' and (self.type2 in ['steel'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'dragon' and (self.type1 in ['fairy'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'dragon' and (self.type2 in ['fairy'])):
            amount = 0
            print(f"{self.name} is immune to {movetype}")
        if (movetype == 'dark' and (self.type1 in ['ghost','psychic'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'dark' and (self.type2 in ['ghost','psychic'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'dark' and (self.type1 in ['fighting','dark','fairy'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'dark' and (self.type2 in ['fighting','dark','fairy'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'fairy' and (self.type1 in ['fighing','dragon','dark'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'fairy' and (self.type2 in ['fighting','dragon','dark'])):
            amount *= 2
            print("It's super effective!")
        if (movetype == 'fairy' and (self.type1 in ['poison','steel','fire'])):
            amount /= 2
            print("It's not very effective...")
        if (movetype == 'fairy' and (self.type2 in ['poison','steel','fire'])):
            amount /= 2
            print("It's not very effective...")

        if stab == True:
            amount *= 1.5

        rnd = (randint(85, 100)/100)
        amount = (amount * rnd)

        crit = 3
        crit_chance = randint(0, 24)
        if crit == crit_chance:
            print('A critical hit!')
            amount *= 1.5

        amount = round(amount)
        self.hp -= amount

        print(f'{self.name} lost {amount} hp')
        self.faint()

    ############ POKEMON FAINT METHOD ##############
    # This class method is fired every time a pokemon takes damage
    # and will print out either the amount of hp a pokemon has lost
    # or that the pokemon has fainted (is kill haha) if hp is below 0

    def faint(self):
        if self.hp <= 0:
            print(f'{self.name} is kill')
            print('')
        else:
            print(f'{self.name} has {self.hp} hp left')
            print('')

########################################################################################
#                  Save Class
# Use this class to store both pokemon's max hp before a battle starts
# To see an instance of this class in use, check the choice_two() helper function near
# the bottom of this script
# 
# This class takes in 2 parameters besides self, the max hp stat of both pokemon in a battle,
# and has two revive() methods that will restore each pokemon's hp

class Save:
    def __init__(self, pokemon1_hp, pokemon2_hp):
        self.hp1 = pokemon1_hp
        self.hp2 = pokemon2_hp

    def revive1(self):
        return self.hp1

    def revive2(self):
        return self.hp2

########################################################################################
#                Timer Class
# Use this to measure turns in a battle
# This class has two methods, an add_turn() method which adds one to the turn count (counter)
# and a reset() method, which sets the counter back to 0

class Timer:
    def __init__(self):
        self.counter = 0
    
    def add_turn(self):
        self.counter += 1
    
    def reset(self):
        self.counter = 0

# A useful instance of the Timer Class here to be used later
turn_counter = Timer()

########################################################################################
#          Instances of the Pokemon Class
# Find and create new instances of the Pokemon Class here
#
# Notice the python datatypes in each variable parameter of an instance of the pokemon class
# Note: All string values besides the pokemon's name are purely lowercase, along with the variable
# names for each instance of the class.
#
# The first is a string for the pokemon's name, followed by 6 integer values for a pokemon's
# stats: HP, ATTACK, DEFENSE, SPECIAL ATTACK, SPECIAL DEFENSE, SPEED, followed by the string values of a pokemon's
# typings (Pokemon usually have 2 types, but in the case of just one type, enter 'none' as the value for the second type),
# and lastly, the pokemon's moves, which is a python list containing 4 dictionaries with the keys 'name' for the movename,
# 'movetype' for the pokemon type of the move, 'damage' for the integer value of the move's damage, and 'phys_special' for
# the string values to determine whether or not the move is physical or special
#
# Note: Only moves with damage are currently supported in this version of the simulation and secondary effects along
# with move accuracy are not considered. If you want to, you can always add more keys to a dictionary, but starting simple
# would be helpful here.


venusaur = Pokemon('Venusaur', 364, 180, 202, 328, 237, 196, 'grass', 'poison',
 [{'name': 'sludge bomb', 'movetype': 'poison', 'damage': 90, 'phys_special': 'special'},
 {'name': 'solarbeam', 'movetype': 'grass', 'damage': 120, 'phys_special': 'special'},
 {'name': 'giga drain', 'movetype': 'grass', 'damage': 75, 'phys_special': 'special'},
 {'name': 'earthquake', 'movetype': 'ground', 'damage': 100, 'phys_special': 'physical'}])

charizard = Pokemon('Charizard', 297, 184, 192, 317, 206, 328, 'fire', 'flying',
 [{'name': 'fire blast', 'movetype': 'fire', 'damage': 110, 'phys_special': 'special'},
 {'name': 'solarbeam', 'movetype': 'grass', 'damage': 120, 'phys_special': 'special'},
 {'name': 'air slash', 'movetype': 'flying', 'damage': 75, 'phys_special': 'special'},
 {'name': 'focus blast', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'special'}])

blastoise = Pokemon('Blastoise', 338, 181, 236, 295, 246, 217, 'water', 'none',
 [{'name': 'dark pulse', 'movetype': 'dark', 'damage': 80, 'phys_special': 'special'},
 {'name': 'hydro pump', 'movetype': 'water', 'damage': 110, 'phys_special': 'special'},
 {'name': 'ice beam', 'movetype': 'ice', 'damage': 90, 'phys_special': 'special'},
 {'name': 'aura sphere', 'movetype': 'fighting', 'damage': 80, 'phys_special': 'special'}])

meganium = Pokemon('Meganium', 364, 180, 236, 291, 237, 196, 'grass', 'none',
 [{'name': 'ancient power', 'movetype': 'rock', 'damage': 60, 'phys_special': 'special'},
 {'name': 'solarbeam', 'movetype': 'grass', 'damage': 120, 'phys_special': 'special'},
 {'name': 'mega drain', 'movetype': 'grass', 'damage': 75, 'phys_special': 'special'},
 {'name': 'hyper beam', 'movetype': 'normal', 'damage': 150, 'phys_special': 'special'}])

typhlosion = Pokemon('Typhlosion', 297, 183, 192, 317, 207, 328, 'fire', 'none',
 [{'name': 'fire blast', 'movetype': 'fire', 'damage': 110, 'phys_special': 'special'},
 {'name': 'solarbeam', 'movetype': 'grass', 'damage': 120, 'phys_special': 'special'},
 {'name': 'extrasensory', 'movetype': 'psychic', 'damage': 80, 'phys_special': 'special'},
 {'name': 'focus blast', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'special'}])

feraligatr = Pokemon('Feraligatr', 312, 339, 236, 174, 202, 255, 'water', 'none',
 [{'name': 'ice punch', 'movetype': 'ice', 'damage': 75, 'phys_special': 'physical'},
 {'name': 'aqua tail', 'movetype': 'water', 'damage': 90, 'phys_special': 'physical'},
 {'name': 'crunch', 'movetype': 'dark', 'damage': 80, 'phys_special': 'physical'},
 {'name': 'dragon claw', 'movetype': 'dragon', 'damage': 80, 'phys_special': 'physical'}])

sceptile = Pokemon('Sceptile', 282, 206, 149, 309, 206, 372, 'grass', 'none',
 [{'name': 'focus blast', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'special'},
 {'name': 'leaf storm', 'movetype': 'grass', 'damage': 130, 'phys_special': 'special'},
 {'name': 'dragon pulse', 'movetype': 'dragon', 'damage': 85, 'phys_special': 'special'},
 {'name': 'earthquake', 'movetype': 'ground', 'damage': 100, 'phys_special': 'physical'}])

blaziken = Pokemon('Blaziken', 302, 339, 176, 230, 176, 284, 'fire', 'fighting',
 [{'name': 'flare blitz', 'movetype': 'fire', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'high jump kick', 'movetype': 'fighting', 'damage': 130, 'phys_special': 'physical'},
 {'name': 'brave bird', 'movetype': 'flying', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'blaze kick', 'movetype': 'fire', 'damage': 85, 'phys_special': 'physical'}])

swampert = Pokemon('Swampert', 404, 350, 216, 185, 216, 157, 'water', 'ground',
 [{'name': 'ice punch', 'movetype': 'ice', 'damage': 75, 'phys_special': 'physical'},
 {'name': 'aqua tail', 'movetype': 'water', 'damage': 90, 'phys_special': 'physical'},
 {'name': 'earthquake', 'movetype': 'ground', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'stone edge', 'movetype': 'rock', 'damage': 100, 'phys_special': 'physical'}])

torterra = Pokemon('Torterra', 394, 348, 246, 167, 206, 149, 'grass', 'ground',
 [{'name': 'stone edge', 'movetype': 'rock', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'wood hammer', 'movetype': 'grass', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'outrage', 'movetype': 'dragon', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'earthquake', 'movetype': 'ground', 'damage': 100, 'phys_special': 'physical'}])

infernape = Pokemon('Infernape', 293, 307, 179, 219, 178, 346, 'fire', 'fighting',
 [{'name': 'flare blitz', 'movetype': 'fire', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'close combat', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'stone edge', 'movetype': 'rock', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'thunder punch', 'movetype': 'electric', 'damage': 75, 'phys_special': 'physical'}])

empoleon = Pokemon('Empoleon', 349, 187, 236, 353, 238, 156, 'water', 'steel',
 [{'name': 'flash cannon', 'movetype': 'steel', 'damage': 80, 'phys_special': 'special'},
 {'name': 'hydro pump', 'movetype': 'water', 'damage': 110, 'phys_special': 'special'},
 {'name': 'ice beam', 'movetype': 'ice', 'damage': 90, 'phys_special': 'special'},
 {'name': 'grass knot', 'movetype': 'grass', 'damage': 100, 'phys_special': 'special'}])

serperior = Pokemon('Serperior', 291, 167, 227, 249, 226, 357, 'grass', 'none',
 [{'name': 'dragon pulse', 'movetype': 'dragon', 'damage': 85, 'phys_special': 'special'},
 {'name': 'leaf storm', 'movetype': 'grass', 'damage': 130, 'phys_special': 'special'},
 {'name': 'giga drain', 'movetype': 'grass', 'damage': 75, 'phys_special': 'special'},
 {'name': 'aqua tail', 'movetype': 'water', 'damage': 90, 'phys_special': 'physical'}])

emboar = Pokemon('Emboar', 362, 379, 166, 212, 166, 229, 'fire', 'fighting',
 [{'name': 'head smash', 'movetype': 'rock', 'damage': 150, 'phys_special': 'physical'},
 {'name': 'flare blitz', 'movetype': 'fire', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'hammer arm', 'movetype': 'fighting', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'wild charge', 'movetype': 'electric', 'damage': 90, 'phys_special': 'physical'}])

samurott = Pokemon('Samurott', 332, 328, 206, 226, 176, 239, 'water', 'none',
 [{'name': 'megahorn', 'movetype': 'bug', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'aqua tail', 'movetype': 'water', 'damage': 90, 'phys_special': 'physical'},
 {'name': 'night slash', 'movetype': 'dark', 'damage': 70, 'phys_special': 'physical'},
 {'name': 'superpower', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'physical'}])

chesnaught = Pokemon('Chesnaught', 380, 313, 309, 165, 186, 164, 'grass', 'fighting',
 [{'name': 'hammer arm', 'movetype': 'fighting', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'wood hammer', 'movetype': 'grass', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'stone edge', 'movetype': 'rock', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'zen headbutt', 'movetype': 'psychic', 'damage': 80, 'phys_special': 'physical'}])

delphox = Pokemon('Delphox', 292, 156, 180, 327, 236, 337, 'fire', 'psychic',
 [{'name': 'solarbeam', 'movetype': 'grass', 'damage': 120, 'phys_special': 'special'},
 {'name': 'fire blast', 'movetype': 'fire', 'damage': 110, 'phys_special': 'special'},
 {'name': 'future sight', 'movetype': 'psychic', 'damage': 120, 'phys_special': 'special'},
 {'name': 'dazzling gleam', 'movetype': 'fairy', 'damage': 80, 'phys_special': 'special'}])

greninja = Pokemon('Greninja', 286, 203, 170, 305, 178, 377, 'water', 'dark',
 [{'name': 'dark pulse', 'movetype': 'dark', 'damage': 80, 'phys_special': 'special'},
 {'name': 'hydro pump', 'movetype': 'water', 'damage': 110, 'phys_special': 'special'},
 {'name': 'ice beam', 'movetype': 'ice', 'damage': 90, 'phys_special': 'special'},
 {'name': 'extrasensory', 'movetype': 'psychic', 'damage': 80, 'phys_special': 'special'}])

decidueye = Pokemon('Decidueye', 298, 344, 186, 212, 236, 239, 'grass', 'ghost',
 [{'name': 'brave bird', 'movetype': 'flying', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'phantom force', 'movetype': 'ghost', 'damage': 90, 'phys_special': 'physical'},
 {'name': 'leaf blade', 'movetype': 'grass', 'damage': 90, 'phys_special': 'physical'},
 {'name': 'sucker punch', 'movetype': 'dark', 'damage': 70, 'phys_special': 'physical'}])

incineroar = Pokemon('Incineroar', 332, 361, 216, 176, 216, 219, 'fire', 'dark',
 [{'name': 'cross chop', 'movetype': 'fighting', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'darkest lariat', 'movetype': 'dark', 'damage': 85, 'phys_special': 'physical'},
 {'name': 'flare blitz', 'movetype': 'fire', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'earthquake', 'movetype': 'ground', 'damage': 100, 'phys_special': 'physical'}])

primarina = Pokemon('Primarina', 364, 202, 184, 315, 269, 156, 'water', 'fairy',
 [{'name': 'moonblast', 'movetype': 'fairy', 'damage': 95, 'phys_special': 'special'},
 {'name': 'hydro pump', 'movetype': 'water', 'damage': 110, 'phys_special': 'special'},
 {'name': 'ice beam', 'movetype': 'ice', 'damage': 90, 'phys_special': 'special'},
 {'name': 'energy ball', 'movetype': 'grass', 'damage': 80, 'phys_special': 'special'}])

mewtwo = Pokemon('Mewtwo', 354, 230, 216, 407, 216, 394, 'psychic', 'none',
 [{'name': 'psystrike', 'movetype': 'psychic', 'damage': 100, 'phys_special': 'special'},
 {'name': 'focus blast', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'special'},
 {'name': 'shadow ball', 'movetype': 'ghost', 'damage': 80, 'phys_special': 'special'},
 {'name': 'ice beam', 'movetype': 'ice', 'damage': 90, 'phys_special': 'physical'}])

rayquaza = Pokemon('Rayquaza', 352, 399, 216, 302, 216, 317, 'dragon', 'flying',
 [{'name': 'outrage', 'movetype': 'dragon', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'earthquake', 'movetype': 'ground', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'dragon ascent', 'movetype': 'flying', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'extremespeed', 'movetype': 'normal', 'damage': 80, 'phys_special': 'physical'}])

kyogre = Pokemon('Kyogre', 342, 212, 216, 438, 354, 241, 'water', 'none',
 [{'name': 'water spout', 'movetype': 'water', 'damage': 150, 'phys_special': 'special'},
 {'name': 'thunder', 'movetype': 'electric', 'damage': 110, 'phys_special': 'special'},
 {'name': 'ice beam', 'movetype': 'ice', 'damage': 90, 'phys_special': 'special'},
 {'name': 'surf', 'movetype': 'water', 'damage': 90, 'phys_special': 'special'}])

groudon = Pokemon('Groudon', 342, 438, 354, 261, 216, 194, 'ground', 'none',
 [{'name': 'precipice blades', 'movetype': 'ground', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'solarbeam', 'movetype': 'grass', 'damage': 120, 'phys_special': 'special'},
 {'name': 'stone edge', 'movetype': 'rock', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'eruption', 'movetype': 'fire', 'damage': 150, 'phys_special': 'special'}])

arceus = Pokemon('Arceus', 382, 248, 276, 372, 276, 339, 'normal', 'none',
 [{'name': 'judgement', 'movetype': 'normal', 'damage': 100, 'phys_special': 'special'},
 {'name': 'focus blast', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'special'},
 {'name': 'future sight', 'movetype': 'psychic', 'damage': 120, 'phys_special': 'special'},
 {'name': 'draco meteor', 'movetype': 'dragon', 'damage': 130, 'phys_special': 'special'}])

lugia = Pokemon('Lugia', 416, 194, 325, 216, 345, 319, 'psychic', 'flying',
 [{'name': 'future sight', 'movetype': 'psychic', 'damage': 120, 'phys_special': 'special'},
 {'name': 'hydro pump', 'movetype': 'water', 'damage': 110, 'phys_special': 'special'},
 {'name': 'aeroblast', 'movetype': 'flying', 'damage': 100, 'phys_special': 'special'},
 {'name': 'thunder', 'movetype': 'electric', 'damage': 110, 'phys_special': 'special'}])

ho_oh = Pokemon('Ho-Oh', 354, 394, 216, 230, 344, 279, 'fire', 'flying',
 [{'name': 'brave bird', 'movetype': 'flying', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'sacred fire', 'movetype': 'fire', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'earthquake', 'movetype': 'ground', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'sky attack', 'movetype': 'flying', 'damage': 140, 'phys_special': 'physical'}])

dialga = Pokemon('Dialga', 342, 248, 314, 438, 236, 241, 'dragon', 'steel',
 [{'name': 'roar of time', 'movetype': 'dragon', 'damage': 150, 'phys_special': 'special'},
 {'name': 'earth power', 'movetype': 'ground', 'damage': 90, 'phys_special': 'special'},
 {'name': 'flash cannon', 'movetype': 'steel', 'damage': 90, 'phys_special': 'special'},
 {'name': 'thunder', 'movetype': 'electric', 'damage': 110, 'phys_special': 'special'}])

palkia = Pokemon('Palkia', 322, 248, 236, 399, 276, 328, 'dragon', 'water',
 [{'name': 'spacial rend', 'movetype': 'dragon', 'damage': 100, 'phys_special': 'special'},
 {'name': 'hydro pump', 'movetype': 'water', 'damage': 110, 'phys_special': 'special'},
 {'name': 'fire blast', 'movetype': 'fire', 'damage': 110, 'phys_special': 'special'},
 {'name': 'focus blast', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'special'}])

giratina = Pokemon('Giratina', 442, 339, 236, 248, 236, 306, 'dragon', 'ghost',
 [{'name': 'shadow force', 'movetype': 'ghost', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'earthquake', 'movetype': 'ground', 'damage': 100, 'phys_special': 'physical'},
 {'name': 'outrage', 'movetype': 'dragon', 'damage': 120, 'phys_special': 'physical'},
 {'name': 'stone edge', 'movetype': 'rock', 'damage': 100, 'phys_special': 'physical'}])

yveltal = Pokemon('Yveltal', 394, 268, 226, 397, 232, 297, 'dark', 'flying',
 [{'name': 'dark pulse', 'movetype': 'dark', 'damage': 120, 'phys_special': 'special'},
 {'name': 'hurricane', 'movetype': 'flying', 'damage': 110, 'phys_special': 'special'},
 {'name': 'psychic', 'movetype': 'psychic', 'damage': 90, 'phys_special': 'special'},
 {'name': 'focus blast', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'special'}])

xerneas = Pokemon('Xerneas', 394, 268, 226, 397, 232, 297, 'fairy', 'none',
 [{'name': 'moonblast', 'movetype': 'fairy', 'damage': 126, 'phys_special': 'special'},
 {'name': 'focus blast', 'movetype': 'fighting', 'damage': 120, 'phys_special': 'special'},
 {'name': 'thunder', 'movetype': 'electric', 'damage': 110, 'phys_special': 'special'},
 {'name': 'flash cannon', 'movetype': 'steel', 'damage': 80, 'phys_special': 'special'}])

# PART 2 ############ TO DO ###############
# Create at least 3 new instances of the Pokemon Class
# here. You can check to see if the pokemon has been created properly
# by printing its different attribuites.

# 1st new instance

# 2nd new instance

# 3rd new instance


########################################################################################
#                LIST OF ALL POKEMON INSTANCES
# PART 2 ########### TO DO ##################
# Add your new instances of the pokemon class to the list of all_pokemon

all_pokemon = [venusaur, charizard, blastoise, meganium, typhlosion, feraligatr, sceptile, blaziken, swampert, torterra, infernape, empoleon, serperior, emboar, samurott, chesnaught, delphox, greninja, decidueye, incineroar, primarina, mewtwo, groudon, kyogre, rayquaza, lugia, ho_oh, palkia, dialga, giratina, yveltal, xerneas, arceus]


########################################################################################
#                BATTLE FUNCTION
# This is where it all comes together
# The battle function takes in 4 parameters, the two pokemon choices, a turn counter, and an
# instance of the Save Class
# It recursively simulates a battle between the two pokemon by using their inbuilt class methods
# It declares a winner and ends the game if a pokemon's hp is at or below zero
# And in the case of the game, it resets the turn counter and returns a new game by passing 3 parameters into the 
# new_game() function


def battle():       # def battle(???, ???, ???, ???):
    # PART 3 ############# TO DO ###################
    # Establish a base case for the pokemon battle simulation
    # Add to the turn count on each turn (recursion)
    # Create a randomized selection of moves for both pokemon
    # Store each pokemon's move selection as integer variables
    # Store each move's name as variables
    # Store the data from each pokemon's moves into variables 
    # Have the faster pokemon attack first
    # Then have the second pokemon attack
    # Print out which pokemon is making which attack whenever a pokemon makes an attack
    # Send the right data for the pokemon to take damage from the other pokemon's attacks
    # Set proper win conditions
    # Print out which pokemon has won if there is a winner
    # Return a new_game() with the proper 3 parameters if there is a win
    # After both pokemon have made a move return the updated data as a recursive callback

    # BASE CASE HERE

    # RECURSIVE CASE HERE

    return # ???????

########################################################################################
#                NEW GAME FUNCTION
# Takes in the 3 data variable parameters returned from the battle() function
# Prompts a user to replay the battle, start a new game, or quit the game
# Resets the initial states of both pokemon in the case of a new game or replay
# then returns a new battle() function with updated data in its 4 parameters


def new_game(pokemon1, pokemon2, save_mon):
    print('')
    print('Replay battle? (yes/no)')
    choice = input()
    if choice == 'yes':
        pokemon1.revive(save_mon.hp1)
        pokemon2.revive(save_mon.hp2)
        return battle(pokemon1, pokemon2, turn_counter, save_mon)
    elif choice == 'no':
        print('')
        print('Do you want to start a new battle or quit? (new / quit)')
        new_quit = input()
        if new_quit == 'new':
            pokemon1.revive(save_mon.hp1)
            pokemon2.revive(save_mon.hp2)
            print('')
            print('Ok')
            return choice_one()
        elif new_quit == 'quit':
            print('')
            print('See you next time!')
            return
        else:
            print('')
            print('Just answer the question...')
            return new_game(pokemon1, pokemon2, save_mon)

    else:
        print('Give a yes or no')
        return new_game(pokemon1, pokemon2, save_mon)

########################################################################################
#                HELPER FUNCTIONS
# These functions are used to set up the game state
# they might also be useful for understanding the functions above

################# INTRO ###################
# Starts the whole script when it is run
# Fires choice_one()

def intro():
    print('Welcome to Adam\'s Pokémon Battle Simulator!')
    print('This simulator uses some optimized pokémon stats and moves for its current level of complexity, but feel free to add in or edit pokémon at your leisure!')
    print('')
    print('You can start by picking your first pokemon from this list:')
    choice_one()

############## CHOICE ONE #################
# Fired by intro(), prompts the user to make a choice for the first pokemon, saves the 
# pokemon to a variable and passes it on when firing choice_two()

def choice_one():
    pokemon1 = ''
    print('')
    for pokemon in all_pokemon:
        print(pokemon.name, end=', ')
    print('')
    print('')
    print('Enter a pokémon\'s name to start')
    choice = input()
    for i in range(0, len(all_pokemon)):
        if choice.lower() == all_pokemon[i].name.lower():
            pokemon1 = all_pokemon[i]
    if pokemon1 not in all_pokemon:
        print('Not a pokémon! Try again!')
        return choice_one()
    print(f'You picked {pokemon1.name}! Would you like to know more about')
    print('this pokémon? (yes/no)')
    pokemon1_info = input()
    print('')
    if pokemon1_info == 'yes':
        print(f'{pokemon1.name}')
        if pokemon1.type2 != 'none':
            print(f'Type: {pokemon1.type1} / {pokemon1.type2}')
        else:
            print(f'Type: {pokemon1.type1}')
        print('')
        print(' HP Atk Def SpA SpD Spd')
        print(f'{pokemon1.hp} {pokemon1.ph_attack} {pokemon1.defense} {pokemon1.sp_attack} {pokemon1.sp_defense} {pokemon1.speed}')
        print('')
        for i in range(0, len(pokemon1.moves)):
            print(f"Move {i+1}: {pokemon1.moves[i]['name']}, type: {pokemon1.moves[i]['movetype']}, damage: {pokemon1.moves[i]['damage']}, {pokemon1.moves[i]['phys_special']} attack")
    elif pokemon1_info == 'no':
        print('Ok')
    else:
        print('Ok, pick a new pokémon.')
        return choice_one()
    print('')
    print('Do you want this to be your first pokémon? (yes/no)')
    confirm = input()
    if confirm == 'yes':
        print(f'{pokemon1.name} is ready for battle!')
        return choice_two(pokemon1)
    else:
        print('Ok, pick a new pokémon.')
        return choice_one()

################## CHOICE TWO #######################
# Prompts a user to choose a second pokemon
# Then, after the user has chosen, SAVES the initial states of BOTH pokemon and 
# starts the battle simulation with pokemon1 and pokemon2 

def choice_two(pokemon1):
    pokemon2 = ''
    print('')
    print('Pick a second pokémon to start the battle!')
    print('')
    for pokemon in all_pokemon:
        print(pokemon.name, end=', ')
    print('')
    print('')
    choice = input()
    for i in range(0, len(all_pokemon)):
        if choice.lower() == all_pokemon[i].name.lower():
            pokemon2 = all_pokemon[i]
    if pokemon2 not in all_pokemon:
        print('Not a pokémon! Try again!')
        return choice_two(pokemon1)
    print(f'You picked {pokemon2.name}! Would you like to know more about')
    print('this pokémon? (yes/no)')
    pokemon2_info = input()
    print('')
    if pokemon2_info == 'yes':
        print(f'{pokemon2.name}')
        if pokemon2.type2 != 'none':
            print(f'Type: {pokemon2.type1} / {pokemon2.type2}')
        else:
            print(f'Type: {pokemon2.type1}')
        print('')
        print(' HP Atk Def SpA SpD Spd')
        print(f'{pokemon2.hp} {pokemon2.ph_attack} {pokemon2.defense} {pokemon2.sp_attack} {pokemon2.sp_defense} {pokemon2.speed}')
        print('')
        for i in range(0, len(pokemon2.moves)):
            print(f"Move {i+1}: {pokemon2.moves[i]['name']}, type: {pokemon2.moves[i]['movetype']}, damage: {pokemon2.moves[i]['damage']}, {pokemon2.moves[i]['phys_special']} attack")
    elif pokemon2_info == 'no':
        print('Ok')
    else:
        print('Ok, pick a new pokémon.')
        return choice_two(pokemon1)
    print('')
    print('Do you want this to be your second pokémon? (yes/no)')
    confirm = input()
    if confirm == 'yes':
        print(f'{pokemon2.name} is ready for battle!')
    else:
        print('Ok, pick a new pokémon.')
        return choice_two(pokemon1)
    print('')
    print('Are you ready?')
    
    save_mon = Save(pokemon1.hp, pokemon2.hp)
    ready = input()
    if ready == 'yes':
        print("Let's gooo!")
    else:
        print('Too bad!')
    print('')
    print(f'Starting battle between {pokemon1.name} and {pokemon2.name} in:')
    def timer(n):
        if n < 0:
            print('')
            print(f"It's a battle to the death between {pokemon1.name} and {pokemon2.name}!")
            return battle(pokemon1, pokemon2, turn_counter, save_mon)
        else:
            print(f'{n}!')
            return timer(n - 1)
    timer(10)
intro()