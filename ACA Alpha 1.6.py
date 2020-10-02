# -*- coding: utf-8 -*-

import sys
import os
import random
import pickle
import time

os.system('mode con: cols=200 lines=200')



#pygame.init()

#screen = pygame.display.set_mode((800,600))


# Title and Icon
#pygame.display.set_caption("Annual Conference Adventure 2020")
#icon = pygame.image.load("cross.png")
#pygame.display.set_icon(icon)

#Game Loop
#running = True
#while running:
   # for event in pygame.event.get():
       # if event.type == pygame.QUIT:
           #running = False



weapons = {"Bible": 40, "Voting Machine": 20, "Piping Hot Coffee": 25, "Old Man's Cane": 75, "Swag Bag": 175, "Fold Up Chair": 300, "Bishop's Staff": 750}





class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 40
        self.potions = 0
        self.exp = 0
        self.weap = ["Thoughts and Prayers"]
        self.curweap = ["Thoughts and Prayers"]
        self.max_faith = 20
        self.faith = 20
        self.base_magic = 15
        self.curspells = []
        self.deathcount = 0
        self.bosscount = 0
        self.attackboost = 0
        self.boostcount = 0
        self.storylist = ["store_first"]
        self.spell_list = []
        self.spell_list_battle = []


    @property
    def attack(self):
        attack = self.base_attack + self.attackboost
        if self.curweap == "Thoughts and Prayers":
            attack += 0
        if self.curweap == "Voting Machine":
            attack += 5
        if self.curweap == "Piping Hot Coffee":
            attack += 7
        if self.curweap == "Bible":
            attack += 10
        if self.curweap == "Old Man's Cane":
            attack += 30
        if self.curweap == "Swag Bag":
            attack += 50
        if self.curweap == "Fold Up Chair":
            attack += 75
        if self.curweap == "Bishop's Staff":
            attack += 100
        return attack

    @property
    def magic(self):
        magic = self.base_magic
        if self.curspells == "Benediction":
            magic += 5
        return magic





#Level 1 Beastiary

class Rural_Layperson:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 25
        self.health = self.maxhealth
        self.attack = 15
        self.goldgain = 7
        self.expgain = 5
Rural_LaypersonIG = Rural_Layperson("Rural Layperson")


class Rural_Clergy:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 30
        self.health = self.maxhealth
        self.attack = 10
        self.goldgain = 7
        self.expgain = 5
Rural_ClergyIG = Rural_Clergy("Rural Clergy")

#Level 2 Beastiary

class Young_Clergy:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 45
        self.health = self.maxhealth
        self.attack = 20
        self.goldgain = 15
        self.expgain = 10
Young_ClergyIG = Young_Clergy("Young Clergy")

class Book_of_Discipline:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 30
        self.goldgain = 15
        self.expgain = 20
Book_of_DisciplineIG = Book_of_Discipline("Book of Discipline")

class District_Administrator:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 30
        self.goldgain = 15
        self.expgain = 20
District_AdministratorIG = District_Administrator("District Administrator")

#Level 3 Beastiary

class District_Lay_Leader:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 75
        self.health = self.maxhealth
        self.attack = 50
        self.goldgain = 25
        self.expgain = 30
District_Lay_LeaderIG = District_Lay_Leader("District Lay Leader")


class Conference_Vote_Teller:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 75
        self.health = self.maxhealth
        self.attack = 50
        self.goldgain = 35
        self.expgain = 35
Conference_Vote_TellerIG = Conference_Vote_Teller("Conference Vote Teller")


class Youth_Delegate:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 50
        self.goldgain = 40
        self.expgain = 35
Youth_DelegateIG = Youth_Delegate("Youth Delegate")

#Level 4 Beastiary

class Tech_Booth_Guy:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 115
        self.health = self.maxhealth
        self.attack = 80
        self.goldgain = 75
        self.expgain = 60
Tech_Booth_GuyIG = Tech_Booth_Guy("Tech Booth Guy")

class Suburban_Layperson:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 120
        self.health = self.maxhealth
        self.attack = 75
        self.goldgain = 75
        self.expgain = 55
Suburban_LaypersonIG = Suburban_Layperson("Suburban Layperson")

class Suburban_Clergy:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 115
        self.health = self.maxhealth
        self.attack = 70
        self.goldgain = 75
        self.expgain = 50
Suburban_ClergyIG = Suburban_Clergy("Suburban Clergy")

# Level 5 Beastiary

class Possessed_Voting_Ballot:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 200
        self.health = self.maxhealth
        self.attack = 90
        self.goldgain = 135
        self.expgain = 90
Possessed_Voting_BallotIG = Possessed_Voting_Ballot("Possessed Voting Ballot")

class Retired_Clergy:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 175
        self.health = self.maxhealth
        self.attack = 100
        self.goldgain = 125
        self.expgain = 100
Retired_ClergyIG = Retired_Clergy("Retired Clergy")

class Retired_Clergy_Book_Collection:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 175
        self.health = self.maxhealth
        self.attack = 100
        self.goldgain = 120
        self.expgain = 105
Retired_Clergy_Book_CollectionIG = Retired_Clergy("Retired Clergy")


#Level 6 Beastiary

class Fallen_Calvinist_Spirit:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 90
        self.goldgain = 120
        self.expgain = 100
Fallen_Calvinist_SpiritIG = Fallen_Calvinist_Spirit("Fallen Calvinist Spirit")

class Calvinist_Assistant:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 90
        self.goldgain = 120
        self.expgain = 100
Calvinist_AssistantIG = Calvinist_Assistant("Calvinist Spirit")

class District_Superintendent:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 120
        self.health = self.maxhealth
        self.attack = 90
        self.goldgain = 150
        self.expgain = 150
District_SuperintendentIG = District_Superintendent("District Superintendent")


#Bosses

class Total_Depravity:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 25
        self.goldgain = 50
        self.expgain = 25
Total_DepravityIG = Total_Depravity("Total Depravity")

class Unconditional_Election:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 55
        self.goldgain = 100
        self.expgain = 75
Unconditional_ElectionIG = Unconditional_Election("Unconditional Election")

class Limited_Atonement:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 200
        self.health = self.maxhealth
        self.attack = 90
        self.goldgain = 175
        self.expgain = 125
Limited_AtonementIG = Limited_Atonement("Limited Atonement")

class Irresistable_Grace:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 300
        self.health = self.maxhealth
        self.attack = 150
        self.goldgain = 300
        self.expgain = 175
Irresistable_GraceIG = Irresistable_Grace("Irresistable Grace")

class Saintly_Preservation:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 500
        self.health = self.maxhealth
        self.attack = 200
        self.goldgain = 500
        self.expgain = 200
Saintly_PreservationIG = Saintly_Preservation("Saintly Preservation")

class Spirit_of_John_Calvin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 1000
        self.health = self.maxhealth
        self.attack = 250
        self.goldgain = 1000
        self.expgain = 1000
Spirit_of_John_CalvinIG = Spirit_of_John_Calvin("Spirit of John Calvin")








#def opening_sequence():
    #opening_message = "Every year, Methodists from around the world gather for an annual meeting of the minds.\nEssentially, these meetings are infomercials for why you should pay apportionments and the actual business only takes about an hour.\n" \
          #"And yet...we gather....but this year...things are different...this year...a conspiracy is afoot.\n"
    #for character in opening_message:
        #sys.stdout.write(character)
        #sys.stdout.flush()
        #time.sleep(0.08)
    #main()



def main():
    os.system('cls')
    print"   _____                                   .__   " + "_________                _____                                          "
    print"  /  _  \   ____  __ __  ____  __ _______  |  |  " + " \_   ___ \  ____   _____/ ____\___________   ____   ____   ____  ____  "
    print" /  /_\  \ /    \|  |  \/    \|  |  \__  \ |  |  " + " /    \  \/ /  _ \ /    \   __\/ __ \_  __ \_/ __ \ /    \_/ ___\/ __ \ "
    print"/    |    \   |  \  |  /   |  \  |  // __ \|  |__" + "\     \___(  <_> )   |  \  | \  ___/|  | \/\  ___/|   |  \  \__\  ___/  "
    print"\____|__  /___|  /____/|___|  /____/(____  /____/" + " \______  /\____/|___|  /__|  \___  >__|    \___  >___|  /\___  >___  > "
    print"        \/     \/           \/           \/      " + "        \/            \/          \/            \/     \/     \/    \/ "
    print"                            _____       .___                    __                       "
    print"                           /  _  \    __| _/__  __ ____   _____/  |_ __ _________   ____ "
    print"                          /  /_\  \  / __ |\  \/ // __ \ /    \   __\  |  \_  __ \_/ __ \ "
    print"                         /    |    \/ /_/ | \   /\  ___/|   |  \  | |  |  /|  | \/\  ___/ "
    print"                         \____|__  /\____ |  \_/  \___  >___|  /__| |____/ |__|    \___  >"
    print"                                 \/      \/           \/     \/                        \/ "

    print "\n"
    print "                                              Pre Alpha 1.7                                \n"
    print "                                            Presented by PyRev                       \n"
    print("                                           1.) Start New Game              ")
    print("                                           2.) Load                        ")
    print("                                           3.) Exit                        ")
    option = raw_input("-> ")
    if option.strip() == "1":
        start()
    elif option.strip() == "2":
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open("savefile", "rb") as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print "Loaded save state...your journey onto perfection continues!"
            option = raw_input("-> ")
            start1()
        else:
            print "You have no saved data...and no salvation"
            option = raw_input("-> ")
        main()
    elif option.strip() == "3":
        sys.exit()
    else:
        main()


def start():
    os.system('cls')
    print "Hello, what is your name?"
    option = raw_input("-> ")
    global PlayerIG
    PlayerIG = Player(option)
    game_instructions()

