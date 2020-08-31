import random
# class Character:
#     def __init__(self, name, health,power):
#         self.name = name
#         self.health = health
#         self.power = power
class Character():
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.attack = 5
        self.coins = 20
        self.luck = 0
        self.armor = 0

    def buy(self, item):
        self.coins -= item.cost
        item.apply(Human)

    # Enemy Spawn
    def Enemy_spawn(self):
        if random.randint(1,10) < 7:
            print(f"\nA {Green_Orc} has appeared and has {Green_Orc.health} health")
            return Green_Orc.name
        else :
            print(f"\nA {Troll} has appeared and has {Troll.health} health")
            return Troll.name
class Human(Character):
    affinity = "Magic"
    
    
    #Initialize Instance Attributes
    def __init__(self, name,class_1, class_nature):
        self.name = name
        self.class_1 = class_1
        self.class_nature = class_nature
        self.luck_stat = random.randint(0,10)
        self.Mana = 100
        self.dmg_mod = 1.0
        self.health = 100
        self.level = 1
        self.attack = 5
        self.coins = 20
    # Def normal attack
    def attack_bar(self,target):
        battle_menu=input("""What would you like to do\n
        \n[1]Normal attack (Base 5 dmg)
        \n[2]Fireball (Base 9 dmg,5 mana)
        \n[3]Pyroblast (Base 20 dmg, 15 mana)
        \n[4]Evocation (Mana + 50)
        \n>>""")
        if battle_menu == '1':
            self.normal_attack(target)
            if target.health > 0:
                print(f"{target.name} has {target.health} hp remaining")
        elif battle_menu =='2':
            self.fireball(target)
            if target.health > 0:
                print(f"{target.name} has {target.health} hp remaining")
        elif battle_menu == '3':
            self.Pyroblast(target)
            if target.health > 0:
                print(f"{target.name} has {target.health} hp remaining")
        elif battle_menu == '4':
            self.evocation()
            print(f"{self.name} has {self.Mana} mana points!")
        else:
            print("Please pick a spell")


    
    def normal_attack(self,target):
        attack = self.attack
        if self.luck_stat > 5 :
            attack += 2
            print(f"\n{self.name} has critically hit{target.name} for {attack}!")
            target.health = target.health - attack
            if target.health <= 0:
                self.coins += 5
                print(f"{target.name} has fallen!You have been rewarded {self.coins} coins")
                
        else :
            print(f"\n{self.name} has  hit {target.name} for {attack}!")
            target.health = target.health - attack
            print(f"\n{target.name} has {target.health} hp points")
            if target.health <= 0:
                self.coins += 5
                print(f"{target.name} has fallen!You have been rewarded {self.coins} coins")
        
    # Cast Fireball
    def fireball(self,target):
        if self.luck_stat > 3 :
            self.attack = 9
            self.attack += 7
            print("It's your lucky day!")
            print(f"Fireball dmg modifier increased by {self.dmg_mod} percent")
            
        if self.affinity == "Magic" and self.Mana >= 5 :
            self.attack = 9
            print("This should wake you up! Fireball!")
            print(f"{self.name} has hit {target.name} for {self.attack}")
            target.health -= self.attack
            self.Mana -= 5
            print(f"You have {self.Mana} mana left.")
            if target.health <= 0:
                self.coins += 5
                print(f"{target.name} has fallen!You have been rewarded {self.coins} coins")
            
        else :
            print("I don't have enough mana!")
    # Cast Pyroblast
    def Pyroblast(self,target):
        if self.luck_stat > 7 :
            self.attack = 20
            self.attack += 20
            print("It's your lucky day!")
            print(f"Pyroblast dmg modifier increased by {self.dmg_mod} percent")
        if self.affinity == "Magic" and self.Mana >= 15 :
            self.attack = 20
            print("Here comes the heat! PYROBLAST!!")
            print(f"{self.name} has hit {target.name} for {self.attack}")
            target.health -= self.attack
            self.Mana -= 15
            print(f"You have {self.Mana} mana left.")
            if target.health <= 0:
                self.coins += 5
                print(f"{target.name} has fallen!You have been rewarded {self.coins} coins")
        else :
            print("I don't have enough mana!")
    # Create a random generated integer for luck stat
    # def luck_stat(self):
    #     self
    # Create spell to restore mana
    def evocation(self):
        self.Mana += 30
        return self.Mana
    def alive(self):
        self.health > 0
        return self.health
    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

    def dead(self):
        self.health <= 0
        print ("You have fallen")
    
        
    def level_up(self,target):
        if target.health <= 0:
            self.level += 1
            return f"Congrats! {self.name} has leveled up to {self.level}"
        else:
            return False
    
            
class Orc(Character) :

    def __init__(self, name, class_1):
        self.name = name
        self.class_1 = class_1
        self.health = 30
        self.attack = 10
        self.luck_stat = random.randint(0,10)

    def normal_attack(self,target):
        attack = self.attack
        if self.health > 0:
            if self.luck_stat > 5 :
                attack += 2
                print(f"Orc has critically hit {target.name} for {attack}!")
                target.health = target.health - attack
                print(f"{target.name} has {target.health} hp points")
            else :
                print(f"Orc has  hit {target.name} for {attack}!")
                target.health = target.health - attack
                print(f"{target.name} has {target.health} hp points")
            if target.health <= 0:
                
                print(f"{target.name} has fallen!I break this game MWAHAHA!")
        
    def alive(self):
        if self.health > 0 :
            return True
        else: 
            print(f"{self.name} has {self.health} hp remaining")
            

    def dead(self):
        if self.health <= 0:
            return True
        else:
            return False
        

