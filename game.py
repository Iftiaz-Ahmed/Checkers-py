import board as b
import re 

class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.moves = []
    
    def gameMenu(self):
        print("---GAME MENU---")
        print("Press: ")
        print("1: ")
    
    def getSavedMoves(self):
        txt_file = open("moves.txt", "r")
        file_content = txt_file.readlines()
        for line in file_content:
            line.replace("\n", "")
            self.moves.append(line)
        txt_file.close()
    
    def validateMoveInput(self, inpt):
        while(True): 
            inputs = inpt.split(" ")
            valid = True

            for i in inputs:
                #Using regex for pattern matching of move input
                #E.g: "C-2,D-3 D-3,E-2" is the correct way of input
                pattern = re.compile("^[A-H]{1}\-{1}[1-8]{1}\,{1}[A-H]{1}\-{1}[1-8]{1}$")
                if not pattern.match(i):
                    valid = False
            
            if valid:
                break
            else:
                print("Wrong move input! Try again!")

        return inputs
            
    
    def runGame(self):
        boardObj = b.Board()
        player = "x"
        i=0
        boardObj.printBoard()
        # self.getSavedMoves()
        while(True):
            if player == "x":
                promptMsg = "{}({}) Please Enter Your Move: ".format(self.player1Name, player)
            else:
                promptMsg = "{}({}) Please Enter Your Move: ".format(self.player2Name, player)

            moveStrs = self.validateMoveInput(input(promptMsg).strip())
            # moveStrs = self.validateMoveInput(self.moves[i])
            
            player = boardObj.checkMove(player, moveStrs)
            boardObj.printBoard()
                
            if boardObj.isGameOver()[0]:
                if boardObj.isGameOver()[1] == "x":
                    print("{} won the game!".format(self.player1Name))
                else:
                    print("{} won the game!".format(self.player2Name))
                break
            
            # i += 1
            # if i > len(self.moves)-1:
            #     break

    def fileHeader(self):
        pass

    def fileBoard(self):
        pass