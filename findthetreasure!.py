print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island, Your mission is to find the treasure.")
way = input("Which way you want to go, right or left?\n")
if way == "right":
    print("Game over, you are dead.")
elif way == "left":
    print("you come to a lake. There is an island in the middle of the lake. ")
    lake = input("swim or wait for a boat?(wait or swim)\n")
    if lake == "swim":
        print("Game over, you are dead.")
    elif lake == "wait":
        print("You arrived at the island. There is a house has 3 doors. One is Yellow One is Blue One is Red")
        door = input("which door do you choose?(blue, red or yellow) ")
        if door == "yellow":
            print("You found the Treasure!")
        elif door == "red":
            print("you fell into flames. Game over.")
        elif door == "blue":
            print("you fell into water. You drowned. Game over")
        