def start1():
    os.system('cls')
    print "Hello, %s how are you?" % PlayerIG.name
    print "Player Items and Stats"
    print "Attack: %d" % PlayerIG.attack
    print "Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth)
    print "Current Weapon: %s" % PlayerIG.curweap
    print "Gold: %g" % PlayerIG.gold
    print "Potions: %d" % PlayerIG.potions
    print "Faith: %s" % PlayerIG.faith
    print "Experience Points: %s\n" % PlayerIG.exp
    print "1.) Fight"
    print "2.) Store"
    print "3.) Save"
    print "4.) Exit"
    print "5.) Inventory"
    print "6.) Continue Story"
    print "7.) Rest"
    option = raw_input("-> ")
    if option.strip() == "1":
        prefight()
    elif option.strip() == "2":
        if "store_first" in PlayerIG.storylist:
            storeintro()
        store()
    elif option.strip() == "3":
        with open('savefile', 'wb') as f:
             pickle.dump(PlayerIG, f)
             print "\n Game has been saved! And so has your soul!\n"
        option = raw_input("-> ")
        start1()
    elif option.strip() == "4":
        sys.exit()
    elif option.strip() == "5":
        inventory()
    elif option.strip() == "6":
        if PlayerIG.exp >= 25 and "Story 1" in PlayerIG.storylist:
            story201()
        elif PlayerIG.exp >= 25 and "Story 1.1" in PlayerIG.storylist:
            bossfight1()
        elif PlayerIG.exp >= 200 and "Story 2" in PlayerIG.storylist:
            story301()
        elif PlayerIG.exp >= 200 and "Story 2.1" in PlayerIG.storylist:
            bossfight2()
        elif PlayerIG.exp >= 600 and "Story 3" in PlayerIG.storylist:
            story401()
        elif PlayerIG.exp >= 600 and "Story 3.1" in PlayerIG.storylist:
            bossfight3()
        elif PlayerIG.exp >= 1500 and "Story 4" in PlayerIG.storylist:
            story501()
        elif PlayerIG.exp >= 1500 and "Story 4.1" in PlayerIG.storylist:
            bossfight4()
        elif PlayerIG.exp >= 3000 and "Story 5" in PlayerIG.storylist:
            story601()
        elif PlayerIG.exp >= 3000 and "Story 5.1" in PlayerIG.storylist:
            bossfight5()
        elif PlayerIG.exp >= 5000 and "Story 6" in PlayerIG.storylist:
            story701()
        elif PlayerIG.exp >= 5000 and "Story 6.1" in PlayerIG.storylist:
            finalboss()
        else:
            if PlayerIG.bosscount == 0:
                print "You cannot continue the story just yet, get " + str(25 - PlayerIG.exp) + " more exp and come back!"
            elif PlayerIG.bosscount == 1:
                print "You cannot continue the story just yet, get " + str(200 - PlayerIG.exp) + " more exp and come back!"
            elif PlayerIG.bosscount == 2:
                print "You cannot continue the story just yet, get " + str(600 - PlayerIG.exp) + " more exp and come back!"
            elif PlayerIG.bosscount == 3:
                print "You cannot continue the story just yet, get " + str(1500 - PlayerIG.exp) + " more exp and come back!"
            elif PlayerIG.bosscount == 4:
                print "You cannot continue the story just yet, get " + str(3000 - PlayerIG.exp) + " more exp and come back!"
            elif PlayerIG.bosscount == 5:
                print "You cannot continue the story just yet, get " + str(5000 - PlayerIG.exp) + " more exp and come back!"
            option = raw_input("-> ")
            start1()
    elif option.strip() == "7":
        rest_init()
    else:
        start1()


def rest_init():
    if "Story 1" in PlayerIG.storylist:
        print "Resting will cost 10 gold. Would you like to rest?"
        print "1.) Yes"
        print "2.) No"
        print "Enter 'b' to go back"
        option = raw_input("-> ")
        if option == "1":
            rest()
        if option == "2":
            start1()
        if option == "b":
            start1()
        else:
            rest_init()
    if "Story 2" in PlayerIG.storylist:
        print "Resting will cost 20 gold. Would you like to rest?"
        print "1.) Yes"
        print "2.) No"
        print "Enter 'b' to go back"
        option = raw_input("-> ")
        if option == "1":
            rest()
        if option == "2":
            start1()
        if option == "b":
            start1()
        else:
            rest_init()
    if "Story 3" in PlayerIG.storylist:
        print "Resting will cost 75 gold. Would you like to rest?"
        print "1.) Yes"
        print "2.) No"
        print "Enter 'b' to go back"
        option = raw_input("-> ")
        if option == "1":
            rest()
        if option == "2":
            start1()
        if option == "b":
            start1()
        else:
            rest_init()
    if "Story 4" in PlayerIG.storylist:
        print "Resting will cost 150 gold. Would you like to rest?"
        print "1.) Yes"
        print "2.) No"
        print "Enter 'b' to go back"
        option = raw_input("-> ")
        if option == "1":
            rest()
        if option == "2":
            start1()
        if option == "b":
            start1()
        else:
            rest_init()
    if "Story 5" in PlayerIG.storylist:
        print "Resting will cost 300 gold. Would you like to rest?"
        print "1.) Yes"
        print "2.) No"
        print "Enter 'b' to go back"
        option = raw_input("-> ")
        if option == "1":
            rest()
        if option == "2":
            start1()
        if option == "b":
            start1()
        else:
            rest_init()
    if "Story 6" in PlayerIG.storylist:
        print "Resting will cost 500 gold. Would you like to rest?"
        print "1.) Yes"
        print "2.) No"
        print "Enter 'b' to go back"
        option = raw_input("-> ")
        if option == "1":
            rest()
        if option == "2":
            start1()
        if option == "b":
            start1()
        else:
            rest_init()





def rest():
    if "Story 1" in PlayerIG.storylist and PlayerIG.gold >= 10:
        print "You have paid 10 gold, and you have restored your health!"
        PlayerIG.gold -= 10
        PlayerIG.health += 10000
        if PlayerIG.health >= PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.faith += 1000
        if PlayerIG.faith >= PlayerIG.max_faith:
            PlayerIG.faith = PlayerIG.max_faith
        option = raw_input("-> ")
        start1()

    elif "Story 2" in PlayerIG.storylist and PlayerIG.gold >= 20:
        print "You have paid 20 gold, and you have restored your health!"
        PlayerIG.gold -= 20
        PlayerIG.health += 10000
        if PlayerIG.health >= PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.faith += 1000
        if PlayerIG.faith >= PlayerIG.max_faith:
            PlayerIG.faith = PlayerIG.max_faith
        option = raw_input("-> ")
        start1()
    elif "Story 3" in PlayerIG.storylist and PlayerIG.gold >= 75:
        print "You have paid 75 gold, and you have restored your health!"
        PlayerIG.gold -= 75
        PlayerIG.health += 10000
        if PlayerIG.health >= PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.faith += 1000
        if PlayerIG.faith >= PlayerIG.max_faith:
            PlayerIG.faith = PlayerIG.max_faith
        option = raw_input("-> ")
        start1()
    elif "Story 4" in PlayerIG.storylist and PlayerIG.gold >= 150:
        print "You have paid 150 gold, and you have restored your health!"
        PlayerIG.gold -= 150
        PlayerIG.health += 10000
        if PlayerIG.health >= PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.faith += 1000
        if PlayerIG.faith >= PlayerIG.max_faith:
            PlayerIG.faith = PlayerIG.max_faith
        option = raw_input("-> ")
        start1()
    elif "Story 5" in PlayerIG.storylist and PlayerIG.gold >= 300:
        print "You have paid 300 gold, and you have restored your health!"
        PlayerIG.gold -= 300
        PlayerIG.health += 10000
        if PlayerIG.health >= PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.faith += 1000
        if PlayerIG.faith >= PlayerIG.max_faith:
            PlayerIG.faith = PlayerIG.max_faith
        option = raw_input("-> ")
        start1()
    elif "Story 6" in PlayerIG.storylist and PlayerIG.gold >= 500:
        print "You have paid 500 gold, and you have restored your health!"
        PlayerIG.gold -= 500
        PlayerIG.health += 10000
        if PlayerIG.health >= PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.faith += 1000
        if PlayerIG.faith >= PlayerIG.max_faith:
            PlayerIG.faith = PlayerIG.max_faith
        option = raw_input("-> ")
        start1()
    else:
        print "You do not have the resources to rest!"
        start1()



def inventory():
    print "You open your fair trade backpack."
    print "What do you want to do?"
    print "1.) Equip Weapon"
    print "2.) Look at Spells"
    print "b.) Back"
    option = raw_input("-> ")
    if option.strip() == "1":
        equip()
    if option.strip() == "2":
        print PlayerIG.spell_list
        print "Type b to go Back"
        option = raw_input("-> ")
        if option == "b":
            inventory()
        else:
            inventory()
    elif option.strip() == "b":
        start1()
    else:
        print "Invalid response"
        inventory()


def equip():
    print "What would you like to equip?"
    for weapon in PlayerIG.weap:
        print weapon
    print "Type 'b' to go back"
    option = raw_input("-> ")
    if option.strip() == "b":
        inventory()
    elif option.strip() == PlayerIG.curweap:
        print "You already have that equipped."
        option = raw_input("-> ")
        equip()
    elif option in PlayerIG.weap:
        PlayerIG.curweap = option
        print "You have equipped  %s" % option
        option = raw_input("-> ")
        start1()
    else:
         print "You don't have %s in your inventory" % option







