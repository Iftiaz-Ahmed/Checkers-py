'''
Final Program - Checkers Game
Iftiaz Ahmed Alfi
ID: 00768112

This module gives the template for the empty squares in the game. It sets the location and type of the empty squares, which can be either 'Black' or 'Red', and returns the location and type of empty squares when the get functions are called. 

python 3.10.6
'''

class Square:
    def __init__(self):
        self.locRow = ""
        self.locCol = 0
        self.sqType = ""
    
    #Function to set row and column location of a square
    def setLoc(self, locRow, locCol):
        self.locRow = locRow
        self.locCol = locCol
    
    #This function returns location data of a square
    def getLoc(self):
        return [self.locRow, self.locCol]
    
    #This function sets square type
    def setType(self, sqType):
        self.sqType = sqType
    
    #This function returns square type
    def getType(self):
        return self.sqType