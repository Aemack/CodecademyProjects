# Pokemon  class
class Pokemon:

    # Dunder method, sets property values
    def __init__(self, name, type, level = 5):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False

    # Takes in amount of health lost takes it away from pokemons health
    def lose_health(self, health_lost):
        self.health -= health_lost

        # Checks to see if pokemon is knocked out, if so runs knock out function
        if self.health <= 0:
            self.knock_out()
        
        # Otherwise print how much health pokemon has left
        else:
            print("{pokemon} has {health} HP!".format(pokemon=self.name,health=self.health))


    # Takes in amount of health gained and adds it to pokemons health
    def gain_health(self, health_gained):
        self.health += health_gained

        # Checks to see if pokemon has over max-health, if so sets health to max
        if (self.health > self.max_health):
            self.health = self.max_health

        # Prints how much health pokemon gained
        print("{pokemon} gained {healthgain} HP".format(pokemon=self.name, healthgain= health_gained ))



    def attack(self, enemy):

        # Checks if self is knocked out and prints appropriate string
        if (self.is_knocked_out):
            print("{name} is knocked out and can't attack!".format(name=self.name))

        # Checks if enemy is knocked out and prints appropriate string
        elif (enemy.is_knocked_out):
            print("You can't attack a knocked out pokemon!")

        else:
            
        # Checks if attack is weak, assigns string and assigns damage appropriately
            if ((self.type == "Grass") and (enemy.type == "Fire")) or ((self.type == "Fire") and (enemy.type == "Water")) or ((self.type == "Water") and (enemy.type == "Grass")):
                damage_dealt = enemy.level * 0.5
                message = "It was not very effective!"

            #Checks if attack is strong, assigns string and assigns damage appropriately
            elif ((self.type == "Grass") and (enemy.type == "Water")) or ((self.type == "Fire") and (enemy.type == "Grass")) or ((self.type == "Water") and (enemy.type == "Fire")):
                damage_dealt = enemy.level * 1.5
                message = "It was super effective!"
            
            # Otherwise it is normal damage, assigns string and assigns damage appropriately
            else:
                damage_dealt = enemy.level
                message = "Good hit!"
            
            # Prints who's pokemon attackes who and for how much damage
            print("{your_pokemon} attacked {enemy_pokemon} for {damage} damage!".format(your_pokemon=self.name, enemy_pokemon=enemy.name, damage=damage_dealt))
            
            # Prints effectiveness string
            print(message)

            # Runs lose_health function on enemy pokemon
            enemy.lose_health(damage_dealt)


    def knock_out(self):

        #Sets health to 0 and knocked_out to true
        self.health = 0
        self.is_knocked_out = True

        # Prints which pokemon is knocked out
        print("{pokemon} has been knocked out!".format(pokemon=self.name))     
    
#Trainer Class
class Trainer:

    # Dunder method sets property values
    def __init__(self, name, pokemon, potions):
        self.name = name
        self.pokemon = pokemon
        self.potions = potions
        self.active_pokemon = 0
    
    #Prints trainers pokemon when created
    def __repr__(self):
        print("\n{self}'s Pokemon: ".format(self=self.name))
        # Loops through players pokemon and prints details, returning the current pokemon
        for pokemon in self.pokemon:
            print("{name}, {type}-Type, Level:{level}, HP: {HP}".format(name=pokemon.name, type=pokemon.type, level = pokemon.level, HP=pokemon.health))
        return "Current Pokemon: {pokemon}".format(pokemon=self.pokemon[self.active_pokemon].name)



    def use_potion(self):
        print("\n")
        # Checks if trainer has potions, if not prints warning message
        if (self.potions == 0):
            print ("{name} have no potions!".format(name = self.name))
        
        # Takes one away from potion count and prints action
        else:
            self.potions -= 1
            print("{name} used a potion on {pokemon}".format(name= self.name, pokemon=self.pokemon[self.active_pokemon].name))
            
            # Runs gain health function on active pokemon
            self.pokemon[self.active_pokemon].gain_health(30)
            print("{pokemon} has {HP} HP left".format(pokemon=self.pokemon[self.active_pokemon].name, HP=self.pokemon[self.active_pokemon].health))



    def attack_trainer(self, enemy):
        print("\n")
        # Checks if pokemon is knocked out, if so prints warning message
        if (self.pokemon[self.active_pokemon].is_knocked_out):
            print("{name}'s {pokemon} is knocked out! Swap to another pokemon".format(name = self.name, pokemon=self.pokemon[self.active_pokemon].name))
        
        # Prints action and runs attack function on active pokemon against enemy's pokemon 
        else:
            print("{your_name}'s {your_pokemon} attacked {enemy_name}'s {enemy_pokemon}!".format(your_name = self.name, your_pokemon=self.pokemon[self.active_pokemon].name, enemy_name=enemy.name, enemy_pokemon=enemy.pokemon[enemy.active_pokemon].name))
            self.pokemon[self.active_pokemon].attack(enemy.pokemon[enemy.active_pokemon])



    def swap_pokemon(self, desired_pokemon):
        print("\n")
        # Checks if desired pokemon is knocked out, if so prints a warning message
        if (self.pokemon[desired_pokemon].is_knocked_out):
            print("You can't swap to a knocked out pokemon!")

        # Prints action, swaps active pokemon to desired pokemon and prints catch phrase
        else:
            print("{name}'s swapping Pokemon!\n\"Come back {pokemon}!".format(name=self.name, pokemon=self.pokemon[self.active_pokemon].name))
            self.active_pokemon = desired_pokemon
            print ("{pokemon} I choose you!\"".format(pokemon = self.pokemon[self.active_pokemon].name))


# Makes a bunch of pokemon objects 
    #Could have made them randomly generate level or have level as another parameter
Charmander = Pokemon("Charmander","Fire",10)
Bulbasaur = Pokemon("Bulbasaur","Grass",11)
Squirtle = Pokemon("Squirtle","Water",7)
Butterfree = Pokemon("Butterfree","Grass",9)
Caterpie = Pokemon("Butterfree","Grass",5)
Polywhirl = Pokemon("Polywhirl","Water",7)
Magmar = Pokemon("Magmar","Fire",3)
Venasaur = Pokemon("Venasaur","Grass",19)

Red = Trainer("Red",[Venasaur,Magmar,Caterpie,Squirtle,Charmander,Polywhirl],4)
Blue = Trainer("Blue",[Charmander,Bulbasaur,Butterfree,Squirtle,Magmar,Polywhirl],4)

# Runs __repr__ methods and prints returned value (player pokemon details)
print(Red)
print(Blue)


#The battle begins!
Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.swap_pokemon(1)
Blue.use_potion()


Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.use_potion
Blue.attack_trainer(Red)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.swap_pokemon(5)
Blue.attack_trainer(Red)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)


Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.use_potion()
Blue.swap_pokemon(2)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)

Red.attack_trainer(Blue)
Blue.attack_trainer(Red)



