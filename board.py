'''
Final Program - Checkers Game
Iftiaz Ahmed Alfi
ID: 00768112

python 3.10.6
'''

import piece as p       #Importing piece module
import square as s      #Importing square module

#Board class
class Board:
    def __init__(self):    #Constructor of Board class
        self.activePieces = []  #activePieces list that holds the playable pieces in the board
        self.nextplayer = ""    #Stores the nextplayer
        self.board = [[" " for i in range(9)] for j in range(9)] #Represents 8x8 playable board
        self.rows = [" ", "A", "B", "C", "D", "E", "F", "G", "H"] #Row dictionary
        self.initBoard()
    
    #This function initializes the checker board
    def initBoard(self):
        #Double loop for 2D list
        for row in range(0, 9):
            for col in range(0, 9):
                if col == 0:
                    if row != 0:
                        self.board[row][col] = self.rows[row] #Storing the row labels 
                elif row == 0:
                    if col != 0:
                        self.board[row][col] = col       #Storing the column labels
                elif (row + col) % 2 != 0 and row < 4:   #This formula sets the player1 pieces in place
                    p1PieceObj = p.Piece()               #Creating piece object for player 1
                    p1PieceObj.setLoc(self.rows[row], col)
                    p1PieceObj.setType('x')
                    self.activePieces.append(p1PieceObj) #Adding object in activePieces list
                    self.board[row][col] = p1PieceObj    #Storing player 1 in board
                elif (row + col) % 2 != 0 and row < 6:   #This formula sets the initial empty black positions
                    sqObj = s.Square()                   #Creating square object which doesn't contain any pieces
                    sqObj.setLoc(self.rows[row], col)
                    sqObj.setType('B')
                    self.board[row][col] = sqObj
                elif (row + col) % 2 != 0 and row > 5:   #This formula sets the player2 pieces in place
                    p2PieceObj = p.Piece()               #Creating piece object for player 2
                    p2PieceObj.setLoc(self.rows[row], col)
                    p2PieceObj.setType('o')
                    self.activePieces.append(p2PieceObj) #Adding object in activePieces list
                    self.board[row][col] = p2PieceObj    #Storing player 2 in board
                else:
                    sqObj = s.Square()
                    sqObj.setLoc(self.rows[row], col)
                    sqObj.setType('R')
                    self.board[row][col] = sqObj        #Else the position in board is identified as Red

    #This function renders the board after every moves, jumps or removing of a piece
    def renderBoard(self):
        self.board = [[" " for i in range(0, 9)] for j in range(0, 9)] #By default all the board positions are stored as an empty string

        for i in range(1, 9):           #This loop sets the row names and column numbers in the board
           self.board[i][0] = self.rows[i]
           self.board[0][i] = i

        #This loop iterates all the active pieces and based on the location the piece object is stored in the board
        for piece in self.activePieces: 
            pieceLoc = piece.getLoc()
            self.board[self.rows.index(pieceLoc[0])][pieceLoc[1]] = piece
        
        #This loop checks all the empty strings in the board and is replaced with the square object
        for row in range(1, 9):
            for col in range(1, 9):
                sqObj = s.Square()
                if isinstance(self.board[row][col], str):
                    if (row + col) % 2 != 0:    #If the summation of row and col is not even, that is identified as B
                        sqObj.setLoc(self.rows[row], col) # The square location is set
                        sqObj.setType('B')                # The dquare type is set
                        self.board[row][col] = sqObj      # And the square object stored in the board
                    else:                                 # Else identified as R
                        sqObj.setLoc(self.rows[row], col) # Square location set
                        sqObj.setType('R')                # Square type set
                        self.board[row][col] = sqObj      # And the red square object set to board
    
    # This function removes the piece from the activePieces list
    def removePC(self, piece):
        pieceLoc = piece.getLoc()  # The piece location is retrieved
        print("\n{} deleted from {}{}!\n".format(piece.getType(), pieceLoc[0], pieceLoc[1])) #Prompts deletion msg
        pieceIdx = self.activePieces.index(piece) # Getting the index positon of the piece in activePieces list
        del self.activePieces[pieceIdx]           #Deleting the piece
        self.renderBoard()                        #rendering to update the board

    # This function sets the piece to its destination
    def setPC2Des(self, piece, destination):
        pcLoc = piece.getLoc() # Retrieving piece location
        desRow = self.rows.index(destination[0]) 

        #Prompting moving msg to the players
        print("\n{} moved from {}{} to {}{}".format(piece.getType(), pcLoc[0], pcLoc[1], destination[0], destination[1]))

        # If o player moves to the 1st row, the piece is Kinged
        if desRow == 1 and piece.getType() == 'o':
            print("\nKinged! o to O\n")
            piece.setType("O")     #Piece type set to O
            self.nextplayer = "x"  #The opposition player is set as nextplayer 
        elif desRow == 8 and piece.getType() == 'x': #If x player moves to the last row, the piece is Kinged
            print("\nKinged! x to X\n")
            piece.setType("X")    #Piece type set to X
            self.nextplayer = "o" #The opposition player is set as nextplayer 

        pieceIdx = self.activePieces.index(piece)   #Index postion of piece is retrieved
        piece.setLoc(destination[0], destination[1]) #Piece location is changed to destination location 
        self.activePieces[pieceIdx] = piece          # The piece object is updated in the activePieces list 
    
    # This function prompts the wrong move message
    def wrongMove(self, source, destination):
        print("\nWrong move! {}{} to {}{}\n".format(source[0], source[1], destination[0], destination[1]))
    
    # This function checks if any jump is available for the specified piece 
    def checkJump(self, piece):
        # Piece type and location retrieved
        pcType = piece.getType()
        pcLoc = piece.getLoc()
        found = False # Jump found is set to False initially

        # If type is X
        if pcType == "x":
            row = self.rows.index(pcLoc[0])
            col = pcLoc[1]
       
            positions = [[row+2, col+2], [row+2, col-2]] #The two possible positions it can jump is specified
            for p in positions:
                if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9: #Checks if the positions are within the board
                    if self.board[p[0]][p[1]].getType() == "B": #If the destination point is found 'B'
                        rowAvg = int((row+p[0])/2)             
                        colAvg = int((col+p[1])/2)

                        oPiece = self.board[rowAvg][colAvg].getType()
                        if oPiece == "o" or oPiece == "O":     #It checks whether the middle diagonal is o or O
                            found = True                       #If matches found is set to true and the loop breaks
                            break
        elif pcType == "o":                                    #If type is o
            row = self.rows.index(pcLoc[0])
            col = pcLoc[1]
            positions = [[row-2, col+2], [row-2, col-2]]      #The two possible positions it can jump is specified
            for p in positions:
                if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9: #Checks if the positions are within the board
                    if self.board[p[0]][p[1]].getType() == "B":  #If the destination point is found 'B'
                        rowAvg = int((row+p[0])/2)
                        colAvg = int((col+p[1])/2)
               
                        oPiece = self.board[rowAvg][colAvg].getType()
                        if oPiece == "x" or oPiece == "X":  #It checks whether the middle diagonal is X or x
                            found = True                    #If matches found is set to true and the loop breaks
                            break
        elif pcType == "X" or pcType == "O":                #If it is a King type X or O
            row = self.rows.index(pcLoc[0])
            col = pcLoc[1]
            #The four possible positions it can jump is specified
            positions = [[row-1, col-2], [row-2, col+2], [row+2, col-2], [row+2, col+2]]
            for p in positions:
                if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9: #Checks if the positions are within the board
                    if self.board[p[0]][p[1]].getType() == "B": #If the destination point is found 'B'
                        # The middle diagonal row and column position calculated
                        rowAvg = int((row+p[0])/2)              
                        colAvg = int((col+p[1])/2)
    
                        if pcType == "X":       #If it's X
                            oPiece = self.board[rowAvg][colAvg].getType()
                            if oPiece == "o" or oPiece == "O":    #And the middle piece is o or O
                                found = True                      #found set to true and the loop breaks
                                break
                        else:                                       #If it's O
                            oPiece = self.board[rowAvg][colAvg].getType()
                            if oPiece == "x" or oPiece == "X":      #And the middle piece is X or x
                                found = True                        #found set to true and the loop breaks
                                break
        return found                                                #Returns found value

    # This function jumps the piece from source to des and removes the in between opposition piece
    def jump(self, player, piece, source, destination):
        #Source, destination, middle diagonal row and col and opposition player data retrieved
        source[1] = int(source[1])
        destination[1] = int(destination[1])
        rowAvg = int((self.rows.index(destination[0]) + self.rows.index(source[0]))/2)
        colAvg = int((destination[1] + source[1])/2)
        oppPlayer = "o" if player == "x" else "x"

        oPiece = self.board[rowAvg][colAvg]  # The opposition piece object retrieved
        if oPiece.getType().lower() == oppPlayer.lower(): #If the opposition ordinary or King piece is found
            self.nextplayer = oppPlayer      # Opposition player set as next player
            self.setPC2Des(piece, destination) # Piece moved from source to destination
            self.removePC(oPiece)             # And the opposition player piece removed
        else:
            self.wrongMove(source, destination) # Else prompts wrong move message 
            self.nextplayer = player            # And allows the current player to re-enter move
    
    # This function moves the piece from source to destination
    def movePC(self, player, source, destination):
        #source and destination column is converted from string to int
        source[1] = int(source[1])
        destination[1] = int(destination[1])

        piece = self.board[self.rows.index(source[0])][source[1]] #Piece obj retrieved from source
        pieceType = piece.getType()                               #Piece type retrieved

        if player != pieceType.lower():                           #If the source piece doesn't belong to player
            self.wrongMove(source, destination)                   #Prompts wrong move message
            self.nextplayer = player                              #Next player set to current player
            return                                                #Returns from the function
        
        #rowDiff and colDiff identifies whether the piece moves one step or two step diagonally
        rowDiff = abs(self.rows.index(destination[0]) - self.rows.index(source[0]))
        colDiff = abs(destination[1] - source[1])
        
        #If the piece is x
        if pieceType == "x":
            '''
            Checks it x destination row is greater than it's source row.It can't move backward
            And the destination is empty
            '''
            if destination[0] > source[0] and self.board[self.rows.index(destination[0])][destination[1]].getType() == "B":
                #If it moves one step
                if rowDiff == 1 and colDiff == 1:
                    self.nextplayer = "o"  #Opposition player set as next player
                    self.setPC2Des(piece, destination) #Piece set to destination
                    self.renderBoard()                 #Renders the board
                elif rowDiff == 2 and colDiff == 2:    #If it moves 2 step, means a jump
                    self.jump(player, piece, source, destination) #jump function is called
                else:
                    self.wrongMove(source, destination) #Else wrong move
                    self.nextplayer = "x"               #And nexplayer set as current player
            else:
                self.wrongMove(source, destination)    
                self.nextplayer = "x"
        elif pieceType == "X":                         #If it is a King piece, X. It can move both direction
            if rowDiff == 1 and colDiff == 1:          #If moves one step
                self.nextplayer = "o"
                self.setPC2Des(piece, destination)     #Piece set to destination
                self.renderBoard()
            elif rowDiff == 2 and colDiff == 2:        #If it moves 2 step, means a jump
                self.jump(player, piece, source, destination) #jump function is called
            else:
                self.wrongMove(source, destination)
                self.nextplayer = "x"
        elif pieceType == "O":                        #If it is a King piece, O. It can move both direction
            if rowDiff == 1 and colDiff == 1:         #If moves one step
                self.nextplayer = "x"
                self.setPC2Des(piece, destination)    #Piece set to destination
                self.renderBoard()
            elif rowDiff == 2 and colDiff == 2:       #If it moves 2 step, means a jump
                self.jump(player, piece, source, destination)  #jump function is called
            else:
                self.wrongMove(source, destination)
                self.nextplayer = "o"
        elif pieceType == "o":                      #If the piece is o
            '''
            Checks it o destination row is smaller than it's source row.It can't move backward
            And if the destination is empty
            '''
            if destination[0] < source[0] and self.board[self.rows.index(destination[0])][destination[1]].getType() == "B":
                if rowDiff == 1 and colDiff == 1:      #If it moves one step
                    self.nextplayer = "x"
                    self.setPC2Des(piece, destination) #Piece set to destination
                    self.renderBoard()
                elif rowDiff == 2 and colDiff == 2:    #If it moves 2 step, means a jump
                    self.jump(player, piece, source, destination)  #jump function is called
                else:
                    self.wrongMove(source, destination)
                    self.nextplayer = "o"
            else:
                self.wrongMove(source, destination)
                self.nextplayer = "o"
        
        return self.nextplayer                  #nextPlayer returned

    #This function checks for valid move
    def checkMove(self, player, moves):
        valid = True      # Valid is set to True initially
        
        #Starting location of the move is retrieved
        start = moves[0].split(",")
        startSource =  start[0].split("-")
        startDes = start[1].split("-")

        #Checks if the starting position has the player piece, if not
        if self.board[self.rows.index(startSource[0])][int(startSource[1])].getType().lower() != player:
            valid = False #Then valid is set to False

        if valid: # If it is still valid then...
            if len(moves) == 1: #Checks if there is one move input or multiple
                #If 1 move input, checks the destionation is "B", if not
                if self.board[self.rows.index(startDes[0])][int(startDes[1])].getType() != "B":
                    valid = False  #Valid set to False
            else:      # If multiple inputs are there
                for move in moves:   #For every move input
                    positions = move.split(",")
                    source = positions[0].split("-")
                    destination = positions[1].split("-")
                    #Checks if all the destination location is "B"
                    if self.board[self.rows.index(destination[0])][int(destination[1])].getType() == "B":
                        #Calculates the middle diagonal location 
                        rowAvg = int((self.rows.index(destination[0]) + self.rows.index(source[0]))/2)
                        colAvg = int((int(destination[1]) + int(source[1]))/2)
                        oppPlayer = "o" if player == "x" else "x"  #Opposition player identified
                        #If the middle diagonal has the opposition piece then..
                        if self.board[rowAvg][colAvg].getType().lower() == oppPlayer and int(source[1]) != colAvg:
                            # Valid continues to be True
                            if not valid:  #Unless the valid was False in the earlier iteration
                                valid = False #Then it is kept as False
                        else:  # Or else valid is set to False
                            valid = False
                    else:      # If des not 'B' then valid set to False
                        valid = False
        # IF the valid still continues to be true then all the moves are valid
        if valid:
            #And for every moves
            for move in moves:
                positions = move.split(",")
                source = positions[0].split("-")
                destination = positions[1].split("-")
                self.nextplayer = self.movePC(player, source, destination) #movePC is called to move the piece from source to destination        
        else:
            #Or Else prompts the not valid move message
            print("Not a valid move. Try again!")
            self.nextplayer = player  #And the nextplayer is set to current player
        
        return self.nextplayer  #Returns nextplayer
        
    
    #This functions prints the checker board
    def printBoard(self):
        print("\n------CHECKER BOARD--------")
        for row in range(9):
            for col in range(9):
                #If list item is str or int
                if isinstance(self.board[row][col], str) or isinstance(self.board[row][col], int):
                    print(self.board[row][col], end=" ") #Prints the item
                else: #If object is found
                    print(self.board[row][col].getType(), end=" ") #Calls the getType function of object
            print()
        print("---------------------------")
    
    #This function prints all the activePieces 
    def getPCs(self):
        print("---Active Pieces---")
        for piece in self.activePieces:
            print("{}: {}".format(piece.getType(), piece.getLoc()))
    
    #This function formats the board content into a string
    def getFileBoard(self):
        board = []
        for row in range(9):
            string = ""
            for col in range(9):
                if row == 0:
                    if col == 0:
                        string += " "
                    string += str(self.board[row][col]) #All the column labels are concatenated as string
                #For each row all the columns are concatenated into a string
                elif isinstance(self.board[row][col], str):
                    string += self.board[row][col]
                    string += "-"    
                else:
                    string += self.board[row][col].getType()
            board.append(string) #The string is then appended in the board list
        board.insert(1, "----------------")
        return board  #Returns board list that contains strings 
    
    #This function decide where the game is over or not
    def isGameOver(self):
        #Tracks x and o piece count
        xCount = 0
        oCount = 0
        #Tracks x and o King count
        xKing = 0
        oKing = 0
        #Tracks if jump is available for x/X or o/O type
        xJump = False
        oJump = False
        #Tracks if move is available for x/X or o/O type
        xMove = False
        oMove = False
        #Track if game is over and who won
        gameOver = False
        whoWon = "?"

        # Runs loop for all the active pieces
        for piece in self.activePieces:
            pcLoc = piece.getLoc()
            row = self.rows.index(pcLoc[0])
            col = pcLoc[1]

            if piece.getType() == "x":  #If piece type is x
                if self.checkJump(piece):
                    xJump = True        #Checks jump and set to true if found

                #Checking if move is available
                pos = [[row+1, col-1], [row+1, col+1]]
                for p in pos:
                    if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9:
                        if self.board[p[0]][p[1]].getType() == "B":
                            xMove = True

                xCount += 1  #Counter increased
            elif piece.getType() == "o":     #If o
                if self.checkJump(piece):    #Checkes jumps
                    oJump = True
                
                #Checks move
                pos = [[row-1, col-1], [row-1, col+1]]
                for p in pos:
                    if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9:
                        if self.board[p[0]][p[1]].getType() == "B":
                            oMove = True

                oCount += 1  #Counter incremented 
            elif piece.getType() == "X" or piece.getType() == "O":  #If X or O
                #Cheking move available
                pos = [[row-1, col-2], [row-2, col+2], [row+2, col-2], [row+2, col+2]]
                for p in pos:
                    if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9:
                        if self.board[p[0]][p[1]].getType() == "B":
                            if piece.getType() == "X":  #If X then xMove set to true
                                xMove = True 
                            else:                       #Else oMove set to true
                                oMove = True
                if piece.getType() == "X":
                    #Checking jump for X type
                    if self.checkJump(piece):
                        xJump = True
                    xCount += 1    #Counter increased of x type and also king 
                    xKing += 1
                else:
                    #Checking jump for O type
                    if self.checkJump(piece):
                        oJump = True
                    oCount += 1   #Counter increased of o type and also king 
                    oKing += 1
        
        #If no jumps and moves left for player, game is draw
        if xJump == False and xMove == False and oJump == False and oMove == False:
            whoWon = "d"
            gameOver = True
        #If all x piece is removed, o wins
        elif xCount < 1:
            whoWon = "o"
            gameOver = True
        #If x available but no jump or move left, o wins
        elif xJump == False and xMove == False:
            whoWon = "o"
            gameOver = True
        #If all o piece is removed, x wins
        elif oCount < 1:
            whoWon = "x"
            gameOver = True
        #If o available but no jump or move left, x wins
        elif oJump == False and oMove == False:
            whoWon = "x"
            gameOver = True
        
        print("\n---Pieces---")
        print("x available: {}, King: {}".format(xCount, xKing))
        print("o available: {}, King: {}".format(oCount, oKing))
        print("-------------")
        
        return [gameOver, whoWon]
    

