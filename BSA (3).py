import random
import math
import sys

def MonsterList(filename):
    Monsters = {}
    name = ""
    with open(filename) as f:
        for line in f:
            stats = []
            name = line.split(",")[0]
            stats = line.split(",")[1:]
            Monsters[name] = stats
    return Monsters

def MakeMonster(level):
    attributes = {"Dead Beat" : -10, "Sexy" : 10, "Desperate" : 5, "Slimy" : -5, "Painfully Honest" : 0}
    ChosenAtt = random.choice(list(attributes.keys()))
    buff = attributes[ChosenAtt]

    MyMonsters = {}
    MyMonsters = MonsterList("BSATXT.txt")

    name = random.choice(list(MyMonsters.keys()))

    MAttack = int(MyMonsters[name][0]) + buff * level + level*level
    MDefense = int(MyMonsters[name][1]) + buff * level + level*level
    MSpeed = int(MyMonsters[name][2]) + buff * level + level*level
    MHealth = 600 + 100 * level + 20 * buff

    namer = ChosenAtt + " " + name

    Monster = [namer, [MAttack, MDefense, MSpeed, MHealth]]
    return Monster

def Battle(Player, level):
    Monster = []
    Monster = MakeMonster(level)
    print("\n\nA " + Monster[0] + " approaches!!!")

    movelist = ["smack", "defend", "charge"]

    Charge = 0
    MonCharge = 0

    AttackChance =[]

    MonBuffer = Monster[1][2]

    buffer = Player[1][2]

    while Monster[1][3] > 0:
        Player[3][0] += 1
        move = input("\nChoose your move: " +
        "\nSMACK" +
        "\nDEFEND" +
        "\nCHARGE" +
        "\n:")
        while True:
            if move.casefold() == "smack" or move.casefold() == "defend" or move.casefold() == "charge":
                break
            else:
                move = input("Please enter a valid move. \n:")

        MonMove = random.choice(movelist)

        dialogue = input("\n\n" + Monster[0] + " used " + MonMove.upper() +
        "\n\n" + Contestant + " used " + move.upper())

        AttackChance.clear()
        spd = 0
        uspd = 0

        if move.casefold() == "smack":
            if MonMove == "smack":
                while spd < Monster[1][2]:
                    AttackChance.append(2)
                    spd += 1
                while uspd < Player[1][2]:
                    AttackChance.append(1)
                    uspd += 1
                winner = random.choice(AttackChance)

                if winner == 1:
                    att = Player[1][0]
                    fence = Monster[1][1]
                    if att*2 > fence:
                        if Monster[1][3] > (att*2 - fence):
                            Monster[1][3] = Monster[1][3] - (att*2 - fence)
                            Player[3][1] += (att*2 - fence)
                            dialogue = input("\n" + Contestant + " did " + str(att*2 - fence) + " points of damage! " +
                            "\n\n" + Monster[0] + "'s health is now " + str(Monster[1][3]) + ".")
                        else:
                            Player = DeadMonster(Monster, Player, level, buffer)
                            Player[3][1] += Monster[1][3]
                            return Player
                    else:
                        dialogue = input("\n" + Contestant + "'s SMACK isn't powerful enough to do any damage!")

                if winner == 2:
                    att = Monster[1][0]
                    fence = Player[1][1]
                    if att*2 > fence:
                        if Player[1][3] > (att*2 - fence):
                            Player[1][3] = Player[1][3] - (att*2 - fence)
                            Player[3][2] += (att*2 - fence)
                            dialogue = input("\n" + Monster[0] + " did " + str(att*2 - fence) + " points of damage!" +
                            "\n\n" + Contestant + "'s health is now " + str(Player[1][3]) + ".")
                        else:
                            Player[3][2] += Player[1][3]
                            GameOver(Player, level)
                    else:
                        dialogue = input("\n" + Monster[0] + "'s SMACK isn't powerful enough to do any damage!")

            if MonMove == "defend":
                dialogue = input("\n" + Monster[0] + " defended! " + Contestant + " did no damage.")
                Monster[1][2] += 35
            if MonMove == "charge":
                if MonCharge > 2:
                    dialogue = input("\n\n" + Monster[0] + " used it's ULTIMATE SMACK!")
                    MonCharge = 0
                    if Player[1][3] > 400:
                        Player[1][3] = Player[1][3] - 400
                        Player[3][2] += 400
                        dialogue = input("\n" + Monster[0] + " did 400 points of damage! " +
                        Contestant + "'s health is now " + str(Player[1][3]) + ".")
                    else:
                        Player[3][2] += Player[1][3]
                        GameOver(Player, level)
                else:
                    MonCharge += 1
                    att = Player[1][0]
                    fence = Monster[1][1]
                    if att*2 > fence:
                        if Monster[1][3] > (att*2 - fence):
                            Monster[1][3] = Monster[1][3] - (att*2 - fence)
                            Player[3][1] += (att*2 - fence)
                            dialogue = input("\n" + Contestant + " did " + str(att*2 - fence) + " points of damage!" +
                            "\n\n" + Monster[0] + "'s health is now " + str(Monster[1][3]) + ".")
                        else:
                            Player = DeadMonster(Monster, Player, level, buffer)
                            Player[3][1] += Monster[1][3]
                            return Player
                    else:
                        dialogue = input("\n" + Contestant + "'s SMACK isn't powerful enough to do any damage!")
                    if MonCharge == 3:
                        dialogue = input("\n\n" + Monster[0] + "'s ULTIMATE SMACK is fully charged!")
        if move.casefold() == "defend":
            if MonMove == "smack":
                dialogue = input("\n\n" + Contestant + " successfully defended " + Monster[0] + "'s SMACK.")
                Player[1][2] += 35
            if MonMove == "defend":
                dialogue = input("\n\nSuccessfully defended.")
            if MonMove == "charge":
                if MonCharge > 2:
                    dialogue = input("\n\n" + Monster[0] + " used it's ULTIMATE SMACK!")
                    MonCharge = 0
                    if Player[1][3] > 400:
                        Player[1][3] = Player[1][3] - 400
                        Player[3][2] += 400
                        dialogue = input("\n" + Monster[0] + " did 400 points of damage! " +
                        Contestant + "'s health is now " + str(Player[1][3]) + ".")
                    else:
                        Player[3][2] += Player[1][3]
                        GameOver(Player, level)
                if MonCharge < 3:
                    MonCharge += 1
                    if MonCharge == 3:
                        dialogue = input("\n\n" + Monster[0] + "'s ULTIMATE SMACK is fully charged!")
        if move.casefold() == "charge":
            if Charge == 2:
                dialogue = input("\nYou're ULTIMATE SMACK is fully charged!")
                Charge += 1
                if MonMove == "smack":
                    att = Monster[1][0]
                    fence = Player[1][1]
                    if att*2 > fence:
                        if Player[1][3] > (att*2 - fence):
                            Player[1][3] = Player[1][3] - (att*2 - fence)
                            Player[3][2] += (att*2 - fence)
                            dialogue = input("\n" + Monster[0] + " did " + str(att*2 - fence) + " points of damage!" +
                            "\n\n" + Contestant + "'s health is now " + str(Player[1][3]) + ".")
                        else:
                            Player[3][2] += Player[1][3]
                            GameOver(Player, level)
                    else:
                        dialogue = input("\n" + Monster[0] + "'s SMACK isn't powerful enough to do any damage!")
                if MonMove == "charge":
                    if MonCharge > 2:
                        dialogue = input("\n\n" + Monster[0] + " used it's ULTIMATE SMACK!")
                        MonCharge = 0
                        if Player[1][3] > 400:
                            Player[1][3] = Player[1][3] - 400
                            Player[3][2] += 400
                            dialogue = input("\n" + Monster[0] + " did 400 points of damage! " +
                            Contestant + "'s health is now " + str(Player[1][3]) + ".")
                        else:
                            Player[3][2] += Player[1][3]
                            GameOver(Player, level)
                    if MonCharge < 3:
                        MonCharge += 1
                        if MonCharge == 3:
                            dialogue = input("\n\n" + Monster[0] + "'s ULTIMATE SMACK is fully charged!")

            elif Charge < 2:
                Charge += 1
                if MonMove == "smack":
                    att = Monster[1][0]
                    fence = Player[1][1]
                    if att*2 > fence:
                        if Player[1][3] > (att*2 - fence):
                            Player[1][3] = Player[1][3] - (att*2 - fence)
                            Player[3][2] += (att*2 - fence)
                            dialogue = input("\n" + Monster[0] + " did " + str(att*2 - fence) + " points of damage! " +
                            "\n\n" + Contestant + "'s health is now " + str(Player[1][3]) + ".")
                        else:
                            Player[3][2] += Player[1][3]
                            GameOver(Player, level)
                    else:
                        dialogue = input("\n" + Monster[0] + "'s SMACK isn't powerful enough to do any damage!")
                if MonMove == "charge":
                    if MonCharge > 2:
                        dialogue = input("\n\n" + Monster[0] + " used it's ULTIMATE SMACK!")
                        MonCharge = 0
                        if Player[1][3] > 400:
                            Player[1][3] = Player[1][3] - 400
                            Player[3][2] += 400
                            dialogue = input("\n" + Monster[0] + " did 400 points of damage! " +
                            Contestant + "'s health is now " + str(Player[1][3]) + ".")
                        else:
                            Player[3][2] += Player[1][3]
                            GameOver(Player, level)
                    if MonCharge < 3:
                        MonCharge += 1
                        if MonCharge == 3:
                            dialogue = input("\n\n" + Monster[0] + "'s ULTIMATE SMACK is fully charged!")
            elif Charge == 3:
                if MonMove == "charge":
                    if MonCharge < 3:
                        Monster[1][3] = Monster[1][3] - 400
                        Player[3][1] += 400
                        print("\nYou used you're ULTIMATE SMACK!!!" +
                        " It did 400 points of damage!")
                        Charge = 0
                        MonCharge += 1
                        if Monster[1][3] > 0:
                            dialogue = input("\n\n" + Monster[0] + "'s health is now at " + str(Monster[1][3]))
                        if Monster[1][3] <= 0:
                            Player = DeadMonster(Monster, Player, level, buffer)
                            return Player
                    else:
                        dialogue = input("Both fighters used their ultimates! The moves cancel out!")
                        Charge = 0
                        MonCharge = 0
                else:
                    Monster[1][3] = Monster[1][3] - 400
                    Player[3][1] += 400
                    print("\nYou used you're ULTIMATE SMACK!!!" +
                    " It did 400 points of damage!")
                    Charge = 0
                    if Monster[1][3] > 0:
                        dialogue = input("\n\n" + Monster[0] + "'s health is now at " + str(Monster[1][3]))
                    if Monster[1][3] <= 0:
                        Player = DeadMonster(Monster, Player, level, buffer)
                        Player[3][1] += Monster[1][3]
                        return Player