class Troll(Character):
    def __init__(self, name, class_1):
        self.name = name
        self.class_1 = class_1
        self.health = 75
        self.attack = 15
        self.luck_stat = random.randint(4,10)
    def normal_attack(self,target):
        attack = self.attack
        if self.health > 0:
            if self.luck_stat > 3 :
                attack *= 2
                print(f"Giant has critically hit{target.name} for {attack}!")
                target.health = target.health - attack
                if target.health > 0:
                    print(f"{target.name} has {target.health} hp points")
                elif target.health <= 0:
                    target.dead()
            else :
                print(f"Giant has  hit {target.name} for {attack}!")
                target.health = target.health - attack
                print(f"{target.name} has {target.health} hp points")
        
    def alive(self):
        if self.health > 0 :
            return True
        else: 
            print(f"{self.name} has {self.health} hp remaining")
            

    def dead(self):
        self.health <= 0
        return True
        print(f"{self.name} has {self.health} hp remaining")

        

class Zone:
    def __init__(self,name, weather):
        self.name = name
        self.weather = weather

    def grassy_buff(self, weather, target):
        if weather == "sunny":
            target.health += 15
            #target.power += 5
            return print(f"\n{target.name} hitpoints have increased by 15 to {target.health}.")
    def frejlord_buff(self, weather, target):
        if weather == "frostbite":
            print("Winters chills slowly freeze your body!")
            target.health -= 15
            target.attack -= 20
            return print(f"\n{target.name} hitpoints have decreased by 15 to {target.health}.\n{target.name} attackpoints have decreased by 20 to {target.attack}.")
           
class SmallRedPot(object):
    cost = 5
    name = " Small red potion"
    def apply(self, character):
        if character.health < 150:
            character.health += 15
        print("%s's health increased to %d." % (character.name, character.health))
        print("If that aint loveeee then I don't know what love is!")
class SmallBluePot(object):
    cost = 15
    name = " Small blue potion"
    def apply(self, character):
        character.Mana += 10
        print("%s's Mana increased to %d." % (character.name, character.Mana))
        print("If that aint loveeee then I don't know what love is!")
class Staff(object):
    cost = 99999999
    name = " Frost Kings Scepter"
    def apply(self, character):
        character.Mana += 100
        character.attack += 15
        print("The Scepter of the Great Frost King. It's power has been known to flash freeze entire kingdoms!")
        print("%s's Mana increased to %d. %s's Attack has incread to %d." % (character.name, character.Mana,character.attack))
class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, character):
        character.attack += 2
        print("%s's attack increased to %d." % (character.name, character.attack))        
class Store(object):
    items = [SmallRedPot, SmallBluePot, Sword]
    
    def do_shooping(self,Human):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print(f"You have {Human.coins} coins and {Human.name} has {Human.health} hitpoints with {Human.Mana} mana points and {Human.attack} battle power.") 
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                if Human.coins >= item.cost:
                    Human.buy(item)
                else:
                    print("Hey you! We don't supply the broke! Go kill some more Orcs then come see me!")


grassy_plains = Zone("Grassy Plains", "sunny")
winter = Zone("Santa Claus Home","snowy")









# Create Jaina
Jaina = Human("Jaina","High-Mage","Arcane magic")
#Create an enemy

Trundle = Troll("Frost Giant","Grunts")
scepter = Staff()
Hoochies_Shop = Store()


while Jaina.alive() > 0:
    user_input=input(f"""Hello {Jaina.name}!Would you like to
\n[1] Enter Dungeon
\n[2] Boss Room
\n[3] Visit Shop
\n[4]Do nothing
\n Please make a selection (1-4)>> """)
    
    if user_input == "1":
        print("\nEntering Grassy Plains!")
        grassy_plains.grassy_buff("sunny",Jaina)
        Green_Orc = Orc("Green Orc", "Peon")
        print(f"\nA {Green_Orc.name} has appeared and has {Green_Orc.health} health")
        Jaina.attack_bar(Green_Orc)
        Green_Orc.normal_attack(Jaina)
        while  Green_Orc.health > 0:
            Jaina.attack_bar(Green_Orc)
            Green_Orc.normal_attack(Jaina)
            
            if Green_Orc.dead() == True:
                print(f"{Green_Orc.name} has been defeated!")
                Hoochies_Shop.do_shooping(Jaina)
                break
            

        
    elif user_input == "2":
        print("\nEntering Frejlord")
        winter.frejlord_buff("frostbite",Jaina)
        Trundle = Troll("Frost Giant","Grunts")
        print(f"\nA {Trundle.name} has appeared and has {Trundle.health} health")
        Jaina.attack_bar(Trundle)
        Trundle.normal_attack(Jaina)
        while Trundle.health > 0:
            Jaina.attack_bar(Trundle)
            Trundle.normal_attack(Jaina)
            if Trundle.dead() == True:
                print(f"{Trundle.name} has been defeated!")
                scepter
                print(f"You have obtained frost giants scepter")
                Jaina.level_up(Trundle)
                Hoochies_Shop.do_shooping(Jaina)
            elif Jaina.health <= 0:
                Jaina.dead()
            
            else:   
                pass
    elif user_input == "3":
        print("""Welcome to Hoochies Shop of Miracles!
        \n If you got the cash we got the goods hehehe! 
        \n<(*-*<)""")
        Hoochies_Shop.do_shooping(Jaina)

        
    elif user_input == "4":
        break

    # if user_input == "1": 
    #     print("\nGoblin has spawned in Grassy Plains! ")
    #     print(f"\nA {Green_Orc.name} has appeared and has {Green_Orc.alive()} health")
    #     Green_Orc.normal_attack(Jaina)
    #     if Jaina.health <= 0:
    #         Jaina.dead()
    #     # AI attacks as well
