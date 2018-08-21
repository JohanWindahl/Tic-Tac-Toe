from random import randint
from random import shuffle
from copy import deepcopy


class GameEngine:

    '''
    This function simulates an easy AI level and generates next move on a given board.
    Param: player (int) who the current player is, should be either the number 1 or 2
    Return: move (int) (1-9)
    '''


    def getAImove1(self, board):
        while (board.anySpaceLeft()):
            returnMove = randint(1, 9)
            if board.checkValidMove(returnMove):
                return returnMove
        return 0


    '''
    This function simulates an intermediate AI level and generates next move on a given board.
    Param: player (int) who the current player is, should be either the number 1 or 2
    Return: move (int) (1-9)
    '''


    def getAImove2(self, player,board):
        if player == 1:
            notPlayer = 2
        elif player == 2:
            notPlayer = 1
        else:
            return 0

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i):
                boardCopy.updateBoard(i, player)
                if boardCopy.checkWinner():
                    # print("winning")
                    return i

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i):
                boardCopy.updateBoard(i, notPlayer)
                if boardCopy.checkWinner():
                    # print("blocking")
                    return i

        possibleMoves = [5, 1, 3, 7, 9, 2, 4, 6, 8]
        shuffle(possibleMoves)

        for i in possibleMoves:
            if board.checkValidMove(i):
                return i

        return 0


    '''
    This function checks if a move can make player 1 or player 2 win
    Param: player (int) who the current player is, should be either the number 1 or 2
    Param: i (int) location to check if it can make a win
    Return: True or False depending on if the checked location can make it win
    '''


    def checkWinMove(self, board, player, i):
        boardCopy = deepcopy(board)
        ##player eller notPlayer
        if player == 1:
            boardCopy.board[i-1] = player
            return player == 1 and boardCopy.checkWinner() == 1
        elif player == 2:
            boardCopy.board[i-1] = player
            return player == 2 and boardCopy.checkWinner() == 1


    '''
    This function determines if a move opens up a fork
    Param: player (int) who the current player is, should be either the number 1 or 2
    Param: i (int) location to check if it can make a win
    Return: move (int) (1-9)
    '''


    def checkForkMove(self, board, player, i):
        # Determines if a move opens up a fork opportunity
        boardCopy = deepcopy(board)
        boardCopy.board[i-1] = player
        winningMoves = 0
        for j in range(1, 10):
            if self.checkWinMove(boardCopy, player, j) and boardCopy.checkValidMove(j):
                winningMoves += 1
                return winningMoves >= 2


    '''
    This function simulates an impossible AI level and generates next move on a given board.
    Param: player (int) who the current player is, should be either the number 1 or 2
    Return: move (int) (1-9)
    '''


    def getAImove3(self, player,board):
        if player == 1:
            notPlayer = 2
        elif player == 2:
            notPlayer = 1
        else:
            return 0

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i):
                boardCopy.updateBoard(i, player)
                if boardCopy.checkWinner():
                    # print("winning")
                    return i

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i):
                boardCopy.updateBoard(i, notPlayer)
                if boardCopy.checkWinner():
                    # print("blocking")
                    return i

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i) and self.checkForkMove(boardCopy, player, i):
                return i

        for i in range(1, 10):
            boardCopy = deepcopy(board)
            if boardCopy.checkValidMove(i) and self.checkForkMove(boardCopy, notPlayer, i):
                return i

        middle = [5]
        cornerMoveList = [1, 3, 7, 9]
        edgeMoveList = [2, 4, 6, 8]

        shuffle(cornerMoveList)
        shuffle(edgeMoveList)

        if self.numberOfFilledSquares(board) == 0:
            return cornerMoveList[0]

        possibleMoves = middle + cornerMoveList + edgeMoveList

        for i in possibleMoves:
            if board.checkValidMove(i):
                return i

        return 0


    '''
    This function checks the board for how many squares that are not used
    Return: square (int)
    '''

    def numberOfFilledSquares(self,board):
        square = 0
        for i in range(0, 9):
            if board.board[i]!=0:
                square=square+1
        return square