def prefight():
    global enemy
    if "Story 1" in PlayerIG.storylist:
        enemynum = random.randint(1, 2)
        if enemynum == 1:
            enemy = Rural_LaypersonIG
            fight()
        else:
             enemy = Rural_ClergyIG
             fight()
    if "Story 2" in PlayerIG.storylist:
        enemynum2 = random.randint(1, 3)
        if enemynum2 == 1:
            enemy = Young_ClergyIG
            fight()
        elif enemynum2 == 2:
            enemy = Book_of_DisciplineIG
            fight()
        else:
            enemy = District_AdministratorIG
            fight()
    if "Story 3" in PlayerIG.storylist:
        enemynum3 = random.randint(1, 3)
        if enemynum3 == 1:
            enemy = District_Lay_LeaderIG
            fight()
        elif enemynum3 == 2:
            enemy = Conference_Vote_TellerIG
            fight()
        else:
            enemy = Youth_DelegateIG
            fight()
    if "Story 4" in PlayerIG.storylist:
        enemynum4 = random.randint(1, 3)
        if enemynum4 == 1:
            enemy = Tech_Booth_GuyIG
            fight()
        elif enemynum4 == 2:
            enemy = Suburban_LaypersonIG
            fight()
        else:
            enemy = Suburban_ClergyIG
            fight()
    if "Story 5" in PlayerIG.storylist:
        enemynum5 = random.randint(1, 3)
        if enemynum5 == 1:
            enemy = Possessed_Voting_BallotIG
            fight()
        elif enemynum5 == 2:
            enemy = Retired_ClergyIG
            fight()
        else:
            enemy = Retired_Clergy_Book_CollectionIG
            fight()
    if "Story 6" in PlayerIG.storylist:
        enemynum6 = random.randint(1, 3)
        if enemynum6 == 1:
            enemy = Fallen_Calvinist_SpiritIG
            fight()
        elif enemynum6 == 2:
            enemy = Calvinist_AssistantIG
            fight()
        else:
            enemy = District_SuperintendentIG
            fight()







def fight():
    os.system('cls')
    print ("%s is approached by a %s") % (PlayerIG.name, enemy.name)
    print "%s's Health: %s/%s   %s's Health %s/%s" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
    print ("Potions: %i") % PlayerIG.potions
    print "1.) Attack"
    print "2.) Cast Spell"
    print "3.) Drink Potion"
    print "4.) Run"
    option = raw_input('-> ')
    if option.strip() == "1":
        attack()
    elif option.strip() == "2":
        spells()
    elif option.strip() == "3":
        drinkpot()
    elif option.strip() == "4":
        run()
    else:
        fight()



def spells():
    print "What spell would you like to cast?"
    print "You have %s faith points" % PlayerIG.faith
    print "Type 'b' to return to previous menu.\n"
    print spell_list_battle
    option = raw_input("-> ")
    if option.lower() == "benediction" and "Benediction" in PlayerIG.spell_list:
        if PlayerIG.faith >= 10:
            cast_benediction()
    if option.lower() == "melodramatic speech" and "Melodramatic Speech" in PlayerIG.spell_list:
        if PlayerIG.faith >= 30:
            cast_melodramaspeech()
    if option.lower() == "call to question" and "Call to Question" in PlayerIG.spell_list:
        if PlayerIG.faith >= 100:
            cast_call_question()
    if option.lower() == "regeneration" and "Regeneration" in PlayerIG.spell_list:
        if PlayerIG.faith >= 10:
            cast_regeneration()
    if option.lower() == "pastoral prayer" and "Pastoral Prayer" in PlayerIG.spell_list:
        if PlayerIG.faith >= 30:
            cast_pastoral_prayer()
    if option.lower() == "baptismal remembrance" and "Baptismal Remembrance" in PlayerIG.spell_list:
        if PlayerIG.faith >= 100:
            cast_baptismal_remembrance()
    if option.lower() == "prevenient grace" and "Prevenient Grace" in PlayerIG.spell_list and PlayerIG.boostcount == 0:
        if PlayerIG.faith >= 10:
            cast_prevenient_grace()
    if option.lower() == "justifying grace" and "Justifying Grace" in PlayerIG.spell_list and PlayerIG.boostcount == 0:
        if PlayerIG.faith >= 30:
            cast_justifying_grace()
    if option.lower() == 'sanctifying grace' and "Sanctifying Grace" in PlayerIG.spell_list and PlayerIG.boostcount == 0:
        if PlayerIG.faith >= 100:
            cast_sanctifying_grace()
    if option == "b":
        fight()
    else:
        print "You don't have enough faith!"
        spells()


def boss_spells():
    print "What spell would you like to cast?"
    print "You have %s faith points" % PlayerIG.faith
    print "Type 'b' to return to previous menu.\n"
    print spell_list_battle
    option = raw_input("-> ")
    if option.lower() == "benediction" and "Benediction" in PlayerIG.spell_list:
        if PlayerIG.faith >= 10:
            cast_benediction_boss()
    if option.lower() == "melodramatic speech" and "Melodramatic Speech" in PlayerIG.spell_list:
        if PlayerIG.faith >= 30:
            cast_melodramaspeech_boss()
    if option.lower() == "call to question" and "Call to Question" in PlayerIG.spell_list:
        if PlayerIG.faith >= 100:
            cast_callquestion_boss()
    if option.lower() == "regeneration" and "Regeneration" in PlayerIG.spell_list:
        if PlayerIG.faith >= 10:
            cast_regeneration_boss()
    if option.lower() == "pastoral prayer" and "Pastoral Prayer" in PlayerIG.spell_list:
        if PlayerIG.faith >= 30:
            cast_pastoralprayer_boss()
    if option.lower() == "baptismal remembrance" and "Baptismal Remembrance" in PlayerIG.spell_list:
        if PlayerIG.faith >= 100:
            cast_baptismal_remembrance_boss()
    if option.lower() == "prevenient grace" and "Prevenient Grace" in PlayerIG.spell_list:
        if PlayerIG.faith >= 10:
            cast_prevenientgrace_boss()
    if option.lower() == "justifying grace" and "Justifying Grace" in PlayerIG.spell_list:
        if PlayerIG.faith >= 30:
            cast_justifyinggrace_boss()
    if option.lower() == 'sanctifying grace' and "Sanctifying Grace" in PlayerIG.spell_list:
        if PlayerIG.faith >= 100:
            cast_sanctifyinggrace_boss()
        else:
            print "You don't have enough faith or you haven't unlocked that spell!"
            if "Boss 1" in PlayerIG.storylist:
                bossfight1()
            elif "Boss 2" in PlayerIG.storylist:
                bossfight2()
            elif "Boss 3" in PlayerIG.storylist:
                bossfight3()
            elif "Boss 4" in PlayerIG.storylist:
                bossfight4()
            elif "Boss 5" in PlayerIG.storylist:
                bossfight5()
            elif "Boss 6" in PlayerIG.storylist:
                finalboss()
            else:
                boss_spells()
    elif option == "b":
        if "Boss 1" in PlayerIG.storylist:
            bossfight1()
        elif "Boss 2" in PlayerIG.storylist:
            bossfight2()
        elif "Boss 3" in PlayerIG.storylist:
            bossfight3()
        elif "Boss 4" in PlayerIG.storylist:
            bossfight4()
        elif "Boss 5" in PlayerIG.storylist:
            bossfight5()
        elif "Boss 6" in PlayerIG.storylist:
            finalboss()
        else:
            boss_spells()
    else:
        boss_spells()



#Regular Damage Spell Casts


def cast_benediction():
    benedictionattack = random.randint(PlayerIG.magic / 2, PlayerIG.magic)
    PlayerIG.faith -= 10
    enemy.health -= benedictionattack
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    print "Benediction does %d points of damage" % benedictionattack
    option = raw_input("-> ")
    if enemy.health <= 0:
        win()
        os.system('clear')
    if EAttack == enemy.attack / 2:
        print "The enemy missed!"
        option = raw_input('-> ')
        fight()
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')







        fight()


def cast_melodramaspeech():
    melodramaattack = random.randint(PlayerIG.magic * 2 / 2, PlayerIG.magic)
    PlayerIG.faith -= 30
    enemy.health -= melodramaattack
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    print "Melodramatic Speech does %d points of damage" % melodramaattack
    option = raw_input("-> ")
    if enemy.health <= 0:
        win()
        os.system('clear')
    if EAttack == enemy.attack / 2:
        print "The enemy missed!"
        option = raw_input('-> ')
        fight()
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
        fight()



def cast_call_question():
    callquestionattack = random.randint(PlayerIG.magic * 3 / 2, PlayerIG.magic)
    PlayerIG.faith -= 100
    enemy.health -= callquestionattack
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    print "Call to Question does %d points of damage" % callquestionattack
    option = raw_input("-> ")
    if enemy.health <= 0:
        win()
        os.system('clear')
    if EAttack == enemy.attack / 2:
        print "The enemy missed!"
        option = raw_input('-> ')
        fight()
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
        fight()


#Regular Heal Spell Casts

def cast_regeneration():
    os.system('cls')
    print "Regeneration has healed 30 hp!"
    option = raw_input("-> ")
    PlayerIG.health += 50
    PlayerIG.faith -= 10
    if PlayerIG.health > PlayerIG.maxhealth:
        PlayerIG.health = PlayerIG.maxhealth
    fight()


def cast_pastoral_prayer():
    os.system('cls')
    print "Pastoral Prayer has healed 100 hp!"
    option = raw_input("-> ")
    PlayerIG.health += 100
    PlayerIG.faith -= 30
    if PlayerIG.health > PlayerIG.maxhealth:
        PlayerIG.health = PlayerIG.maxhealth
    fight()



def cast_baptismal_remembrance():
    os.system('cls')
    print "Pastoral Prayer has healed 250 hp!"
    option = raw_input("-> ")
    PlayerIG.health += 250
    PlayerIG.faith -= 100
    if PlayerIG.health > PlayerIG.maxhealth:
        PlayerIG.health = PlayerIG.maxhealth
    fight()

#Regular Buff Spell Casts

def cast_prevenient_grace():
    os.system('cls')
    print "Your attack has been temporarily buffed!"
    option = raw_input("-> ")
    PlayerIG.attackboost += 10
    PlayerIG.faith -= 10
    PlayerIG.boostcount += 1
    fight()


