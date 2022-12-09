'''
Final Program - Checkers Game
Iftiaz Ahmed Alfi
ID: 00768112

The main module takes valid player 1 and player 2 name inputs and with it creates a Game class object. It then calls the gameMenu function and when the program ends, it renames the old log file with new name. 

python 3.10.6
'''


import game as g                         #importing game module
from time import localtime, strftime     #importing time library to get current time and date
import os                                #importing os library to rename the log file


#This function takes a non-empty name input and returns the name
def validateNameInput(promptMsg, player):
    while(True):
        name = input(promptMsg)
        if name.strip() == "":          #If the name input is empty shows an invalid msg based on player
            if player == 0:             #And asks to re-enter the name
                promptMsg = "Invalid input for Player 1's Name Please Input a Valid Name: "
            elif player == 1:
                promptMsg = "Invalid input for Player 2's Name Please Input a Valid Name: "
        else:
            break
    return name                         #Non-empty name value returned


#The main function from where the program starts
def main():
    try:                                                           #Exception used to avoid any input errors
        player1 = validateNameInput("Enter Player 1's Name: ", 0)  #Taking Player 1 name input
        player2 = validateNameInput("Enter Player 2's Name: ", 1)  #Taking Player 2 name input

        gameObj = g.Game(player1, player2)                         #Creating Game class object with player 1 & 2
        gameObj.gameMenu()                                         #Calling gameMenu() from the Game class
    except:
        print("Unknown error occurred!")
    
    current_datetime = strftime('%m_%d_%Y_%I.%M.%S_%p', localtime()) #Current date and time retrieved
    old = player1 + '_' + player2                                    #The old file name consist of player 1 and 2 name
    old_name = r'{}'.format(os.path.abspath(old+'.txt'))    #Absolute file path retrieved and converted to raw string
    new = old + '_{}'.format(current_datetime)             
    new_name = r'{}'.format(os.path.abspath(new+'.txt')) #Absolute file path for new name and converted to raw string
    
    isExits = os.path.exists(old+'.txt')                    #Checking if the old file exits
    if isExits:                                             #If it exists then
        os.rename(old_name, new_name)                       #The old_name is renamed to new_name
        print("The program ended!")                         # Program end prompt message


if __name__ == "__main__":
    main()