def DeadMonster(Monster, Player, level, buffer):
    units = 100 * level
    opt = [1, 2]
    packs = random.choice(opt)
    dialogue = input("\nYou successfully defeated " + Monster[0] + "!!!"
    + "\n\nYou found " + str(units) + " GALACTIC UNITS." +
    "\nYou found " + str(packs) + " MED PACKS.")
    Player[1][4] = Player[1][4] + units
    Player[1][5] = Player[1][5] + packs
    Player[1][2] = buffer
    return Player

def GameOver(Player, level):
    dialogue = input("\n\n" + Contestant + " was defeated.")

    dialogue = input("\n\nGAME OVER" +
    "\n\nYou made it to level " + str(level) +
    "\nBetter luck next time!")

    print("\nFinal Stats:" +
    "\nAttack: " + str(Player[1][0]) +
    "\nDefense: " + str(Player[1][1]) +
    "\nSpeed: " + str(Player[1][2]) +
    "\nMax Health: " + str(Player[1][6]) +
    "\n\nTotal Moves: " + str(Player[3][0]) +
    "\nDamage Dealt: " + str(Player[3][1]) +
    "\nDamage Taken: " + str(Player[3][2]))
    sys.exit()

def Shop(Player):
    ShopChoice = input("\n\nWould you like to enter the shop?" + "\n:")
    if ShopChoice.casefold() == "yes":
        while True:
            Pow = 25 + Player[2][0] * 5
            Def = 25 + Player[2][1] * 5
            Spe = 25 + Player[2][2] * 5
            Pac = 35 + Player[2][3] * 5
            Hel = 50 + Player[2][4] * 25

            Purchase = input("\nEnter your selection. Type EXIT to leave shop." +
            "\n\nPOWER:" +
            "\n" + str(Pow) + " GU" +
            "\n\nDEFENSE:" +
            "\n" + str(Def) + " GU" +
            "\n\nSPEED:" +
            "\n" + str(Spe) + " GU" +
            "\n\nMED PACK:" +
            "\n" + str(Pac) + " GU" +
            "\n\nHEALTH:" +
            "\n" + str(Hel) + " GU" +
            "\n\n:")


            if Purchase.casefold() == "power":
                if Player[1][4] >= Pow:
                    Player[1][0] = Player[1][0] + 10
                    Player[2][0] += 1
                    Player[1][4] = Player[1][4] - Pow
                    dialogue = input("\n\nYou're POWER has increased!" +
                    "\nReamaining units: " + str(Player[1][4]))

                else:
                    dialogue = input("\nYou don't have enough galactic units to purchase this item.")
            if Purchase.casefold() == "defense":
                if Player[1][4] >= Def:
                    Player[1][1] = Player[1][1] + 10
                    Player[2][1] += 1
                    Player[1][4] = Player[1][4] - Def
                    dialogue = input("\n\nYou're DEFENSE has increased!" +
                    "\nReamaining units: " + str(Player[1][4]))

                else:
                    dialogue = input("\nYou don't have enough galactic units to purchase this item.")
            if Purchase.casefold() == "speed":
                if Player[1][4] >= Spe:
                    Player[1][2] = Player[1][2] + 10
                    Player[2][2] += 1
                    Player[1][4] = Player[1][4] - Spe
                    dialogue = input("\n\nYou're SPEED has increased!" +
                    "\nReamaining units: " + str(Player[1][4]))

                else:
                    dialogue = input("\nYou don't have enough galactic units to purchase this item.")
            if Purchase.casefold() == "med pack":
                if Player[1][4] >= Pac:
                    Player[1][5] = Player[1][5] + 1
                    Player[2][3] += 1
                    Player[1][4] = Player[1][4] - Pac
                    dialogue = input("\n\nYou purchased one MED PACK!" +
                    "\nReamaining units: " + str(Player[1][4]))

                else:
                    dialogue = input("\nYou don't have enough galactic units to purchase this item.")
            if Purchase.casefold() == "health":
                if Player[1][4] >= Hel:
                    Player[1][6] = Player[1][6] + 100
                    Player[1][3] = Player[1][3] + 100
                    Player[2][4] += 1
                    Player[1][4] = Player[1][4] - Hel
                    dialogue = input("\n\nYou're HEALTH has increased!" +
                    "\nReamaining units: " + str(Player[1][4]))

                else:
                    dialogue = input("\nYou don't have enough galactic units to purchase this item.")
            if Purchase.casefold() == "exit":
                dialogue = input("\n\nPurchase Complete")
                return Player
    if ShopChoice.casefold() == "no":
        return Player

