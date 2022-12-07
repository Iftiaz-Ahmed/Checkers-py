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