def cast_justifying_grace():
    os.system('cls')
    print "Your attack has been temporarily and moderately buffed!"
    option = raw_input("-> ")
    PlayerIG.attackboost += 30
    PlayerIG.faith -= 30
    PlayerIG.boostcount += 1
    fight()


def cast_sanctifying_grace():
    os.system('cls')
    print "Your attack has been temporarily and majorly buffed!"
    option = raw_input("-> ")
    PlayerIG.attackboost += 100
    PlayerIG.faith -= 100
    PlayerIG.boostcount += 1
    fight()


#Boss Damaging Spells

def cast_benediction_boss():
    if "Boss 1" in PlayerIG.storylist:
        enemy = Total_DepravityIG
    elif "Boss 2" in PlayerIG.storylist:
        enemy = Unconditional_ElectionIG
    elif "Boss 3" in PlayerIG.storylist:
        enemy = Limited_AtonementIG
    elif "Boss 4" in PlayerIG.storylist:
        enemy = Irresistable_GraceIG
    elif "Boss 5" in PlayerIG.storylist:
        enemy = Saintly_PreservationIG
    elif "Boss 6" in PlayerIG.storylist:
        enemy = Spirit_of_John_CalvinIG
    benedictionattack = random.randint(PlayerIG.magic / 2, PlayerIG.magic)
    PlayerIG.faith -= 10
    enemy.health -= benedictionattack
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    print "Benediction does %d points of damage" % benedictionattack
    option = raw_input("-> ")
    if enemy.health <= 0:
        if "Boss 1" in PlayerIG.storylist:
            bosswin1()
        if "Boss 2" in PlayerIG.storylist:
            bosswin2()
        if "Boss 3" in PlayerIG.storylist:
            bosswin3()
        if "Boss 4" in PlayerIG.storylist:
            bosswin4()
        if "Boss 5" in PlayerIG.storylist:
            bosswin5()
        if "Boss 6" in PlayerIG.storylist:
            finalbosswin()
    if EAttack == enemy.attack / 2:
        print "The enemy missed!"
        if "Boss 1" in PlayerIG.storylist:
            bossfight1()
        if "Boss 2" in PlayerIG.storylist:
            bossfight2()
        if "Boss 3" in PlayerIG.storylist:
            bossfight3()
        if "Boss 4" in PlayerIG.storylist:
            bossfight4()
        if "Boss 5" in PlayerIG.storylist:
            bossfight5()
        if "Boss 6" in PlayerIG.storylist:
            finalboss()
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
        if "Boss 1" in PlayerIG.storylist:
            bossfight1()
        if "Boss 2" in PlayerIG.storylist:
            bossfight2()
        if "Boss 3" in PlayerIG.storylist:
            bossfight3()
        if "Boss 4" in PlayerIG.storylist:
            bossfight4()
        if "Boss 5" in PlayerIG.storylist:
            bossfight5()
        if "Boss 6" in PlayerIG.storylist:
            finalboss()


def cast_melodramaspeech_boss():
    if "Boss 1" in PlayerIG.storylist:
        enemy = Total_DepravityIG
    elif "Boss 2" in PlayerIG.storylist:
        enemy = Unconditional_ElectionIG
    elif "Boss 3" in PlayerIG.storylist:
        enemy = Limited_AtonementIG
    elif "Boss 4" in PlayerIG.storylist:
        enemy = Irresistable_GraceIG
    elif "Boss 5" in PlayerIG.storylist:
        enemy = Saintly_PreservationIG
    elif "Boss 6" in PlayerIG.storylist:
        enemy = Spirit_of_John_CalvinIG
    melodramaattack = random.randint(PlayerIG.magic * 2 / 2, PlayerIG.magic)
    PlayerIG.faith -= 10
    enemy.health -= melodramaattack
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    print "Melodramatic Speech does %d points of damage" % melodramaattack
    option = raw_input("-> ")
    if enemy.health <= 0:
        if "Boss 1" in PlayerIG.storylist:
            bosswin1()
        if "Boss 2" in PlayerIG.storylist:
            bosswin2()
        if "Boss 3" in PlayerIG.storylist:
            bosswin3()
        if "Boss 4" in PlayerIG.storylist:
            bosswin4()
        if "Boss 5" in PlayerIG.storylist:
            bosswin5()
        if "Boss 6" in PlayerIG.storylist:
            finalbosswin()
    if EAttack == enemy.attack / 2:
        print "The enemy missed!"
        if "Boss 1" in PlayerIG.storylist:
            bossfight1()
        if "Boss 2" in PlayerIG.storylist:
            bossfight2()
        if "Boss 3" in PlayerIG.storylist:
            bossfight3()
        if "Boss 4" in PlayerIG.storylist:
            bossfight4()
        if "Boss 5" in PlayerIG.storylist:
            bossfight5()
        if "Boss 6" in PlayerIG.storylist:
            finalboss()
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
        if "Boss 1" in PlayerIG.storylist:
            bossfight1()
        if "Boss 2" in PlayerIG.storylist:
            bossfight2()
        if "Boss 3" in PlayerIG.storylist:
            bossfight3()
        if "Boss 4" in PlayerIG.storylist:
            bossfight4()
        if "Boss 5" in PlayerIG.storylist:
            bossfight5()
        if "Boss 6" in PlayerIG.storylist:
            finalboss()


def cast_callquestion_boss():
    if "Boss 1" in PlayerIG.storylist:
        enemy = Total_DepravityIG
    elif "Boss 2" in PlayerIG.storylist:
        enemy = Unconditional_ElectionIG
    elif "Boss 3" in PlayerIG.storylist:
        enemy = Limited_AtonementIG
    elif "Boss 4" in PlayerIG.storylist:
        enemy = Irresistable_GraceIG
    elif "Boss 5" in PlayerIG.storylist:
        enemy = Saintly_PreservationIG
    elif "Boss 6" in PlayerIG.storylist:
        enemy = Spirit_of_John_CalvinIG
    callquestionattack = random.randint(PlayerIG.magic * 3 / 2, PlayerIG.magic)
    PlayerIG.faith -= 10
    enemy.health -= callquestionattack
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    print "Call To Question does %d points of damage!" % callquestionattack
    option = raw_input("-> ")
    if enemy.health <= 0:
        if "Boss 1" in PlayerIG.storylist:
            bosswin1()
        if "Boss 2" in PlayerIG.storylist:
            bosswin2()
        if "Boss 3" in PlayerIG.storylist:
            bosswin3()
        if "Boss 4" in PlayerIG.storylist:
            bosswin4()
        if "Boss 5" in PlayerIG.storylist:
            bosswin5()
        if "Boss 6" in PlayerIG.storylist:
            finalbosswin()
    if EAttack == enemy.attack / 2:
        print "The enemy missed!"
        if "Boss 1" in PlayerIG.storylist:
            bossfight1()
        if "Boss 2" in PlayerIG.storylist:
            bossfight2()
        if "Boss 3" in PlayerIG.storylist:
            bossfight3()
        if "Boss 4" in PlayerIG.storylist:
            bossfight4()
        if "Boss 5" in PlayerIG.storylist:
            bossfight5()
        if "Boss 6" in PlayerIG.storylist:
            finalboss()
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
        if "Boss 1" in PlayerIG.storylist:
            bossfight1()
        if "Boss 2" in PlayerIG.storylist:
            bossfight2()
        if "Boss 3" in PlayerIG.storylist:
            bossfight3()
        if "Boss 4" in PlayerIG.storylist:
            bossfight4()
        if "Boss 5" in PlayerIG.storylist:
            bossfight5()
        if "Boss 6" in PlayerIG.storylist:
            finalboss()


#Boss Heal Casts

def cast_regeneration_boss():
    os.system('cls')
    print "Regeneration has healed 30 hp!"
    option = raw_input("-> ")
    PlayerIG.health += 30
    PlayerIG.faith -= 10
    if PlayerIG.health > PlayerIG.maxhealth:
        PlayerIG.health = PlayerIG.maxhealth
    if "Boss 1" in PlayerIG.storylist:
        bossfight1()
    if "Boss 2" in PlayerIG.storylist:
        bossfight2()
    if "Boss 3" in PlayerIG.storylist:
        bossfight3()
    if "Boss 4" in PlayerIG.storylist:
        bossfight4()
    if "Boss 5" in PlayerIG.storylist:
        bossfight5()
    if "Boss 6" in PlayerIG.storylist:
        finalboss()


def cast_pastoralprayer_boss():
    os.system('cls')
    print "Pastoral Prayer has healed 100 hp!"
    option = raw_input("-> ")
    PlayerIG.health += 100
    PlayerIG.faith -= 30
    if PlayerIG.health > PlayerIG.maxhealth:
        PlayerIG.health = PlayerIG.maxhealth
    if "Boss 1" in PlayerIG.storylist:
        bossfight1()
    if "Boss 2" in PlayerIG.storylist:
        bossfight2()
    if "Boss 3" in PlayerIG.storylist:
        bossfight3()
    if "Boss 4" in PlayerIG.storylist:
        bossfight4()
    if "Boss 5" in PlayerIG.storylist:
        bossfight5()
    if "Boss 6" in PlayerIG.storylist:
        finalboss()

def cast_baptismal_remembrance_boss():
    os.system('cls')
    print "Baptismal Remembrance has healed 250 hp!"
    option = raw_input("-> ")
    PlayerIG.health += 250
    PlayerIG.faith -= 100
    if PlayerIG.health > PlayerIG.maxhealth:
        PlayerIG.health = PlayerIG.maxhealth
    if "Boss 1" in PlayerIG.storylist:
        bossfight1()
    if "Boss 2" in PlayerIG.storylist:
        bossfight2()
    if "Boss 3" in PlayerIG.storylist:
        bossfight3()
    if "Boss 4" in PlayerIG.storylist:
        bossfight4()
    if "Boss 5" in PlayerIG.storylist:
        bossfight5()
    if "Boss 6" in PlayerIG.storylist:
        finalboss()


