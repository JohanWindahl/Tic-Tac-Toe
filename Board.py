from __future__ import print_function
from random import randint
from random import shuffle
from copy import deepcopy
from GameEngine import GameEngine


class Board:

    def __init__(self):
        self.board = [0] * 9
        self.winningCombinations = (
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        )
        self.playerMoves = [5, 4]

    '''
    This function updates the board.
    Param: move (int) the move by the player or the AI
    Param: player (int) the current player
    '''
    def updateBoard(self, move, player):
        self.board[move-1] = player
        return self

    '''
    This function returns the board updated with the new AI move. Depending on the difficulty chosen
    different AIs will be used.
    Param: AIlevel (int) the difficulty of the AI, can be a number between 1 and 3
    Param: player (int) who the current player is, should be either the number 1 or 2
    Return: board (list). If invalid player or AIlevel function returns 0
    '''

    def AImove(self, AIlevel, player):
        AI = GameEngine()
        if player != 1 and player != 2:
            return 0

        if int(AIlevel) == 1:
            self.updateBoard(AI.getAImove1(self), player)
            return self.board
        elif int(AIlevel) == 2:
            self.updateBoard(AI.getAImove2(player, self), player)
            return self.board
        elif int(AIlevel) == 3:
            self.updateBoard(AI.getAImove3(player, self), player)
            return self.board
        else:
            return 0

    '''
    This function returns the board updated with the new move. If the move or the player is invalid
    -1 will be returned.
    Param: move (int) the move the player choose to make, should be a number between 1 and 9
    Param: player (int) who the current player is, should be either the number 1 or 2
    Return: board (list)
    '''
    def playerMove(self, move, player):
        if player != 1 and player != 2:
            return -1

        if not self.checkValidMove(move):
            return -1
        else:
            self.updateBoard(move, player)
        return self.board




    '''
    This function initiates the board.
    Return: board (list)
    '''
    def initiateGameState(self):
        board = [0] * 9
        return board


    '''
    This function checks if any player has won
    Return: 0 if no winner, 1 or 2 if winner
    '''
    def checkWinner(self):
        for combination in self.winningCombinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == 1:
                return 1
            elif self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == 2:
                return 2
        return 0

    '''
    This function checks if the move is valid.
    Return: Bool
    '''
    def checkValidMove(self, move):
        if move not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        elif self.board[move-1] != 0:
           return False
        return True



    def anySpaceLeft(self):
        """
        Checks if there is zeros in self.board
        :return: True if there is a zero in self.board otherwise False
        """
        for i in range(0, 9):
            if self.board[i] == 0:
                return True
        return False

    """
    Prints the board
    return:
    """
    def printBoard(self):

      print("====== Game Platform ======")
      print("       -------------")
      print("       | " + self.checkBoard(0) + " | " + self.checkBoard(1) + " | " + self.checkBoard(2) + " |")
      print("       -------------")
      print("       | " + self.checkBoard(3) + " | " + self.checkBoard(4) + " | " + self.checkBoard(5) + " |")
      print("       -------------")
      print("       | " + self.checkBoard(6) + " | " + self.checkBoard(7) + " | " + self.checkBoard(8) + " |")
      print("       -------------")
      print("===========================\n")


    def setBoard(self,newboard):
        """
        Changes the current board into a new board. Used in the testing only
        :param newboard: The board (int[9]) that will be changed into
        """
        self.board = newboard

    def checkBoard(self, position):
        if self.board[position] == 0:
            return " "
        elif self.board[position] == 1:
            return "X"
        elif self.board[position] == 2:
            return "O"
        else:
            return ""

    def print(self):
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])
        return False
