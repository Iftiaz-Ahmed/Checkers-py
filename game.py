import board as b
import re 
import os

class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player = "x"
        self.moves = []
    
    def gameMenu(self):
        while(True):
            decision = input("Begin game play? (Y/N): ")
            if decision.lower() == 'y':
                self.runGame()
                return
            elif decision.lower() == 'n':
                return
            else:
                print("Invalid entry!")

    def fileHeader(self):
        return self.player1Name + "_" + self.player2Name + ".txt"
    
    def fileBoard(self, moves, boardObj):
        player = "x" if self.player == "o" else "o"
        isExit = os.path.exists(self.fileHeader())

        if not isExit:
            f = open(self.fileHeader(), "a")
            f.write("GAME START" + '\n')
            for line in boardObj.getFileBoard():
                f.write(line + '\n')
            f.write("*********************************************************" + '\n')
            f.close()

        writeContent = boardObj.getFileBoard()
        if player == 'x':
            title = f"Player 1: {self.player1Name}"
        else:
            title = f"Player 2: {self.player2Name}"
        
        for move in moves:
            pos = move.split(",")
            source = pos[0].split("-")
            des = pos[1].split("-")
            title += f" Move {source[0]}{source[1]} to {des[0]}{des[1]}"
        writeContent.insert(0, title)

        f = open(self.fileHeader(), "a")
        for line in writeContent:
            f.write(line + '\n')
        f.write("*********************************************************" + '\n')
        f.close()
    
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
        boardObj.printBoard()
        while(True):
            if self.player == "x":
                promptMsg = "{}({}) Please Enter Your Move: ".format(self.player1Name, self.player)
            else:
                promptMsg = "{}({}) Please Enter Your Move: ".format(self.player2Name, self.player)

            moveStrs = self.validateMoveInput(input(promptMsg).strip())
            
            self.player = boardObj.checkMove(self.player, moveStrs)
            self.fileBoard(moveStrs, boardObj)
            boardObj.printBoard()
                
            if boardObj.isGameOver()[0]:
                self.isActive = False
                if boardObj.isGameOver()[1] == "x":
                    print("{} won the game!".format(self.player1Name))
                else:
                    print("{} won the game!".format(self.player2Name))
                break