def Menu(Player):
    if Player[1][5] > 0:
        decision = input("\nYou're health is currently " + str(Player[1][3]) + " out of " + str(Player[1][6]) +
        "\nWould you like to use a MED PACK? \n:")
        while True:
            if decision.casefold() == "yes":
                amount = int(input("\nHow many would you like to use? \nYou currently have " + str(Player[1][5]) + "\n:"))
                while True:
                    if Player[1][5] >= amount:
                        Player[1][3] = Player[1][3] + 200 * amount
                        Player[1][5] = Player[1][5] - amount
                        break
                    else:
                        amount = input("You don't have that many MED PACKS.")
                if Player[1][3] > Player[1][6]:
                    Player[1][3] = Player[1][6]
                dialogue = input("\n\nYou're health is now at " + str(Player[1][3]))
                return Player
            elif decision.casefold() == "no":
                return Player
            else:
                decision = input("Please enter either 'YES' or 'NO'.")


def Victory(Player):
    dialogue = input("\n\nTriumphant, you step away from MASTER's body. "  +
    "\nSecurity guards rain down on you, and you concede, " +
    "\nknowing you've done all you can, hoping to one day be free again.")

    print("\n\n\nVICTORY")

    print("\nFinal Stats:" +
    "\nAttack: " + str(Player[1][0]) +
    "\nDefense: " + str(Player[1][1]) +
    "\nSpeed: " + str(Player[1][2]) +
    "\nMax Health: " + str(Player[1][6]) +
    "\n\nTotal Moves: " + str(Player[3][0]) +
    "\nDamage Dealt: " + str(Player[3][1]) +
    "\nDamage Taken: " + str(Player[3][2]))


    sys.exit()


