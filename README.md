# Pokémon Python Lab
<div>
  <img src="https://wallpapercave.com/wp/d4emJ2t.jpg" alt="pokemon" />
</div>

### An exploration in Python3 data types, object oriented programming (OOP), and recursion.

## Introduction
You have been given an unfinished Pokémon battle simulator python script that is capable of running infinite simulations of Pokémon battles. Your goal is to complete the pokemon.py battle script to be able to run battle simulations. This task is broken up into 3 parts which will be described below and are also written out inline with the script.  

### Part 1
- `fork` and `clone` this repository. _Maybe give it a star 🙄🤞? Entirely up to you._
- Take a look at the structure of the `pokemon.py` script. While it is long, it's split up nicely into 3 main sections from top to bottom. The first section is involved with classes, the second is involved with battle functions, and the third section is where the helper functions for the initialization of the game are found. Each section's parts have been commented out to give more information about what is being accomplished where.
- Find the section for Part 1 in the Classes section of the script. It is labelled by `# PART 1`
- In this section, your task is to:
  - 1. Initialize the Pokemon class. This class requires 10 variable parameters besides `self` in its initialization. Take a look at instances of the class, the order of data in the instances, and places in some of the class's pre-built methods that use these variable parameters to find what you might need in the class's initialization.
  - 2. Define a `revive()` method for the Pokemon class which takes in one other variable parameter besides `self`.
- To test out if your initialization of the class was correct, you can comment out the `intro()` function call at the bottom of the script and try to print data from instances of the Pokemon class.

### Part 2
- Find the sections for Part 2, labelled by `# PART 2` in the class instances sections of this script. Both sections for Part 2 are right next to each other.
- In this simulation, all Pokémon are at level 100.
- Your goal is to create 3 or more accurate instances of the Pokemon class.
- To assist in this goal, here are 2 resources that will be helpful _(if you want your simulation to be accurate)_:
  - https://www.serebii.net/pokedex-sm/ Find any 3 Pokémon that you like from this Pokédex. This will help you find the proper data for each Pokémon's name, typings, and move data. Choose 4 moves with damage that the Pokémon can learn (damage is the integer value in the Att. column for moves).
  - http://psypokes.com/dex/stats.php Once you have found a Pokémon's name, typings, and moves, this resource will help you properly calculate its stats at level 100. You can find the Pokémon by name in the top dropdown list. EVs (Effort Values) for each stat have a max amount of 252 and will boost the value of the Pokémon's stat. The total EVs a Pokémon can have is 508. Typically, a Pokémon is optimized with 252 EVs in two stats and 4 in another. Natures also affect stat maximums, which can be selected from in the Nature dropdown list.
 - Cheers to data aggregation! After you've completed your 3+ Pokémon, add them to the `all_pokemon` list. 
 
### Part 3
- Find the section for Part 3, labelled `# PART 3` in the battle functions section of the script.
- Your goal is to finish the `battle()` function, which has instructions pseudocoded for your use.
- Once you've completed the function, you can test your simulation! Make sure that `intro()` is being called in at the bottom of the script.
- Congratulations! You should now be able to run infinite (and accurate) Pokémon battle simulations with this script. 

### Bonus
- These are all completely unnecessary but if you're ever feeling up to the challenge, here are some ideas:
  - Add functionality for status moves, recovery moves, accuracy, additional move effects, or multi-turn moves.
  - Implement the RESTful Pokémon API: https://pokeapi.co/ . It might be nice to also seed a database with a couple API calls, but that's a major stretch goal.
  - Create a probability function to test the probability of one Pokémon defeating another.
  - Add functionality for team battles.
   
  <br />
  <div>
    <img src="https://i.imgur.com/OpUVg9z.gif" alt="battle" />
  </div>
  
  Have fun with your new Pokémon battle simulator!
  