#Boss Buff Casts

def cast_prevenientgrace_boss():
    os.system('cls')
    print "Your attack has been temporarily buffed!"
    option = raw_input("-> ")
    PlayerIG.attackboost += 10
    PlayerIG.faith -= 10
    PlayerIG.boostcount += 1
    if "Boss 1" in PlayerIG.storylist:
        bossfight1()
    if "Boss 2" in PlayerIG.storylist:
        bossfight2()
    if "Boss 3" in PlayerIG.storylist:
        bossfight3()
    if "Boss 4" in PlayerIG.storylist:
        bossfight4()
    if "Boss 5" in PlayerIG.storylist:
        bossfight5()
    if "Boss 6" in PlayerIG.storylist:
        finalboss()


def cast_justifyinggrace_boss():
    os.system('cls')
    print "Your attack has been temporarily moderately buffed!"
    option = raw_input("-> ")
    PlayerIG.attackboost += 30
    PlayerIG.faith -= 30
    PlayerIG.boostcount += 1
    if "Boss 1" in PlayerIG.storylist:
        bossfight1()
    if "Boss 2" in PlayerIG.storylist:
        bossfight2()
    if "Boss 3" in PlayerIG.storylist:
        bossfight3()
    if "Boss 4" in PlayerIG.storylist:
        bossfight4()
    if "Boss 5" in PlayerIG.storylist:
        bossfight5()
    if "Boss 6" in PlayerIG.storylist:
        finalboss()


def cast_sanctifyinggrace_boss():
    os.system('cls')
    print "Your attack has been temporarily buffed!"
    option = raw_input("-> ")
    PlayerIG.attackboost += 100
    PlayerIG.faith -= 100
    PlayerIG.boostcount += 1
    if "Boss 1" in PlayerIG.storylist:
        bossfight1()
    if "Boss 2" in PlayerIG.storylist:
        bossfight2()
    if "Boss 3" in PlayerIG.storylist:
        bossfight3()
    if "Boss 4" in PlayerIG.storylist:
        bossfight4()
    if "Boss 5" in PlayerIG.storylist:
        bossfight5()
    if "Boss 6" in PlayerIG.storylist:
        finalboss()

def attack():
    os.system('cls')
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    if PAttack == PlayerIG.attack / 2:
        print "You miss!"
        option = raw_input('-> ')
    else:
        enemy.health -= PAttack
        print("You deal %d damage with  " + str(PlayerIG.curweap) +"!") % PAttack
        option = raw_input('-> ')
    if enemy.health <= 0:
        win()
        os.system('cls')
    if EAttack == enemy.attack / 2:
            print "The enemy missed!"
    else:
        PlayerIG.health -= EAttack
        print ("The enemy deals ") + str(EAttack) +  (" damage!")
        option = raw_input('-> ')
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()


def drinkpot():
    os.system('cls')
    if PlayerIG.potions == 0:
        print "You don't have any potions!"
    else:
        if "Story 1" in PlayerIG.storylist:
            PlayerIG.health += 50
        elif "Story 2" in PlayerIG.storylist:
            PlayerIG.health += 75
        elif "Story 3" in PlayerIG.storylist:
            PlayerIG.health += 100
        elif "Story 5" in PlayerIG.storylist:
            PlayerIG.health += 150
        elif "Story 6" in PlayerIG.storylist:
            PlayerIG.health += 200
        print "You drank a potion!"
    option = raw_input("-> ")
    health_equalization()


def health_equalization():
    if PlayerIG.health > PlayerIG.maxhealth:
        PlayerIG.health = PlayerIG.maxhealth
    fight()