print("\nWelcome Contestant!" +
"\n\nThis is BATTLE SMACK, the ultimate smacking arena!" +
"\n\nEvery fight is to the death, so be prepared to smack the life out of somebody!"
"\n\nLet's start by creating your champion!\n\n")

Contestant = ""
count1 = 0

BPacks = 0
BAtt = 0
BDef = 0
BSpeed = 0
BHealth = 0



attack = 0
defense = 0
speed = 0
health = 1000
weapon = ""
units = 0
packs = 0
maxH = 1000
TotalMoves = 0
TotalDamage = 0
TotalDamageTaken = 0


Contestant = input("What is your name? \n:")

while True:
    if Contestant != "":
        break
    else:
        Contestant = input("\nPlease enter a valid name.\n:")



Class = input("\n\nChoose your class, " + Contestant + ":" +
"\n\nFISH MAN:" +
"\nAttack: 100" +
"\nDefense: 100" +
"\nSpeed: 100" +

"\n\nMOM:" +
"\nAttack: 100" +
"\nDefense: 50" +
"\nSpeed: 150" +

"\n\nMUTANT SLOTH:" +
"\nAttack: 100" +
"\nDefense: 175" +
"\nSpeed: 25" +

"\n\nFLYING MONKEY:" +
"\nAttack: 150" +
"\nDefense: 75" +
"\nSpeed: 75" +

"\n\nARMORED INFANT:" +
"\nAttack: 25" +
"\nDefense: 125" +
"\nSpeed: 150" +

"\n\nPIRATE:" +
"\nAttack: 200" +
"\nDefense: 25" +
"\nSpeed: 75" +

"\n\nHOBO:" +
"\nAttack: 25" +
"\nDefense: 25" +
"\nSpeed: 25\n\n:")

