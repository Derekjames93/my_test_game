import random
class Human:
    affinity = "Magic"
    
    
    #Initialize Instance Attributes
    def __init__(self, name,class_1, class_nature,):
        self.name = name
        self.class_1 = class_1
        self.class_nature = class_nature
        self.luck_stat = random.randint(0,10)
        self.Mana = 100
        self.dmg_mod = 1.0
        self.health = 100
    # Cast Fireball
    def fireball(self):
        if self.luck_stat > 3 :
            self.dmg_mod += 1.5
            print("It's your lucky day!")
            print(f"Fireball dmg modifier increased by {self.dmg_mod} percent")
        if self.affinity == "Magic" and self.Mana >= 5 :
            print("Fireball!")
            self.Mana -= 5
            print(f"You have {self.Mana} mana left.")
        else :
            print("I don't have enough mana!")
    # Cast Pyroblast
    def Pyroblast(self):
        if self.luck_stat > 7 :
            self.dmg_mod += 1.5
            print("It's your lucky day!")
            print(f"Pyroblast dmg modifier increased by {self.dmg_mod} percent")
        if self.affinity == "Magic" and self.Mana >= 15 :
            print("Pyroblast")
            self.Mana -= 15
            print(f"You have {self.Mana} mana left.")
        else :
            print("I don't have enough mana!")
    # Create a random generated integer for luck stat
    # def luck_stat(self):
    #     self
    # Create spell to restore mana
    def evocation(self):
        self.Mana += 50
        print(self.Mana)

class Orc :

    def __init__(self, name, class_1):
        self.name = name
        self.class_1 = class_1
        self.health = 100
        self.attack = 10
        self.luck_stat = random.randint(0,10)

    def normal_attack(self,target):
        attack = self.attack
        if self.luck_stat > 5 :
            attack += 2
            print(f"Orc has critically hit{target.name} for {attack}!")
            
        else :
            print(f"Orc has  hit {target.name}for {attack}!")
        target.health = target.health - attack
        print(f"{target.name} has {target.health} hp points")










# Create Jaina
Jaina = Human("Jaina","High-Mage","Arcane magic")
#Create an enemy
Green_Orc = Orc("Green Orc", "Peon")

# print(f"I am {Jaina.name}, a {Jaina.class_1} that resides in Dalaran. I have a natural affinity in {Jaina.class_nature}.")
# Jaina.fireball()
# Jaina.Pyroblast()
# Jaina.Pyroblast()
# Jaina.evocation()
Green_Orc.normal_attack(Jaina)