def run():
    runnum = random.randint(1, 3)
    if runnum == 1:
        print "You got away!"
        option = raw_input('-> ')
        start1()
    else:
        print "You couldn't escape!"
        option = raw_input("-> ")
        os.system('cls')
        EAttack = random.randint(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack / 2:
            print "The enemy missed!"
        else:
            PlayerIG.health -= EAttack
            print "The enemy deals damage!"
            option = raw_input('-> ')
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()



def store():
    os.system('cls')
    print "You head to the clergy used book sale in order to gain power and wisdom."
    print "A older gentleman wearing a sack cloth approaches you and says 'Can I interest you in my wares?'"
    print "1.) Buy Weapons"
    print "2.) Unlock Spells"
    print "3.) Some Self Confidence"
    print "4.) Buy a Potion"
    print "Type b to go back"
    option = raw_input("-> ")
    if option.strip() == "1":
        os.system('cls')
        print "You have %s gold\n" % PlayerIG.gold
        print "Type out which weapon you would like to buy.\n"
        if "Voting Machine" not in PlayerIG.weap:
            print "Voting Machine 20g"
        if "Piping Hot Coffee" not in PlayerIG.weap:
            print "Piping Hot Coffee 25g"
        if "Bible" not in PlayerIG.weap:
            print "Bible 40g"
        if "Old Man's Cane" not in PlayerIG.weap:
            print "Old Man's Cane 75g"
        if "Swag Bag" not in PlayerIG.weap:
            print "Swag Bag 175g"
        if "Fold Up Chair" not in PlayerIG.weap:
            print "Fold Up Chair 300g"
        if "Bishop's Staff" not in PlayerIG.weap:
            print "Bishop's Staff 750g"
        print "Type b to go Back"
        option = raw_input('-> ')
        if option in weapons:
            if PlayerIG.gold >= weapons[option]:
                os.system('cls')
                PlayerIG.gold -= weapons[option]
                PlayerIG.weap.append(option)
                os.system('cls')
                print "You have acquired a %s" % option
                option = raw_input("-> ")
                start1()
            else:
                os.system('cls')
                print "You don't have enough resources my child"
                option = raw_input("-> ")
                store()
        elif option.strip().lower() == "b":
            store()
        else:
            print("That item does not exist")
            store()

    elif option.strip() == "2":
        os.system('cls')
        print "Type out what spell you would like.\n"
        print "You have %s gold\n" % PlayerIG.gold
        if "Regeneration" not in PlayerIG.spell_list:
            print "Regeneration (minor healing) 40g"
        if "Pastoral Prayer" not in PlayerIG.spell_list:
            print "Pastoral Prayer (moderate healing) 200g"
        if "Baptismal Remembrance" not in PlayerIG.spell_list:
            print "Baptismal Remembrance (major healing) 1000g"
        if "Benediction" not in PlayerIG.spell_list:
            print "Benediction (minor damage) 40g"
        if "Melodramatic Speech" not in PlayerIG.spell_list:
            print "Melodramatic Speech (moderate damage) 200g"
        if "Call to Question" not in PlayerIG.spell_list:
            print "Call to Question (major damage) 1000g"
        if "Prevenient Grace" not in PlayerIG.spell_list:
            print "Prevenient Grace (minor attack boost) 40g"
        if "Justifying Grace" not in PlayerIG.spell_list:
            print "Justifying Grace (moderate attack boost) 200g"
        if "Sanctifying Grace" not in PlayerIG.spell_list:
            print "Sanctifying Grace (major attack boost) 1000g"
        print "\n"
        print "Type b to go Back"
        option = raw_input("-> ")
        if option.lower() == "regeneration" and PlayerIG.gold >= 40:
            print "You can now cast Regeneration!"
            option = raw_input("-> ")
            PlayerIG.spell_list.append("Regeneration")
            PlayerIG.spell_list_battle.append("Regeneration 10fp")
            PlayerIG.gold -= 40
            store()
        if option.lower() == "pastoral prayer" and PlayerIG.gold >= 200:
            print "You can now cast Pastoral Prayer!"
            option = raw_input("-> ")
            PlayerIG.spell_list.append("Pastoral Prayer")
            PlayerIG.spell_list_battle.append("Pastoral Prayer 30fp")
            PlayerIG.gold -= 200
            store()
        if option.lower() == "baptismal remembrance" and PlayerIG.gold >= 1000:
            print "You can now cast Baptismal Remembrance!"
            option = raw_input("-> ")
            PlayerIG.spell_list.append("Baptismal Remembrance")
            PlayerIG.spell_list_battle.append("Baptismal Remembrance 100fp")
            PlayerIG.gold -= 1000
            store()
        if option.lower() == "benediction" and PlayerIG.gold >= 40:
            print "You can now cast Benediction!"
            option = raw_input("-> ")
            PlayerIG.spell_list.append("Benediction")
            PlayerIG.spell_list_battle.append("Benediction 10fp")
            PlayerIG.gold -= 40
            store()
        if option.lower() == "melodramatic speech" and PlayerIG.gold >= 200:
            print "You can now cast Melodramatic Speech!"
            option = raw_input("-> ")
            PlayerIG.spell_list.append("Melodramatic Speech")
            PlayerIG.spell_list_battle.append("Melodramatic Speech 30fp")
            PlayerIG.gold -= 200
            store()
        if option.lower() == "call to question" and PlayerIG.gold >= 1000:
            print "You can now cast Call to Question!"
            option = raw_input("-> ")
            PlayerIG.spell_list.append("Call to Question")
            PlayerIG.spell_list_battle.append("Call to Question 100fp")
            PlayerIG.gold -= 1000
            store()
        if option.lower() == "prevenient grace" and PlayerIG.gold >= 40:
            print "You can now cast Prevenient Grace!"
            option = raw_input("-> ")
            PlayerIG.spell_list.append("Prevenient Grace")
            PlayerIG.spell_list_battle.append("Prevenient Grace 10fp")
            PlayerIG.gold -= 40
            store()
        if option.lower() == "justifying grace" and PlayerIG.gold >= 200:
            print "You can now cast Justifying Grace!"
            option = raw_input("-> ")
            PlayerIG.spell_list.append("Justifying Grace")
            PlayerIG.spell_list_battle.append("Justifying Grace 30fp")
            PlayerIG.gold -= 200
            store()
        if option.lower() == "sanctifying grace" and PlayerIG.gold >= 1000:
            print "You can now cast Sanctifying Grace!"
            option = raw_input("-> ")
            PlayerIG.spell_list.append("Sanctifying Grace")
            PlayerIG.spell_list_battle.append("Sanctifying Grace 10fp")
            PlayerIG.gold -= 1000
            store()
        if option.lower().strip() == "b":
            store()
        else:
            print "Invalid response or not enough gold!."
            option = raw_input("-> ")
            store()
    elif option.strip() == "3":
        print "Take some self confidence. That is free!"
        option = raw_input("-> ")
        store()
    elif option.strip() == "4":
        buypotion()
    elif option.strip() == "b":
        start1()
    else:
        store()


def buypotion():
    if "Story 1" in PlayerIG.storylist:
        print "You have %s gold" % PlayerIG.gold
        print "Potions are 20 gold. Would you like to buy?"
        print "1.) Yes"
        print "2.) No"
        option = raw_input("-> ")
        if option == "1" and PlayerIG.gold >= 20:
            print "You acquired a potion!"
            option = raw_input("-> ")
            PlayerIG.potions += 1
            PlayerIG.gold -= 20
            store()
        else:
            print "Invalid response, or you do not have enough gold!"
            store()
    elif "Story 2" in PlayerIG.storylist and PlayerIG.gold >= 30:
        print "You have %s gold" % PlayerIG.gold
        print "Potions are 30 gold. Would you like to buy?"
        print "1.) Yes"
        print "2.) No"
        option = raw_input("-> ")
        if option == "1" and PlayerIG.gold >= 30:
            print "You acquired a potion!"
            option = raw_input("-> ")
            PlayerIG.potions += 1
            PlayerIG.gold -= 30
            store()
        if option == "2":
            store()
        else:
            print "Insufficient Funds"
    elif "Story 3" in PlayerIG.storylist:
        print "You have %s gold" % PlayerIG.gold
        print "Potions are 60 gold. Would you like to buy?"
        print "1.) Yes"
        print "2.) No"
        option = raw_input("-> ")
        if option == "1" and PlayerIG.gold >= 60:
            print "You acquired a potion!"
            option = raw_input("-> ")
            PlayerIG.potions += 1
            PlayerIG.gold -= 60
            store()
        else:
            store()
    elif "Story 4" in PlayerIG.storylist:
        print "You have %s gold" % PlayerIG.gold
        print "Potions are 100 gold. Would you like to buy?"
        print "1.) Yes"
        print "2.) No"
        option = raw_input("-> ")
        if option == "1" and PlayerIG.gold >= 100:
            print "You acquired a potion!"
            option = raw_input("-> ")
            PlayerIG.potions += 1
            PlayerIG.gold -= 100
            store()
        else:
            store()
    elif "Story 5" in PlayerIG.storylist:
        print "You have %s gold" % PlayerIG.gold
        print "Potions are 200 gold. Would you like to buy?"
        print "1.) Yes"
        print "2.) No"
        option = raw_input("-> ")
        if option == "1" and PlayerIG.gold >= 200:
            print "You acquired a potion!"
            option = raw_input("-> ")
            PlayerIG.potions += 1
            PlayerIG.gold -= 200
            store()
        else:
            store()
    elif "Story 6" in PlayerIG.storylist:
        print "You have %s gold" % PlayerIG.gold
        print "Potions are 350 gold. Would you like to buy?"
        print "1.) Yes"
        print "2.) No"
        option = raw_input("-> ")
        if option == "1" and PlayerIG.gold >= 350:
            print "You acquired a potion!"
            option = raw_input("-> ")
            PlayerIG.potions += 1
            PlayerIG.gold -= 350
            store()
        else:
            store()
    else:
        store()


def win():
    os.system('cls')
    raw_input("-> ")
    PlayerIG.gold += enemy.goldgain
    PlayerIG.exp += enemy.expgain
    enemy.health = enemy.maxhealth
    PlayerIG.attackboost = 0
    PlayerIG.boostcount = 0
    print "You have survived the encounter!"
    print "You found %i gold!" % enemy.goldgain
    print "You gained %s experience points!" % enemy.expgain
    option = raw_input("-> ")
    start1()


def dead():
    print "You died....at Annual Conference...that sucks...and lost gold...wow."
    option = raw_input("-> ")
    PlayerIG.health = PlayerIG.maxhealth
    PlayerIG.deathcount += 1
    if "Story 1" in PlayerIG.storylist:
        PlayerIG.gold -= 20
    if "Story 2" in PlayerIG.storylist:
        PlayerIG.gold -= 75
    if "Story 3" in PlayerIG.storylist:
        PlayerIG.gold -= 125
    if "Story 4" in PlayerIG.storylist:
        PlayerIG.gold -= 250
    if "Story 5" in PlayerIG.storylist:
        PlayerIG.gold -= 350
    if "Story 6" in PlayerIG.storylist:
        PlayerIG.gold -= 500
    if PlayerIG.gold <= 0:
        PlayerIG.gold = 0
    start1()


def game_instructions():
    os.system('cls')
    print "Hello " + PlayerIG.name + ". Welcome to Annual Conference Adventure!"
    print "Here are some quick instructions. When you are playing. If you see"
    print "numbered options, simply selecting that number, and then clicking Enter"
    print "will make that selection. However, sometimes, you will be prompted to type"
    print "your full response. The game will tell you when that is required. But generally,"
    print "if you do not see numbered selections. You are required to type a full response\n"
    print "Also, if you see an arrow that looks like this: (->) and there aren't numbered "
    print "selections, or options to type out, you are being prompted to hit Enter without"
    print "typing anything.\n"
    print "That's it! Good luck!"
    PlayerIG.storylist.append("instructions")
    option = raw_input("-> ")
    story101()



def storeintro():
    if "store_first" not in PlayerIG.storylist:
        store()
    else:
        print "You make your way to where the used clergy book sale is every year."
        PlayerIG.storylist.remove("store_first")
        store()



def story101():
    os.system('cls')
    #storymessage101 = "Early Summer has arrived, which means its time to go to Annual Conference again.\n" \
               #"You love seeing your friends each year, but the meeting itself is usually,well, awful.\n" \
               #"You pack your bags. As you drive to conference, you can’t help but wish that something\n " \
               #"amazing would happen, something unexpected, something that you would never forget.\n" \
               #"As you arrive, the venue is bustling…people are excited to see each other again. You miss that excitement, but instead,\n " \
               #"you sit in dread at the three days of long speeches, back patting, and longer than necessary bathroom breaks.\n" \
               #"Suddenly, you feel a pestering tap on your shoulder. You turn around to find the pasty eager face of your friend Tim.\n" \
               #1
    #"Tim: " + PlayerIG.name + " It’s so good to see you! Are you ready for conference?\n"


    #for character in storymessage101:
         #sys.stdout.write(character)
         #sys.stdout.flush()
         #time.sleep(0.08)
    print "\n"
    print "1.) I suppose so!"
    print "2.) I do what I have to do I guess"

    option = raw_input("-> ")
    if option.strip() == "1":
        print "Tim: Ugh, you’re annoyingly chipper today. Well, let’s get registered before we have to walk in late with everyone looking at us."
        option = raw_input("-> ")
        story102()
    elif option.strip() == "2":
        print "Tim: Now that’s my little pessimistic friend. Don’t worry, it only gets worse. Well, let’s get registered before we have to walk in late with everyone looking at us."
        story102()
    else:
        print "Tim: Not wanting to talk today? That's fine, let's head inside to get registered."
        option = raw_input("-> ")
        story102()


def story102():
    os.system('cls')
    #story102 = "You walk in with Tim and head to the registration booth. You give the radically underpaid District Administrator your name and receive your badge.\n" \
               #"That night, with your friends, you catch up, vent to each other about work, family, and all the other stuff that is way more important than Annual Confernece. You wonder why it is even necessary at all?\n " \
               #"After a long evening of laughs and catching up, your retire to bed….\n" \
               #"In the morning, you wake up, get dressed quickly and head over to the conference center.\n" \
               #"However…when you arrive, something isn’t right…everyone looks….catatonic….you find a friend, but they don’t respond.\n" \
               #"You scream….you start to panic…but then…you notice that a vote has been put on the floor. Everyone has begun to raise their voting machines in the air in unison.\n" \
               #"You look at the legislation on the large screen. It is a motion to adopt the five points of Calvinism as the official doctrine of the United Methodist Church.\n" \
               #"The presiding officer on stage pauses then says “Does anyone need more time? If not, the vote is closed.\n”" \
               #"You cannot believe what is going on. This is the kind of situation that only happens in really bad pulp fiction rags.\n" \
               #"The vote results come in….the vote passes." \
               #"As you run to the bathroom to catch your breath, and do a little panicking, you sit there and realize what is going on…something\n is controlling and possessing the Annual Conference. " \
               #"You begin to cry…through your sobbing, you wonder why the supernatural is becoming real. You consider calling the cops, alerting \nsomeone to the danger…but everything is sealed shut…and through the window, the outside has been transformed into an almost purple aurora void that surrounds everything." \
               #"You sob some more…you’re scared." \
               #"But, then you decide, you won’t take this. You won’t let your friends be taken captive, you won’t let your church be controlled,\n and you’re always down…to fight Calvinism."
    #for character in story102:
         #sys.stdout.write(character)
         #sys.stdout.flush()
         #time.sleep(0.08)
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 1")
    start1()

def story201():
    print "This story section will lead to a boss fight!"
    print "Are you ready?"
    print "1.) Yes"
    print "2.) No, I'll come back."
    option = raw_input("-> ")
    if option.strip() == "1":
        os.system('cls')
        story2011message = "As you start to get your feet under you, you begin defeating some of your currently possessed friends, making sure not to harm them, only to temporarily incapacitate them.\n" \
                           "In the distance, you sport a hooded figure walking towards you. You prepare to fight, but, the hooded figures voice cuts through the slight fog inside the conference center.\n" \
                           "\n" \
                           "Hooded Figure: Wait stop! I mean you no harm!\n" \
                           "\n"
        for character in story2011message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.08)
        PlayerIG.storylist.append("Story 1.1")
        PlayerIG.storylist.remove("Story 1")
        option = raw_input("-> ")
        print "What do you do?"
        print "1.) Swing your weapon at the hooded figure."
        print "2.) Say (Who are you?!)"
        option = raw_input("-> ")
        if option.strip() == "1":
            story2012message = " The "


        boss_init1()
    else:
        start1()