while True:
    if Class.casefold() == "fish man":
        attack = 100
        defense = 100
        speed = 100
        weapon = "Caviar"
        break
    if Class.casefold() == "mom":
        attack = 100
        defense = 50
        speed = 150
        weapon = "Magic Bean"
        break
    if Class.casefold() == "mutant sloth":
        attack = 100
        defense = 175
        speed = 25
        weapon = "Cardiovascular Disorder"
        break
    if Class.casefold() == "flying monkey":
        attack = 150
        defense = 75
        speed = 75
        weapon = "Banana Bomb"
        break
    if Class.casefold() == "armored child":
        attack = 75
        defense = 125
        speed = 100
        weapon = "Tired Parent"
        break
    if Class.casefold() == "pirate":
        attack = 200
        defense = 50
        speed = 50
        weapon = "Laser Hook"
        break
    if Class.casefold() == "hobo":
        attack = 25
        defense = 25
        speed = 25
        weapon = "Warm Meal"
        break
    else:
        Class = input("Please enter a category listed above.\n:")

Player = [Contestant, [attack, defense, speed, health, units, packs, maxH], [BAtt, BDef, BSpeed, BPacks, BHealth], [TotalMoves, TotalDamage, TotalDamageTaken]]

print("\nSelection succesful! " + Class.title() + " " + Contestant + " has entered the arena!")

dialogue = input("\n\nYou wake up in a clouded haze on a distant planet. You look around, but see nothing." +
"\n\nOut of nowhere, a greasy humanoid grabs your shoulder and puts" +
"\na suspicious metal rod up to your neck.")

dialogue = input("\n\nMASTER:\n'GET UP!!!" +
"\nI PAID 3,000 Galactic Units FOR YOU, SLAVE." +
"\nYOU BETTER SMACK THE LIVING HELL OUT OF EVERYBODY!!!" +
"\nNOW, TAKE THIS AND GO WIN ME SOME MONEY!!!'")

dialogue = input("\n\nMASTER gives you one rusty " + weapon + ".")

dialogue = input("\nYou slowly walk into a small stone arena, surrounded by lowlifes betting on your demise.")

level = 1

Player = Battle(Player, level)

Player = Shop(Player)

Player = Menu(Player)

level = 2

dialogue = input("\n\nMASTER:" + "\nWOW!!! I'LL MAKE A CHAMPION OUT OF YOU YET!!!" +
"\n\nI NEED TO GET YOU TO THE BIG LEAGUES!!!" +
"\nBUT FIRST, LET'S CHALLENGE THE LOCAL GANG LEADER, JAYSON!!!" +
"\nSHOW HIS SLAVES WHAT YOU'RE MADE OF!!!! I'M GUNNA BE RICH!!!!")

dialogue = input("\n\nYou walk into an abandoned highshool and" +
"\nfind JAYSON waiting with two fighters.")

