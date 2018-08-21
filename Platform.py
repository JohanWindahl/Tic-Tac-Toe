from Board import Board
from Player import Player
import time
from random import randint


class Platform:

    def __init__(self, player1, player2):

        self.players = [player1, player2]
        self.playerTurn = 1
        self.gameState = Board()

    '''
    Main loop
    returns winner name or 0 if tie
    '''
    def startGame(self):
        winner = 0
        if self.players[0].getIsAI() and self.players[1].getIsAI():
            winner = self.AIvsAI()
            return winner

        self.printBoardHelp()
        print("To place a move, enter the number corresponding to the position on the board")
        print("Press q to quit the game\n")
        time.sleep(2)

        while True:
            print(self.players[0].name + ", moves left: " + "X " * self.gameState.playerMoves[0])
            print(self.players[1].name + ", moves left: " + "O " * self.gameState.playerMoves[1])
            self.gameState.printBoard()
            if not self.players[self.playerTurn-1].getIsAI():

                inputMove = self.askForMove(self.players[self.playerTurn-1].name, "Choose your move: ")
                print("\n")
                if inputMove in ('q', 'Q', 'quit', 'Quit'):
                    print(self.players[self.playerTurn-1].name, "has quit the game")
                    print(self.players[winner-1].name + " wins the game!")
                    print("Going back to menu...")
                    time.sleep(2)

                    # What should be returned? should other player win?
                    break
                while True:
                    moveIsValid = self.gameState.checkValidMove(inputMove)
                    if moveIsValid:  # or inputMove == 0:
                        break
                    else:
                        inputMove = self.askForMove(self.players[self.playerTurn-1].name, "Invalid move, input a new move: ")
                self.gameState.playerMove(inputMove, self.playerTurn)
                self.gameState.playerMoves[self.playerTurn-1] -= 1
            else:
                self.gameState.AImove(self.players[self.playerTurn-1].getAIlevel(), self.playerTurn)
                self.gameState.playerMoves[self.playerTurn - 1] -= 1
            winner = self.gameState.checkWinner()
            if winner != 0:
                self.gameState.printBoard()
                print("The Winner is " + self.players[winner-1].name + "!")
                print("Congratulations!\n")
                print("Going back to menu...")
                time.sleep(3)
                winner = self.players[winner-1].name
                break
            if not self.gameState.anySpaceLeft():
                print("The Game Ended in a Tie!")
                break
            if self.playerTurn == 1:
                self.playerTurn = 2
            elif self.playerTurn == 2:
                self.playerTurn = 1
            else:
                print("Something has gone wrong while switching players")
        return winner

    def askForMove(self, player, string):
        while True:
            inputString = input(str(player)+", "+string)
            if len(inputString) > 0 and inputString in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return int(inputString)
            elif len(inputString) > 0 and inputString in ['q', 'Q', 'quit', 'Quit']:
                return inputString
            else:
                print("Invalid input, should be 1-9")

    def printBoardHelp(self):
        print("===== Board Positions ====")
        print("       -------------     ")
        print("       | 1 | 2 | 3 |     ")
        print("       -------------     ")
        print("       | 4 | 5 | 6 |     ")
        print("       -------------     ")
        print("       | 7 | 8 | 9 |     ")
        print("       -------------     ")
        print("========================== \n")

    def AIvsAI(self):
        # Requires the possibility to fetch AI level from AI
        if self.players[0].AIlevel > self.players[1].AIlevel:
            return self.players[0].name
        elif self.players[0].AIlevel < self.players[1].AIlevel:
            return self.players[1].name
        else:
            winningAI = randint(1, 2)
            if winningAI == 1:
                return self.players[0].name
            elif winningAI == 2:
                return self.players[1].name
            else:
                return 0
