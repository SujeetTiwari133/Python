import random
import sys


def gamecon(com, player):
    if com == player:
        return None
    elif com == 'r':
        if player == 's':
            return False
        elif player == 'p':
            return True
    elif com == 'p':
        if player == 's':
            return True
        elif player == 'r':
            return False
    elif com == 's':
        if player == 'p':
            return False
        elif player == 'r':
            return True


# RUN = True
i = 0
while i >= 0:
    if i == 0:
        print("Computer choose Rock(r) Paper(p) or Scissor(s) ?")
        randc = random.randint(1, 3)
        if randc == 1:
            com = 'r'
        elif randc == 2:
            com = 'p'
        elif randc == 3:
            com = 's'
        player = input(
            "player please choose from Rock(r) Paper(p) or Scissor(s) ?  ")
        player1 = ['r', 'p', 's', 'e']
        if player not in player1:
            print("Sorry wrong input")
            continue
        else:
            print(f"You chose {player}")
            print(f"The computer chose {com}")
            result = gamecon(com, player)
            if result == None:
                print("The game tied! ")
            elif result == False:
                print("You lose the game!")
            elif result:
                print("You win the game!")
            i += 1
    elif i > 0:
        player = input(
            "player please choose from Rock(r) Paper(p) or Scissor(s) or Exit(e) ?  ")
        # print(player)
        if player not in player1:
            print("Sorry Wrong input !")
            continue
        else:
            print("Computer choose Rock(r) Paper(p) or Scissor(s) ?")
            randc = random.randint(1, 3)
            if randc == 1:
                com = 'r'
            elif randc == 2:
                com = 'p'
            elif randc == 3:
                com = 's'

            print(f"The computer chose {com}")
            print(f"You chose {player}")

            result = gamecon(com, player)
            if result == None:
                print("The game tied! ")
            elif result == False:
                print("You lose the game!")
            elif result:
                print("You win the game!")
        if player == 'e':
            break

print("Thank You for playing !")
