import piece as p
import square as s

class Board:
    def __init__(self):
        self.activePieces = []
        self.nextplayer = "" 
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

    
    def renderBoard(self):
        self.board = [[" " for i in range(0, 9)] for j in range(0, 9)]

        for i in range(1, 9):
           self.board[i][0] = self.rows[i]
           self.board[0][i] = i

        for piece in self.activePieces:
            pieceLoc = piece.getLoc()
            self.board[self.rows.index(pieceLoc[0])][pieceLoc[1]] = piece
        
        for row in range(1, 9):
            for col in range(1, 9):
                sqObj = s.Square()
                if isinstance(self.board[row][col], str):
                    if (row + col) % 2 != 0:
                        sqObj.setLoc(self.rows[row], col)
                        sqObj.setType('B')
                        self.board[row][col] = sqObj
                    else:
                        sqObj.setLoc(self.rows[row], col)
                        sqObj.setType('R')
                        self.board[row][col] = sqObj
    
    def removePC(self, piece):
        pieceLoc = piece.getLoc()
        print("\n{} deleted from {}{}!\n".format(piece.getType(), pieceLoc[0], pieceLoc[1]))
        pieceIdx = self.activePieces.index(piece)
        del self.activePieces[pieceIdx]
        self.renderBoard()

    def setPC2Des(self, piece, destination):
        pcLoc = piece.getLoc()
        desRow = self.rows.index(destination[0])

        print("\n{} moved from {}{} to {}{}".format(piece.getType(), pcLoc[0], pcLoc[1], destination[0], destination[1]))

        if desRow == 1 and piece.getType() == 'o':
            print("\nKinged! o to O\n")
            piece.setType("O")
            self.nextplayer = "x"
        elif desRow == 8 and piece.getType() == 'x':
            print("\nKinged! x to X\n")
            piece.setType("X")
            self.nextplayer = "o"

        pieceIdx = self.activePieces.index(piece)
        piece.setLoc(destination[0], destination[1])
        self.activePieces[pieceIdx] = piece
    
    def wrongMove(self, source, destination):
        print("\nWrong move! {}{} to {}{}\n".format(source[0], source[1], destination[0], destination[1]))
    
    def checkJump(self, piece):
        pcType = piece.getType()
        pcLoc = piece.getLoc()
        found = False

        if pcType == "x":
            row = self.rows.index(pcLoc[0])
            col = pcLoc[1]
       
            positions = [[row+2, col+2], [row+2, col-2]]
            for p in positions:
                if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9:
                    if self.board[p[0]][p[1]].getType() == "B":
                        rowAvg = int((row+p[0])/2)
                        colAvg = int((col+p[1])/2)

                        oPiece = self.board[rowAvg][colAvg].getType()
                        if oPiece == "o" or oPiece == "O":
                            found = True
                            break
        elif pcType == "o":
            row = self.rows.index(pcLoc[0])
            col = pcLoc[1]
            positions = [[row-2, col+2], [row-2, col-2]]
            for p in positions:
                if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9:
                    if self.board[p[0]][p[1]].getType() == "B":
                        rowAvg = int((row+p[0])/2)
                        colAvg = int((col+p[1])/2)
               
                        oPiece = self.board[rowAvg][colAvg].getType()
                        if oPiece == "x" or oPiece == "X":
                            found = True
                            break
        elif pcType == "X" or pcType == "O":
            row = self.rows.index(pcLoc[0])
            col = pcLoc[1]
            positions = [[row-1, col-2], [row-2, col+2], [row+2, col-2], [row+2, col+2]]
            for p in positions:
                if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9:
                    if self.board[p[0]][p[1]].getType() == "B":
                        rowAvg = int((row+p[0])/2)
                        colAvg = int((col+p[1])/2)
    
                        if pcType == "X":
                            oPiece = self.board[rowAvg][colAvg].getType()
                            if oPiece == "o" or oPiece == "O":
                                found = True
                                break
                        else:
                            oPiece = self.board[rowAvg][colAvg].getType()
                            if oPiece == "x" or oPiece == "X":
                                found = True
                                break
        return found

    def jump(self, player, piece, source, destination):
        source[1] = int(source[1])
        destination[1] = int(destination[1])
        rowAvg = int((self.rows.index(destination[0]) + self.rows.index(source[0]))/2)
        colAvg = int((destination[1] + source[1])/2)
        oppPlayer = "o" if player == "x" else "x"

        oPiece = self.board[rowAvg][colAvg]
        if oPiece.getType() == oppPlayer or oPiece.getType() == oppPlayer.upper():
            self.nextplayer = oppPlayer
            self.setPC2Des(piece, destination)
            self.removePC(oPiece)
        else:
            self.wrongMove(source, destination)
            self.nextplayer = player
    
    def checkMove(self, player, moves):
        valid = True
        
        start = moves[0].split(",")
        startSource =  start[0].split("-")
        startDes = start[1].split("-")

        if self.board[self.rows.index(startSource[0])][int(startSource[1])].getType() != player:
            valid = False

        if valid:
            if len(moves) == 1:
                if self.board[self.rows.index(startDes[0])][int(startDes[1])].getType() != "B":
                    valid = False
            else:
                for move in moves:
                    positions = move.split(",")
                    source = positions[0].split("-")
                    destination = positions[1].split("-")
                    if self.board[self.rows.index(destination[0])][int(destination[1])].getType() == "B":
                        rowAvg = int((self.rows.index(destination[0]) + self.rows.index(source[0]))/2)
                        colAvg = int((int(destination[1]) + int(source[1]))/2)
                        oppPlayer = "o" if player == "x" else "x"
                        if self.board[rowAvg][colAvg].getType() == oppPlayer and int(source[1]) != colAvg:
                            if not valid:
                                valid = False
                        else:
                            valid = False
                    else:
                        valid = False

        if valid:
            for move in moves:
                positions = move.split(",")
                source = positions[0].split("-")
                destination = positions[1].split("-")
                self.nextplayer = self.movePC(player, source, destination)        
        else:
            print("Not a valid move. Try again!")
            self.nextplayer = player
        
        return self.nextplayer
            

    def movePC(self, player, source, destination):
        try:
            source[1] = int(source[1])
            destination[1] = int(destination[1])

            piece = self.board[self.rows.index(source[0])][source[1]]
            pieceType = piece.getType()
            if player != pieceType.lower():
                self.wrongMove(source, destination)
                self.nextplayer = player
                return
            
            rowDiff = abs(self.rows.index(destination[0]) - self.rows.index(source[0]))
            colDiff = abs(destination[1] - source[1])
            
            if pieceType == "x":
                if destination[0] > source[0] and self.board[self.rows.index(destination[0])][destination[1]].getType() == "B":
                    if rowDiff == 1 and colDiff == 1:
                        self.nextplayer = "o"
                        self.setPC2Des(piece, destination)
                        self.renderBoard()
                    elif rowDiff == 2 and colDiff == 2:
                        self.jump(player, piece, source, destination)
                    else:
                        self.wrongMove(source, destination)
                        self.nextplayer = "x"
                else:
                    self.wrongMove(source, destination)
                    self.nextplayer = "x"
            elif pieceType == "X":
                if rowDiff == 1 and colDiff == 1:
                    self.nextplayer = "o"
                    self.setPC2Des(piece, destination)
                    self.renderBoard()
                elif rowDiff == 2 and colDiff == 2:
                    self.jump(player, piece, source, destination)
                else:
                    self.wrongMove(source, destination)
                    self.nextplayer = "x"
            elif pieceType == "O":
                if rowDiff == 1 and colDiff == 1:
                    self.nextplayer = "x"
                    self.setPC2Des(piece, destination)
                    self.renderBoard()
                elif rowDiff == 2 and colDiff == 2:
                    self.jump(player, piece, source, destination)
                else:
                    self.wrongMove(source, destination)
                    self.nextplayer = "o"
            elif pieceType == "o":
                if destination[0] < source[0] and self.board[self.rows.index(destination[0])][destination[1]].getType() == "B":
                    if rowDiff == 1 and colDiff == 1:
                        self.nextplayer = "x"
                        self.setPC2Des(piece, destination)
                        self.renderBoard()
                    elif rowDiff == 2 and colDiff == 2:
                        self.jump(player, piece, source, destination)
                    else:
                        self.wrongMove(source, destination)
                        self.nextplayer = "o"
                else:
                    self.wrongMove(source, destination)
                    self.nextplayer = "o"
        except:
            self.nextplayer = player
            print("Something went wrong! Try again.") 
        
        return self.nextplayer
        
    
    #This functions prints the checker board
    def printBoard(self):
        print("\n------CHECKER BOARD--------")
        for row in range(9):
            for col in range(9):
                if isinstance(self.board[row][col], str) or isinstance(self.board[row][col], int):
                    print(self.board[row][col], end=" ")
                else:
                    print(self.board[row][col].getType(), end=" ")
                    
            print()
        print("---------------------------")
    
    def getPCs(self):
        print("---Active Pieces---")
        for piece in self.activePieces:
            print("{}: {}".format(piece.getType(), piece.getLoc()))
    
    def isGameOver(self):
        xCount = 0
        oCount = 0
        xKing = 0
        oKing = 0
        xJump = False
        oJump = False
        xMove = False
        oMove = False
        gameOver = False
        whoWon = "?"

        for piece in self.activePieces:
            pcLoc = piece.getLoc()
            row = self.rows.index(pcLoc[0])
            col = pcLoc[1]

            if piece.getType() == "x":
                if self.checkJump(piece):
                    xJump = True

                pos = [[row+1, col-1], [row+1, col+1]]
                for p in pos:
                    if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9:
                        if self.board[p[0]][p[1]].getType() == "B":
                            xMove = True

                xCount += 1
            elif piece.getType() == "o":
                if self.checkJump(piece):
                    oJump = True
                
                pos = [[row-1, col-1], [row-1, col+1]]
                for p in pos:
                    if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9:
                        if self.board[p[0]][p[1]].getType() == "B":
                            oMove = True

                oCount += 1
            elif piece.getType() == "X" or piece.getType() == "O":
                pos = [[row-1, col-2], [row-2, col+2], [row+2, col-2], [row+2, col+2]]
                for p in pos:
                    if p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9:
                        if self.board[p[0]][p[1]].getType() == "B":
                            if piece.getType() == "X":
                                xMove = True
                            else:
                                oMove = True
                if piece.getType() == "X":
                    if self.checkJump(piece):
                        xJump = True
                    xCount += 1
                    xKing += 1
                else:
                    if self.checkJump(piece):
                        oJump = True
                    oCount += 1
                    oKing += 1
        
        if xCount < 1 and xJump == False and xMove == False:
            whoWon = "o"
            gameOver = True
        elif oCount < 1 and oJump == False and oMove == False:
            whoWon = "x"
            gameOver = True
        
        print("\n---Pieces---")
        print("x available: {}, King: {}".format(xCount, xKing))
        print("o available: {}, King: {}".format(oCount, oKing))
        print("-------------")
        
        return [gameOver, whoWon]
    