def story202():
    print "The hooded figure approaches and says 'Good Work my boy!'"
    print "Take this Quadrilateral Seal that Total Depravity left behind."
    print "You receive the Quadrilateral seal of Scripture!"
    option = raw_input("-> ")
    PlayerIG.storylist.remove("Story 1.1")
    PlayerIG.storylist.append("Story 2")
    PlayerIG.maxhealth += 75
    PlayerIG.max_faith += 30
    PlayerIG.health = PlayerIG.maxhealth
    PlayerIG.faith = PlayerIG.max_faith
    PlayerIG.bosscount += 1
    start1()


def story301():
    print "Your story continues."
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 2.1")
    PlayerIG.storylist.remove("Story 2")
    boss_init2()

def story302():
    print "You won....your story continues."
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 3")
    PlayerIG.storylist.remove("Story 2.1")
    PlayerIG.maxhealth += 100
    PlayerIG.max_faith += 50
    PlayerIG.health = PlayerIG.maxhealth
    PlayerIG.faith = PlayerIG.max_faith
    PlayerIG.bosscount += 1
    start1()

def story401():
    print "Your story continues"
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 3.1")
    PlayerIG.storylist.remove("Story 3")
    boss_init3()

def story402():
    print "You won...your story continues!"
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 4")
    PlayerIG.storylist.remove("Story 3.1")
    PlayerIG.maxhealth += 150
    PlayerIG.max_faith += 50
    PlayerIG.health = PlayerIG.maxhealth
    PlayerIG.faith = PlayerIG.max_faith
    PlayerIG.bosscount += 1
    start1()

def story501():
    print "Your story continues!"
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 4.1")
    PlayerIG.storylist.remove("Story 4")
    boss_init4()

def story502():
    print "You won! Your story continues!"
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 5")
    PlayerIG.storylist.remove("Story 4.1")
    PlayerIG.maxhealth += 150
    PlayerIG.max_faith += 50
    PlayerIG.health = PlayerIG.maxhealth
    PlayerIG.faith = PlayerIG.max_faith
    PlayerIG.bosscount += 1
    start1()

def story601():
    print "Your story continues!"
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 5.1")
    PlayerIG.storylist.remove("Story 5")
    boss_init5()

def story602():
    print "You won! You're almost there!"
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 6")
    PlayerIG.storylist.remove("Story 5.1")
    PlayerIG.maxhealth += 50
    PlayerIG.max_faith += 50
    PlayerIG.health = PlayerIG.maxhealth
    PlayerIG.faith = PlayerIG.max_faith
    PlayerIG.bosscount += 1
    start1()

def story701():
    print "Time for the final boss!"
    option = raw_input("-> ")
    PlayerIG.storylist.append("Story 6.1")
    PlayerIG.storylist.remove("Story 6")
    final_boss_init()

def story702():
    print "You did it. It is over."
    option = raw_input("-> ")
    credits()


#Boss Initialization

def boss_init1():
    Total_DepravityIG.health = Total_DepravityIG.maxhealth
    bossfight1()


def boss_init2():
    Unconditional_ElectionIG.health = Unconditional_ElectionIG.maxhealth
    bossfight2()


def boss_init3():
    Limited_AtonementIG.health = Limited_AtonementIG.maxhealth
    bossfight3()


def boss_init4():
    Irresistable_GraceIG.health = Irresistable_GraceIG.maxhealth
    bossfight4()


def boss_init5():
    Saintly_PreservationIG.health = Saintly_PreservationIG.maxhealth
    bossfight5()


def final_boss_init():
    Spirit_of_John_CalvinIG.health = Spirit_of_John_CalvinIG.maxhealth
    finalboss()



# Boss Fights

