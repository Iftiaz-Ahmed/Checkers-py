import game as g
from time import localtime, strftime
import os
from pathlib import Path

def main():
    try:
        player1 = input("Enter player 1 name: ")
        player2 = input("Enter player 2 name: ")

        gameObj = g.Game(player1, player2)
        gameObj.runGame()
    except:
        print("Unknow error occurred!")
        pass
    
    current_datetime = strftime('%m_%d_%Y_%I.%M.%S_%p', localtime())
    old = player1 + '_' + player2
    old_name = r'{}'.format(os.path.abspath(old+'.txt'))
    new = old + '_{}'.format(current_datetime)
    new_name = r'{}'.format(os.path.abspath(new+'.txt'))
    os.rename(old_name, new_name)


if __name__ == "__main__":
    main()

