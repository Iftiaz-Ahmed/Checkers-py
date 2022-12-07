import game as g

player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")

gameObj = g.Game(player1, player2)
gameObj.runGame()