def bossfight1():
    enemy = Total_DepravityIG
    PlayerIG.storylist.append("Boss 1")
    os.system('cls')
    print ("%s is approached by %s") % (PlayerIG.name, enemy.name)
    print "%s's Health: %s/%s   %s's Health %s/%s" % (
    PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
    print ("Potions: %i") % PlayerIG.potions
    print "1.) Attack"
    print "2.) Cast Spell"
    print "3.) Drink Potion"
    option = raw_input('-> ')
    if option.strip() == "1":
        bossattack1()
    elif option.strip() == "2":
        boss_spells()
    elif option.strip() == "3":
        drinkpotboss1()
    else:
        bossfight1()

def bossfight2():
    enemy = Unconditional_ElectionIG
    os.system('cls')
    print ("%s is approached by %s") % (PlayerIG.name, enemy.name)
    print "%s's Health: %s/%s   %s's Health %s/%s" % (
        PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
    print ("Potions: %i") % PlayerIG.potions
    print "1.) Attack"
    print "2.) Cast Spell"
    print "3.) Drink Potion"
    option = raw_input('-> ')
    if option.strip() == "1":
        bossattack2()
    elif option.strip() == "2":
        boss_spells()
    elif option.strip() == "3":
        drinkpotboss2()
    else:
        bossfight2()

def bossfight3():
    enemy = Limited_AtonementIG
    os.system('cls')
    print ("%s is approached by %s") % (PlayerIG.name, enemy.name)
    print "%s's Health: %s/%s   %s's Health %s/%s" % (
        PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
    print ("Potions: %i") % PlayerIG.potions
    print "1.) Attack"
    print "2.) Cast Spell"
    print "3.) Drink Potion"
    option = raw_input('-> ')
    if option.strip() == "1":
        bossattack3()
    elif option.strip() == "2":
        boss_spells()
    elif option.strip() == "3":
        drinkpotboss3()
    else:
        bossfight3()

def bossfight4():
    enemy = Irresistable_GraceIG
    os.system('cls')
    print ("%s is approached by %s") % (PlayerIG.name, enemy.name)
    print "%s's Health: %s/%s   %s's Health %s/%s" % (
        PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
    print ("Potions: %i") % PlayerIG.potions
    print "1.) Attack"
    print "2.) Cast Spell"
    print "3.) Drink Potion"
    option = raw_input('-> ')
    if option.strip() == "1":
        bossattack4()
    elif option.strip() == "2":
        boss_spells()
    elif option.strip() == "3":
        drinkpotboss4()
    else:
        bossfight4()

def bossfight5():
    enemy = Saintly_PreservationIG
    os.system('cls')
    print ("%s is approached by %s") % (PlayerIG.name, enemy.name)
    print "%s's Health: %s/%s   %s's Health %s/%s" % (
        PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
    print ("Potions: %i") % PlayerIG.potions
    print "1.) Attack"
    print "2.) Cast Spell"
    print "3.) Drink Potion"
    option = raw_input('-> ')
    if option.strip() == "1":
        bossattack5()
    elif option.strip() == "2":
        boss_spells()
    elif option.strip() == "3":
        drinkpotboss5()
    else:
        bossfight5()

def finalboss():
    enemy = Spirit_of_John_CalvinIG
    os.system('cls')
    print ("%s is approached by the %s") % (PlayerIG.name, enemy.name)
    print "%s's Health: %s/%s   %s's Health %s/%s" % (
        PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
    print ("Potions: %i") % PlayerIG.potions
    print "1.) Attack"
    print "2.) Cast Spell"
    print "3.) Drink Potion"
    option = raw_input('-> ')
    if option.strip() == "1":
        bossattack5()
    elif option.strip() == "2":
        boss_spells()
    elif option.strip() == "3":
        drinkpotfinalboss()
    else:
        finalboss()


#bossattack

def bossattack1():
    global Total_DepravityIG
    os.system('cls')
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(Total_DepravityIG.attack / 2, Total_DepravityIG.attack)
    if PAttack == PlayerIG.attack / 2:
        print "You miss!"
        option = raw_input('-> ')
    else:
        Total_DepravityIG.health -= PAttack
        print("You deal %d damage with " + str(PlayerIG.curweap) + "!") % PAttack
        option = raw_input('-> ')
    if Total_DepravityIG.health <= 0:
        bosswin1()
        os.system('cls')
    if EAttack == Total_DepravityIG.attack / 2:
        print "The enemy missed!"
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
    if PlayerIG.health <= 0:
        dead()
    else:
        bossfight1()

def bossattack2():
    global Unconditional_ElectionIG
    os.system('cls')
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(Unconditional_ElectionIG.attack / 2, Unconditional_ElectionIG.attack)
    if PAttack == PlayerIG.attack / 2:
        print "You miss!"
        option = raw_input('-> ')
    else:
        Unconditional_ElectionIG.health -= PAttack
        print("You deal %d damage with " + str(PlayerIG.curweap) + "!") % PAttack
        option = raw_input('-> ')
    if Unconditional_ElectionIG.health <= 0:
        bosswin2()
        os.system('cls')
    if EAttack == Unconditional_ElectionIG.attack / 2:
        print "The enemy missed!"
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
    if PlayerIG.health <= 0:
        dead()
    else:
        bossfight2()


def bossattack3():
    global Limited_AtonementIG
    os.system('cls')
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(Limited_AtonementIG.attack / 2, Limited_AtonementIG.attack)
    if PAttack == PlayerIG.attack / 2:
        print "You miss!"
        option = raw_input('-> ')
    else:
        Limited_AtonementIG.health -= PAttack
        print("You deal %d damage with " + str(PlayerIG.curweap) + "!") % PAttack
        option = raw_input('-> ')
    if Limited_AtonementIG.health <= 0:
        bosswin3()
        os.system('cls')
    if EAttack == Limited_AtonementIG.attack / 2:
        print "The enemy missed!"
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
    if PlayerIG.health <= 0:
        dead()
    else:
        bossfight3()

def bossattack4():
    global Irresistable_GraceIG
    os.system('cls')
    PAttack = random.randint(Irresistable_GraceIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(Irresistable_GraceIG.attack / 2, Irresistable_GraceIG.attack)
    if PAttack == PlayerIG.attack / 2:
        print "You miss!"
        option = raw_input('-> ')
    else:
        Irresistable_GraceIG.health -= PAttack
        print("You deal %d damage with " + str(PlayerIG.curweap) + "!") % PAttack
        option = raw_input('-> ')
    if Irresistable_GraceIG.health <= 0:
        bosswin4()
        os.system('cls')
    if EAttack == Irresistable_GraceIG.attack / 2:
        print "The enemy missed!"
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
    if PlayerIG.health <= 0:
        dead()
    else:
        bossfight4()


def bossattack5():
    global Saintly_PreservationIG
    os.system('cls')
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(Saintly_PreservationIG.attack / 2, Saintly_PreservationIG.attack)
    if PAttack == PlayerIG.attack / 2:
        print "You miss!"
        option = raw_input('-> ')
    else:
        Saintly_PreservationIG.health -= PAttack
        print("You deal %d damage with " + str(PlayerIG.curweap) + "!") % PAttack
        option = raw_input('-> ')
    if Saintly_PreservationIG.health <= 0:
        bosswin5()
        os.system('cls')
    if EAttack == Saintly_PreservationIG.attack / 2:
        print "The enemy missed!"
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
    if PlayerIG.health <= 0:
        dead()
    else:
        bossfight5()

def finalbossattack():
    global Spirit_of_John_CalvinIG
    os.system('cls')
    PAttack = random.randint(Spirit_of_John_CalvinIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(Spirit_of_John_CalvinIG.attack / 2, Spirit_of_John_CalvinIG.attack)
    if PAttack == PlayerIG.attack / 2:
        print "You miss!"
        option = raw_input('-> ')
    else:
        Spirit_of_John_CalvinIG.health -= PAttack
        print("You deal %d damage with " + str(PlayerIG.curweap) + "!") % PAttack
        option = raw_input('-> ')
    if Spirit_of_John_CalvinIG.health <= 0:
        bosswin1()
        os.system('cls')
    if EAttack == Spirit_of_John_CalvinIG.attack / 2:
        print "The enemy missed!"
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals damage!"
        option = raw_input('-> ')
    if PlayerIG.health <= 0:
        dead()
    else:
        finalboss()


def drinkpotboss1():
    os.system('cls')
    if PlayerIG.potions == 0:
        print "You don't have any potions!"
    else:
        if "Story 1" in PlayerIG.storylist:
            PlayerIG.health += 50
        elif "Story 2" in PlayerIG.storylist:
            PlayerIG.health += 75
        elif "Story 3" in PlayerIG.storylist:
            PlayerIG.health += 100
        elif "Story 5" in PlayerIG.storylist:
            PlayerIG.health += 150
        elif "Story 6" in PlayerIG.storylist:
            PlayerIG.health += 200
        elif PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print "You drank a potion!"
    option = raw_input("-> ")
    bossfight1()

def drinkpotboss2():
    os.system('cls')
    if PlayerIG.potions == 0:
        print "You don't have any potions!"
    else:
        if "Story 1" in PlayerIG.storylist:
            PlayerIG.health += 50
        elif "Story 2" in PlayerIG.storylist:
            PlayerIG.health += 75
        elif "Story 3" in PlayerIG.storylist:
            PlayerIG.health += 100
        elif "Story 5" in PlayerIG.storylist:
            PlayerIG.health += 150
        elif "Story 6" in PlayerIG.storylist:
            PlayerIG.health += 200
        elif PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print "You drank a potion!"
    option = raw_input("-> ")
    bossfight2()

def drinkpotboss3():
    os.system('cls')
    if PlayerIG.potions == 0:
        print "You don't have any potions!"
    else:
        if "Story 1" in PlayerIG.storylist:
            PlayerIG.health += 50
        elif "Story 2" in PlayerIG.storylist:
            PlayerIG.health += 75
        elif "Story 3" in PlayerIG.storylist:
            PlayerIG.health += 100
        elif "Story 5" in PlayerIG.storylist:
            PlayerIG.health += 150
        elif "Story 6" in PlayerIG.storylist:
            PlayerIG.health += 200
        elif PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print "You drank a potion!"
    option = raw_input("-> ")
    bossfight3()

def drinkpotboss4():
    os.system('cls')
    if PlayerIG.potions == 0:
        print "You don't have any potions!"
    else:
        if "Story 1" in PlayerIG.storylist:
            PlayerIG.health += 50
        elif "Story 2" in PlayerIG.storylist:
            PlayerIG.health += 75
        elif "Story 3" in PlayerIG.storylist:
            PlayerIG.health += 100
        elif "Story 5" in PlayerIG.storylist:
            PlayerIG.health += 150
        elif "Story 6" in PlayerIG.storylist:
            PlayerIG.health += 200
        elif PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print "You drank a potion!"
    option = raw_input("-> ")
    bossfight4()

def drinkpotboss5():
    os.system('cls')
    if PlayerIG.potions == 0:
        print "You don't have any potions!"
    else:
        if "Story 1" in PlayerIG.storylist:
            PlayerIG.health += 50
        elif "Story 2" in PlayerIG.storylist:
            PlayerIG.health += 75
        elif "Story 3" in PlayerIG.storylist:
            PlayerIG.health += 100
        elif "Story 5" in PlayerIG.storylist:
            PlayerIG.health += 150
        elif "Story 6" in PlayerIG.storylist:
            PlayerIG.health += 200
        elif PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print "You drank a potion!"
    option = raw_input("-> ")
    bossfight5()

def drinkpotfinalboss():
    os.system('cls')
    if PlayerIG.potions == 0:
        print "You don't have any potions!"
    else:
        if "Story 1" in PlayerIG.storylist:
            PlayerIG.health += 50
        elif "Story 2" in PlayerIG.storylist:
            PlayerIG.health += 75
        elif "Story 3" in PlayerIG.storylist:
            PlayerIG.health += 100
        elif "Story 5" in PlayerIG.storylist:
            PlayerIG.health += 150
        elif "Story 6" in PlayerIG.storylist:
            PlayerIG.health += 200
        elif PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print "You drank a potion!"
    option = raw_input("-> ")
    finalboss()




def bosswin1():
    enemy = Total_DepravityIG
    PlayerIG.gold += enemy.goldgain
    PlayerIG.exp += enemy.expgain
    enemy.health = enemy.maxhealth
    PlayerIG.attackboost = 0
    PlayerIG.boostcount = 0
    PlayerIG.storylist.remove("Boss 1")
    print "You have survived the encounter!"
    print "You found %i gold!" % enemy.goldgain
    print "You gained %s experience points!" % enemy.expgain
    option = raw_input("-> ")
    story202()

def bosswin2():
    enemy = Unconditional_ElectionIG
    PlayerIG.gold += enemy.goldgain
    PlayerIG.exp += enemy.expgain
    enemy.health = enemy.maxhealth
    PlayerIG.attackboost = 0
    PlayerIG.boostcount = 0
    print "You have survived the encounter!"
    print "You found %i gold!" % enemy.goldgain
    print "You gained %s experience points!" % enemy.expgain
    option = raw_input("-> ")
    story302()

def bosswin3():
    enemy = Limited_AtonementIG
    PlayerIG.gold += enemy.goldgain
    PlayerIG.exp += enemy.expgain
    enemy.health = enemy.maxhealth
    PlayerIG.attackboost = 0
    PlayerIG.boostcount = 0
    print "You have survived the encounter!"
    print "You found %i gold!" % enemy.goldgain
    print "You gained %s experience points!" % enemy.expgain
    option = raw_input("-> ")
    story402()

def bosswin4():
    enemy = Irresistable_GraceIG
    PlayerIG.gold += enemy.goldgain
    PlayerIG.exp += enemy.expgain
    enemy.health = enemy.maxhealth
    PlayerIG.attackboost = 0
    PlayerIG.boostcount = 0
    print "You have survived the encounter!"
    print "You found %i gold!" % enemy.goldgain
    print "You gained %s experience points!" % enemy.expgain
    option = raw_input("-> ")
    story502()

def bosswin5():
    enemy = Saintly_PreservationIG
    PlayerIG.gold += enemy.goldgain
    PlayerIG.exp += enemy.expgain
    enemy.health = enemy.maxhealth
    PlayerIG.attackboost = 0
    PlayerIG.boostcount = 0
    print "You have survived the encounter!"
    print "You found %i gold!" % enemy.goldgain
    print "You gained %s experience points!" % enemy.expgain
    option = raw_input("-> ")
    story602()

def finalbosswin():
    enemy = Spirit_of_John_CalvinIG
    PlayerIG.gold += enemy.goldgain
    PlayerIG.exp += enemy.expgain
    enemy.health = enemy.maxhealth
    PlayerIG.attackboost = 0
    PlayerIG.boostcount = 0
    print "You have survived the encounter!"
    print "You found %i gold!" % enemy.goldgain
    print "You gained %s experience points!" % enemy.expgain
    option = raw_input("-> ")
    story702()


def credits():
    print "Congratulations! You saved the Methodist Church and gave hope for the future!"
    print "THE END"
    option = raw_input("-> ")
    os.system("exit")





main()


