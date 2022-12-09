'''
Final Program - Checkers Game
Iftiaz Ahmed Alfi
ID: 00768112

This module has the Game class. It displays the gameMenu to the players and upon their decision runs the game by creating Board class object and calling its functions. It logs all the active game moves and stores in a file.

python 3.10.6
'''

import board as b         #Imports board module
import re                 #Imports regex library
import os                 #Imports os library

#Game class
class Game:
    def __init__(self, player1Name, player2Name):   #Constructor of a Game class
        self.player1Name = player1Name              #Takes player 1 and 2 input and sets them in the constructor
        self.player2Name = player2Name
        self.player = "x"                           #The current player turn is stored here
    
    #This function displays an option to the user to begin the game
    def gameMenu(self):
        while(True):
            decision = input("Begin game play? (Y/N): ")  #Taking user decision input
            if decision.lower() == 'y':                   #If Y
                self.runGame()                            #Then runGame function is called
                return                          
            elif decision.lower() == 'n':                 #If N
                return                                    #It returns and the program ends
            else:
                print("Invalid entry!")                   #Else prompts invalid message and asks to enter again

    #This function creates the log file of the active game and writes the initial game board to the file
    def fileHeader(self, boardObj):
        fileName = self.player1Name + "_" + self.player2Name + ".txt"  #Filename of the log file

        f = open(fileName, "w")                           #File opened in write mode
        f.write("GAME START" + '\n')                      #write() is used to add contents in the file 
        for line in boardObj.getFileBoard():
            f.write(line + '\n')
        f.write("*********************************************************" + '\n')
        f.close()                                         #File closed
    
    #This function appends content in the active log file
    def fileBoard(self, moves, boardObj):
        player = "x" if self.player == "o" else "o"       #Correct player identified
        fileName = self.player1Name + "_" + self.player2Name + ".txt"  #Filename created


        writeContent = boardObj.getFileBoard()            #Getting the current board in formatted strings
        
        '''
        Before adding the board content in the file the dynamic title is created first.
        First the player information is added to the title.
        Then based on the number of moves he played, all the moves are concatenated with 
        the title variable. 
        '''
        if player == 'x':                                 
            title = f"Player 1: {self.player1Name}"
        else:
            title = f"Player 2: {self.player2Name}"
        
        for move in moves:
            pos = move.split(",")
            source = pos[0].split("-")
            des = pos[1].split("-")
            title += f" Move {source[0]}{source[1]} to {des[0]}{des[1]}" #Move details concatenated

        writeContent.insert(0, title)  #The title is added at the beginning of the board contents 

        f = open(fileName, "a")        #The file is opened in append mode
        for line in writeContent:      #Contents appended in log file
            f.write(line + '\n')
        f.write("*********************************************************" + '\n')
        f.close()                      #File closed
    
    #This function validates user's move input
    def validateMoveInput(self, promptMsg):
        while(True):
            inpt = input(promptMsg).strip() #Move input taken from player
            inputs = inpt.split(" ")   #All move inputs are splitted and stored in inputs list
            valid = True               #valid is kept True initially

            for i in inputs:           #For all the move inputs
                #Using regex for pattern matching of move input
                #E.g: "C-2,D-3 D-3,E-2" is the correct way of input
                pattern = re.compile("^[A-H]{1}\-{1}[1-8]{1}\,{1}[A-H]{1}\-{1}[1-8]{1}$")
                if not pattern.match(i):
                    valid = False     #If not matched, valid is set to False
            
            if valid:                #If valid, the loop breaks
                break
            else:
                print("Wrong move input! Try again!") #Else prompts wrong move message and asks to try again

        return inputs               #The valid inputs list is then returned
    

    #This is the main function of the Game class that calls the Board class to play the game        
    def runGame(self):
        boardObj = b.Board()        #The board object is first created
        self.fileHeader(boardObj)   #This function is called to create a log file and add the initial board in file
        boardObj.printBoard()       #Calls printBoard() to display the board

        while(True):
            #Based on player the prompt message is set, to display for moves input
            if self.player == "x":
                promptMsg = "{}({}) Please Enter Your Move: ".format(self.player1Name, self.player)
            else:
                promptMsg = "{}({}) Please Enter Your Move: ".format(self.player2Name, self.player)

            moveStrs = self.validateMoveInput(promptMsg) #The valid move inputs are stored in moveStrs
            
            '''
            checkMove() function is called to check if the moves are valid which then calls the movePC() function
            which then returns the player that has the next turn
            '''
            self.player = boardObj.checkMove(self.player, moveStrs) 

            self.fileBoard(moveStrs, boardObj) #After the move, the updated board content is logged in the file
            boardObj.printBoard()              #Displays the updated board content to the players
                
            isGameOver, whoWon = boardObj.isGameOver() #This function returns if the game is over and who won
            if isGameOver:                             #If the game is over
                if whoWon == "x":                      #It checks who won and prompts the final verdict of the game
                    print("{} won the game!".format(self.player1Name))
                elif whoWon == "d":
                    print("The game is a draw!")
                else:
                    print("{} won the game!".format(self.player2Name))
                break                                  #Breaks the loop
