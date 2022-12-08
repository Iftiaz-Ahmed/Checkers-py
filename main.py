import game as g
from time import localtime, strftime
import os
from pathlib import Path

def validateNameInput(promptMsg, player):
    while(True):
        name = input(promptMsg)
        if name.strip() == "":
            if player == 0:
                promptMsg = "Invalid input for Player 1's Name Please Input a Valid Name: "
            elif player == 1:
                promptMsg = "Invalid input for Player 2's Name Please Input a Valid Name: "
        else:
            break
    return name


def main():
    try:
        player1 = validateNameInput("Enter Player 1's Name: ", 0)
        player2 = validateNameInput("Enter Player 2's Name: ", 1)

        gameObj = g.Game(player1, player2)
        gameObj.gameMenu()
    except:
        print("Unknow error occurred!")
        pass
    
    current_datetime = strftime('%m_%d_%Y_%I.%M.%S_%p', localtime())
    old = player1 + '_' + player2
    old_name = r'{}'.format(os.path.abspath(old+'.txt'))
    new = old + '_{}'.format(current_datetime)
    new_name = r'{}'.format(os.path.abspath(new+'.txt'))
    os.rename(old_name, new_name)
    print("The program ended!")


if __name__ == "__main__":
    main()