dialogue = input("\n\nJAYSON:" +
"\nHOW DARE YOU ENTER MY TEMPLE!!! YOU WILL PAY FOR THIS!!!")

dialogue = input("\n\nMASTER:" +
"\nNO, YOU!!!")

dialogue = input("\n\nJAYSON:" +
"\nNO, YOU!!!")

dialogue = input("\n\nMASTER:" +
"\nNO, YOU!!!")

Player = Battle(Player, level)

Player = Menu(Player)

Player = Battle(Player, level)

Player = Shop(Player)

Player = Menu(Player)

level = 3

dialogue = input("\n\nMASTER: " +
"\nTHAT'S WHAT I'M TALKING ABOUT!!!" +
"\nI JUST SCHEDULED A MINOR LEAGUE FIGHT FOR YOU." +
"\nCOME ON, TIME IS WASTING, AND TIME IS MONEY!!!")

dialogue = input("\nYou enter a run-down arena to find 5 other \nfighters, standing in a circle, ready to SMACK")

Player = Battle(Player, level)

dialogue = input("\n\nAs you deliver the final blow, the only other remaining \nfighter comes sprinting toward you.")

Player = Menu(Player)

Player = Battle(Player, level)

Player = Shop(Player)

Player = Menu(Player)

level = 4

dialogue = input("\n\nMASTER: " +
"\nINCREDULOUS!!! AMAZING JOB SLAVE, " +
"\nTO THE BIG LEAGUES WE GO!!!")

dialogue = input("\n\nAs your final fight approaches, you think back to your life before." +
"\nYou grow hopeful, knowing freedom is within arms reach.")

dialogue = input("\n\nYou enter a stadium full of screaming fans, but none cheer for you.")

Player = Battle(Player, level)

Player = Menu(Player)

Player = Battle(Player, level)

Player = Menu(Player)

dialogue = input("\n\nThis is it. Your last fight before freedom.")

Player = Battle(Player, level)

Player = Shop(Player)

Player = Menu(Player)


dialogue = input("\n\nMASTER: " +
"\nYOU THOUGHT I WOULD FREE YOU? " +
"\nBWAHAHAHAHAHAHAHA" +
"\nI'LL FORCE YOU TO FIGHT UNTIL YOU DIE," +
"\nAND YOU'LL MAKE ME RICH IN THE PROCESS!!!")

dialogue = input("\n\nEnraged, you charge your master.")



Monster = ["MASTER", [250, 150, 175, 2000]]
print("\n\n" + Monster[0] + " approaches!!!")

movelist = ["smack", "defend", "charge"]

Charge = 0
MonCharge = 0

AttackChance =[]

TotalMoves = 0

