# Pokemon  class
class Pokemon:
    def __init__(self, name, type, level = 5):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False

    def lose_health(self, health_lost):
        self.health -= health_lost
        if self.health <= 0:
            self.knock_out()
        else:
            print("{pokemon} has {health} HP!".format(pokemon=self.name,health=self.health))

    def gain_health(self, health_gained):
        self.health += health_gained
        if (self.health > self.max_health):
            self.health = self.max_health
        print("{pokemon} gained {healthgain} HP".format(pokemon=self.name, healthgain= health_gained ))

    def attack(self, enemy):
        if (self.is_knocked_out):
            print("{name} is knocked out and can't attack!".format(name=self.name))
        elif (enemy.is_knocked_out):
            print("You can't attack a knocked out pokemon!")
        else:
            if ((self.type == "Grass") and (enemy.type == "Fire")) or ((self.type == "Fire") and (enemy.type == "Water")) or ((self.type == "Water") and (enemy.type == "Grass")):
                damage_dealt = enemy.level * 0.5
                message = "It was not very effective!"
            elif ((self.type == "Grass") and (enemy.type == "Water")) or ((self.type == "Fire") and (enemy.type == "Grass")) or ((self.type == "Water") and (enemy.type == "Fire")):
                damage_dealt = enemy.level * 1.5
                message = "It was super effective!"
            else:
                damage_dealt = enemy.level
                message = "Good hit!"
            print("{your_pokemon} attacked {enemy_pokemon} for {damage} damage!".format(your_pokemon=self.name, enemy_pokemon=enemy.name, damage=damage_dealt))
            print(message)
            enemy.lose_health(damage_dealt)

    def knock_out(self):
        self.health = 0
        self.is_knocked_out = True
        print("{pokemon} has been knocked out!".format(pokemon=self.name))     
    
#Trainer Class
class Trainer:
    def __init__(self, name, pokemon, potions):
        self.name = name
        self.pokemon = pokemon
        self.potions = potions
        self.active_pokemon = 0
    
    def __repr__(self):
        print("\n{self}'s Pokemon: ".format(self=self.name))
        for pokemon in self.pokemon:
            print("{name}, {type}-Type, Level:{level}, HP: {HP}".format(name=pokemon.name, type=pokemon.type, level = pokemon.level, HP=pokemon.health))
        return "Current Pokemon: {pokemon}".format(pokemon=self.pokemon[self.active_pokemon].name)

    def use_potion(self):
        print("\n")
        if (self.potions == 0):
            print ("{name} have no potions!".format(name = self.name))
        else:
            self.potions -= 1
            print("{name} used a potion on {pokemon}".format(name= self.name, pokemon=self.pokemon[self.active_pokemon].name))
            self.pokemon[self.active_pokemon].gain_health(30)
            print("{pokemon} has {HP} HP left".format(pokemon=self.pokemon[self.active_pokemon].name, HP=self.pokemon[self.active_pokemon].health))

    def attack_trainer(self, enemy):
        print("\n")
        if (self.pokemon[self.active_pokemon].is_knocked_out):
            print("{name}'s {pokemon} is knocked out! Swap to another pokemon".format(name = self.name, pokemon=self.pokemon[self.active_pokemon].name))
        else:
            print("{your_name}'s {your_pokemon} attacked {enemy_name}'s {enemy_pokemon}!".format(your_name = self.name, your_pokemon=self.pokemon[self.active_pokemon].name, enemy_name=enemy.name, enemy_pokemon=enemy.pokemon[enemy.active_pokemon].name))
            self.pokemon[self.active_pokemon].attack(enemy.pokemon[enemy.active_pokemon])

    def swap_pokemon(self, desired_pokemon):
        print("\n")
        if (self.pokemon[desired_pokemon].is_knocked_out):
            print("You can't swap to a knocked out pokemon!")
        else:
            print("{name}'s swapping Pokemon!\nCome back {pokemon}!".format(name=self.name, pokemon=self.pokemon[self.active_pokemon].name))
            self.active_pokemon = desired_pokemon
            print ("{pokemon} I choose you!".format(pokemon = self.pokemon[self.active_pokemon].name))

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

print(Red)
print(Blue)

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



