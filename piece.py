class Piece:
    def __init__(self):
        self.locRow = ""
        self.locCol = 0
        self.pcType = ""
    
    #Function to set row and column location of a piece
    def setLoc(self, locRow, locCol):
        self.locRow = locRow
        self.locCol = locCol
    
    #This function returns location data of a piece
    def getLoc(self):
        return [self.locRow, self.locCol]
    
    #This function sets piece type
    def setType(self, pcType):
        self.pcType = pcType
    
    #This function returns piece type
    def getType(self):
        return self.pcType