while Monster[1][3] > 0:
    TotalMoves += 1
    move = input("\nChoose your move: " +
    "\nSMACK" +
    "\nDEFEND" +
    "\nCHARGE" +
    "\n:")
    while True:
        if move.casefold() == "smack" or move.casefold() == "defend" or move.casefold() == "charge":
            break
        else:
            move = input("Please enter a valid move. \n:")

    MonMove = random.choice(movelist)

    dialogue = input("\n\n" + Monster[0] + " used " + MonMove.upper() +
    "\n\n" + Contestant + " used " + move.upper())

    AttackChance.clear()
    spd = 0
    uspd = 0

    if move.casefold() == "smack":
        if MonMove == "smack":
            while spd < Monster[1][2]:
                AttackChance.append(0)
                spd += 1
            while uspd < Player[1][2]:
                AttackChance.append(1)
                uspd += 1
            winner = random.choice(AttackChance)

            if winner == 1:
                att = Player[1][0]
                fence = Monster[1][1]
                if att*2 > fence:
                    if Monster[1][3] > (att*2 - fence):
                        Monster[1][3] = Monster[1][3] - (att*2 - fence)
                        dialogue = input("\n" + Contestant + " did " + str(att*2 - fence) + " points of damage!" +
                        "\n\n" + Monster[0] + "'s health is now " + str(Monster[1][3]) + ".")
                    else:
                        Victory(Player)

                else:
                    dialogue = input("\n" + Contestant + "'s SMACK isn't powerful enough to do any damage!")

            if winner == 0:
                att = Monster[1][0]
                fence = Player[1][1]
                if att*2 > fence:
                    if Player[1][3] > (att*2 - fence):
                        Player[1][3] = Player[1][3] - (att*2 - fence)
                        dialogue = input("\n" + Monster[0] + " did " + str(att*2 - fence) + " points of damage!" +
                        "\n\n" + Contestant + "'s health is now " + str(Player[1][3]) + ".")
                    else:
                        GameOver(Player)
                else:
                    dialogue = input("\n" + Monster[0] + "'s SMACK isn't powerful enough to do any damage!")

        if MonMove == "defend":
            dialogue = input("\n" + Monster[0] + " defended! " + Contestant + " did no damage.")
        if MonMove == "charge":
            if MonCharge > 2:
                dialogue = input("\n\n" + Monster[0] + " used it's ULTIMATE SMACK!")
                MonCharge = 0
                if Player[1][3] > 400:
                    Player[1][3] = Player[1][3] - 400
                    dialogue = input("\n" + Monster[0] + " did 400 points of damage!" +
                    Contestant + "'s health is now " + str(Player[1][3]) + ".")
                else:
                    GameOver(Player)
            if MonCharge < 3:
                MonCharge += 1
                att = Player[1][0]
                fence = Monster[1][1]
                if att*2 > fence:
                    if Monster[1][3] > (att*2 - fence):
                        Monster[1][3] = Monster[1][3] - (att*2 - fence)
                        dialogue = input("\n" + Contestant + " did " + str(att*2 - fence) + " points of damage!" +
                        "\n\n" + Monster[0] + "'s health is now " + str(Monster[1][3]) + ".")
                    else:
                        Victory(Player)
                else:
                    dialogue = input("\n" + Contestant + "'s SMACK isn't powerful enough to do any damage!")
                if MonCharge == 3:
                    dialogue = input("\n\n" + Monster[0] + "'s ULTIMATE SMACK is fully charged!")
    if move.casefold() == "defend":
        if MonMove == "smack":
            dialogue = input("\n\n" + Contestant + " successfully defended " + Monster[0] + "'s SMACK.")
        if MonMove == "defend":
            dialogue = input("\n\nSuccessfully defended.")
        if MonMove == "charge":
            if MonCharge > 2:
                dialogue = input("\n\n" + Monster[0] + " used it's ULTIMATE SMACK!")
                MonCharge = 0
                if Player[1][3] > 400:
                    Player[1][3] = Player[1][3] - 400
                    dialogue = input("\n" + Monster[0] + " did 400 points of damage!" +
                    Contestant + "'s health is now " + str(Player[1][3]) + ".")
                else:
                    GameOver(Player)
            if MonCharge < 3:
                MonCharge += 1
                if MonCharge == 3:
                    dialogue = input("\n\n" + Monster[0] + "'s ULTIMATE SMACK is fully charged!")
    if move.casefold() == "charge":
        if Charge == 2:
            dialogue = input("You're ULTIMATE SMACK is fully charged!")
            Charge += 1
            if MonMove == "smack":
                att = Monster[1][0]
                fence = Player[1][1]
                if att*2 > fence:
                    if Player[1][3] > (att*2 - fence):
                        Player[1][3] = Player[1][3] - (att*2 - fence)
                        dialogue = input("\n" + Monster[0] + " did " + str(att*2 - fence) + " points of damage!" +
                        "\n\n" + Contestant + "'s health is now " + str(Player[1][3]) + ".")
                    else:
                        GameOver(Player)
                else:
                    dialogue = input("\n" + Monster[0] + "'s SMACK isn't powerful enough to do any damage!")

        if Charge < 2:
            Charge += 1
            if MonMove == "smack":
                att = Monster[1][0]
                fence = Player[1][1]
                if att*2 > fence:
                    if Player[1][3] > (att*2 - fence):
                        Player[1][3] = Player[1][3] - (att*2 - fence)
                        dialogue = input("\n" + Monster[0] + " did " + str(att*2 - fence) + " points of damage!" +
                        "\n\n" + Contestant + "'s health is now " + str(Player[1][3]) + ".")
                    else:
                        GameOver(Player)
                else:
                    dialogue = input("\n" + Monster[0] + "'s SMACK isn't powerful enough to do any damage!")
        if Charge == 3:
            Monster[1][3] = Monster[1][3] - 400
            print("\nYou used you're ULTIMATE SMACK!!!" +
            " It did 400 points of damage!")
            if Monster[1][3] > 0:
                dialogue = input("\n\n" + Monster[0] + "'s health is now at " + str(Monster[1][3]))
            if Monster[1][3] <= 0:
                Victory(Player)
