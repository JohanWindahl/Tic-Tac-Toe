from unittest import TestCase
from GameEngine import GameEngine
from Board import Board

class TestGameEngine(TestCase):
    def test_playerMove(self):
        board = Board()

        self.assertEqual(board.playerMove(1,1), [1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(board.playerMove(9,1), [1, 0, 0, 0, 0, 0, 0, 0, 1])

        #Test invalid moves
        self.assertEqual(board.playerMove(1,2),-1)
        self.assertEqual(board.playerMove(10, 2), -1)
        self.assertEqual(board.playerMove(0, 2), -1)
        self.assertEqual(board.playerMove(1, 1), -1)
        self.assertEqual(board.playerMove(-2, 1), -1)

        # Invalid player
        self.assertEqual(board.playerMove(5, 3), -1)
        self.assertEqual(board.playerMove(5, 0), -1)
        self.assertEqual(board.playerMove(5, -1), -1)

    def test_numberOfFilledSquares(self):
        gameEngine = GameEngine()
        board = Board()

        # Empty board
        self.assertEqual(gameEngine.numberOfFilledSquares(board), 0)

        # One square filled
        board.setBoard([0,0,0,2,0,0,0,0,0])
        self.assertEqual(gameEngine.numberOfFilledSquares(board), 1)

        # All squares filled
        board.setBoard([1,1,2,2,2,1,2,2,1])
        self.assertEqual(gameEngine.numberOfFilledSquares(board), 9)

    def test_AImove(self):
        board = Board()
        gameEngine = GameEngine()

        # Testing different AI levels
        board.setBoard([1, 1, 2, 2, 2, 1, 1, 1, 0])
        self.assertEqual(board.AImove(1, 2), [1, 1, 2, 2, 2, 1, 1, 1, 2])
        self.assertEqual(board.AImove(2, 2), [1, 1, 2, 2, 2, 1, 1, 1, 2])
        self.assertEqual(board.AImove(3, 2), [1, 1, 2, 2, 2, 1, 1, 1, 2])


        # Invalid AIlevel
        board.setBoard([0,0,0,0,0,0,0,0,0])
        self.assertEqual(board.AImove(4,1), 0)
        self.assertEqual(board.AImove(0, 1), 0)
        self.assertEqual(board.AImove(-1, 1), 0)

        # Invalid player
        board.setBoard([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(board.AImove(1, 3), 0)
        self.assertEqual(board.AImove(1, 0), 0)
        self.assertEqual(board.AImove(1, -1), 0)


    def test_getAImove1(self):
        board = Board()
        gameEngine = GameEngine()

        # Only one available move
        board.setBoard([1, 1, 2, 2, 2, 1, 1, 1, 0])
        self.assertEqual(gameEngine.getAImove1(board), 9)
        self.assertEqual(gameEngine.getAImove1(board), 9)

        # Full board
        board.setBoard([1, 1, 2, 2, 2, 1, 1, 1, 2])
        self.assertEqual(gameEngine.getAImove1(board), 0)
        self.assertEqual(gameEngine.getAImove1(board), 0)

        # Empty board
        board.setBoard([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertTrue(isinstance(gameEngine.getAImove1(board), int))
        self.assertTrue(isinstance(gameEngine.getAImove1(board), int))

    def test_getAImove2(self):
        board = Board()
        gameEngine = GameEngine()

        # Only one available move
        board.setBoard([1, 1, 2, 2, 2, 1, 1, 1, 0])
        self.assertEqual(gameEngine.getAImove2(1,board), 9)
        self.assertEqual(gameEngine.getAImove2(2,board), 9)

        # Full board
        board.setBoard([1, 1, 2, 2, 2, 1, 1, 1, 2])
        self.assertEqual(gameEngine.getAImove2(1,board), 0)
        self.assertEqual(gameEngine.getAImove2(2,board), 0)

        # Empty board
        board.setBoard([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertTrue(isinstance(gameEngine.getAImove2(1,board), int))
        self.assertTrue(isinstance(gameEngine.getAImove2(2,board), int))

        # Invalid player
        board.setBoard([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(gameEngine.getAImove2(3, board), 0)

        # Both chance of winning
        board.setBoard([1, 1, 0, 2, 2, 0, 1, 0, 0])
        self.assertEqual(gameEngine.getAImove2(1, board), 3)
        self.assertEqual(gameEngine.getAImove2(2, board), 6)

        # P1 chance of winning
        board.setBoard([1, 1, 0, 2, 2, 1, 1, 0, 0])
        self.assertEqual(gameEngine.getAImove2(1, board), 3)
        self.assertEqual(gameEngine.getAImove2(2, board), 3)

        # P2 chance of winning
        board.setBoard([1, 1, 2, 2, 2, 0, 1, 0, 0])
        self.assertEqual(gameEngine.getAImove2(1, board), 6)
        self.assertEqual(gameEngine.getAImove2(2, board), 6)

        # P1 chance of winning diagonally
        board.setBoard([1, 0, 2, 0, 1, 0, 2, 0, 0])
        self.assertEqual(gameEngine.getAImove2(1, board), 9)
        self.assertEqual(gameEngine.getAImove2(2, board), 9)

    def test_getAImove3(self):
        board = Board()
        gameEngine = GameEngine()

        # Only one available move
        board.setBoard([1, 1, 2, 2, 2, 1, 1, 1, 0])
        self.assertEqual(gameEngine.getAImove3(1, board), 9)
        self.assertEqual(gameEngine.getAImove3(2, board), 9)

        # Full board
        board.setBoard([1, 1, 2, 2, 2, 1, 1, 1, 2])
        self.assertEqual(gameEngine.getAImove3(1, board), 0)
        self.assertEqual(gameEngine.getAImove3(2, board), 0)

        # Empty board should place in random corner
        board.setBoard([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertTrue(gameEngine.getAImove3(1, board) in [1, 3, 7, 9])
        self.assertTrue(gameEngine.getAImove3(2, board) in [1, 3, 7, 9])

        # Invalid player
        board.setBoard([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(gameEngine.getAImove3(3, board), 0)

        # Both chance of winning
        board.setBoard([1, 1, 0, 2, 2, 0, 1, 0, 0])
        self.assertEqual(gameEngine.getAImove3(1, board), 3)
        self.assertEqual(gameEngine.getAImove3(2, board), 6)

        # P1 chance of winning
        board.setBoard([1, 1, 0, 2, 2, 1, 1, 0, 0])
        self.assertEqual(gameEngine.getAImove3(1, board), 3)
        self.assertEqual(gameEngine.getAImove3(2, board), 3)

        # P2 chance of winning
        board.setBoard([1, 1, 2, 2, 2, 0, 1, 0, 0])
        self.assertEqual(gameEngine.getAImove3(1, board), 6)
        self.assertEqual(gameEngine.getAImove3(2, board), 6)

        # P1 chance of winning diagonally
        board.setBoard([1, 0, 2, 0, 1, 0, 2, 0, 0])
        self.assertEqual(gameEngine.getAImove3(1, board), 9)
        self.assertEqual(gameEngine.getAImove3(2, board), 9)



    def test_updateBoard(self):
        board1 = Board()
        board2 = Board()

        #board(move.player)

        #test first move
        board1.updateBoard(1, 1)
        self.assertEqual(board1.board, [1, 0, 0, 0, 0, 0, 0, 0, 0])
        board2.updateBoard(1, 2)
        self.assertEqual(board2.board, [2, 0, 0, 0, 0, 0, 0, 0, 0])

        #test invalid move
#        self.assertEqual(board1.board(1,2), 0)
 #       self.assertEqual(board2.board(1,1), 0)
  #      self.assertEqual(board1.board(1,1), 0)
   #     self.assertEqual(board2.board(1,2), 0)

        #test evey spot pl.1
        board1.updateBoard(2, 1)
        self.assertEqual(board1.board, [1, 1, 0, 0, 0, 0, 0, 0, 0])
        board1.updateBoard(3, 1)
        self.assertEqual(board1.board, [1, 1, 1, 0, 0, 0, 0, 0, 0])
        board1.updateBoard(4, 1)
        self.assertEqual(board1.board, [1, 1, 1, 1, 0, 0, 0, 0, 0])
        board1.updateBoard(5, 1)
        self.assertEqual(board1.board, [1, 1, 1, 1, 1, 0, 0, 0, 0])
        board1.updateBoard(6, 1)
        self.assertEqual(board1.board, [1, 1, 1, 1, 1, 1, 0, 0, 0])
        board1.updateBoard(7, 1)
        self.assertEqual(board1.board, [1, 1, 1, 1, 1, 1, 1, 0, 0])
        board1.updateBoard(8, 1)
        self.assertEqual(board1.board, [1, 1, 1, 1, 1, 1, 1, 1, 0])
        board1.updateBoard(9, 1)
        self.assertEqual(board1.board, [1, 1, 1, 1, 1, 1, 1, 1, 1])

        #test every spot pl.2
        board2.updateBoard(2, 2)
        self.assertEqual(board2.board, [2, 2, 0, 0, 0, 0, 0, 0, 0])
        board2.updateBoard(3, 2)
        self.assertEqual(board2.board, [2, 2, 2, 0, 0, 0, 0, 0, 0])
        board2.updateBoard(4, 2)
        self.assertEqual(board2.board, [2, 2, 2, 2, 0, 0, 0, 0, 0])
        board2.updateBoard(5, 2)
        self.assertEqual(board2.board, [2, 2, 2, 2, 2, 0, 0, 0, 0])
        board2.updateBoard(6, 2)
        self.assertEqual(board2.board, [2, 2, 2, 2, 2, 2, 0, 0, 0])
        board2.updateBoard(7, 2)
        self.assertEqual(board2.board, [2, 2, 2, 2, 2, 2, 2, 0, 0])
        board2.updateBoard(8, 2)
        self.assertEqual(board2.board, [2, 2, 2, 2, 2, 2, 2, 2, 0])
        board2.updateBoard(9, 2)
        self.assertEqual(board2.board, [2, 2, 2, 2, 2, 2, 2, 2, 2])
  #test invalid inputs
  #      self.assertEqual(board1.board(1,0), 0)
  #      self.assertEqual(board1.board(1,3), 0)
   #     self.assertEqual(board1.board(0,2), 0)
    #    self.assertEqual(board1.board(9,2), 0)



    def test_checkWinner(self):
        board = Board()

        # Horisontal win tests

        board.setBoard([1, 1, 1, 0, 0, 0, 0, 0, 0])
        self.assertEqual(board.checkWinner(), 1)

        board.setBoard([2, 2, 2, 0, 0, 0, 0, 0, 0])
        self.assertEqual(board.checkWinner(), 2)

        board.setBoard([0, 0, 0, 1, 1, 1, 0, 0, 0])
        self.assertEqual(board.checkWinner(), 1)

        board.setBoard([0, 0, 0, 2, 2, 2, 0, 0, 0])
        self.assertEqual(board.checkWinner(), 2)

        board.setBoard([0, 0, 0, 0, 0, 0, 1, 1, 1])
        self.assertEqual(board.checkWinner(), 1)

        board.setBoard([0, 0, 0, 0, 0, 0, 2, 2, 2])
        self.assertEqual(board.checkWinner(), 2)

        # Diagonal win tests
        board.setBoard([1, 0, 0, 0, 1, 0, 0, 0, 1])
        self.assertEqual(board.checkWinner(), 1)

        board.setBoard([2, 0, 0, 0, 2, 0, 0, 0, 2])
        self.assertEqual(board.checkWinner(), 2)

        board.setBoard([0, 0, 2, 0, 2, 0, 2, 0, 0])
        self.assertEqual(board.checkWinner(), 2)

        board.setBoard([0, 0, 1, 0, 1, 0, 1, 0, 0])
        self.assertEqual(board.checkWinner(), 1)

        # Vertical win tests
        board.setBoard([1, 0, 0, 1, 0, 0, 1, 0, 0])
        self.assertEqual(board.checkWinner(), 1)

        board.setBoard([2, 0, 0, 2, 0, 0, 2, 0, 0])
        self.assertEqual(board.checkWinner(), 2)

        board.setBoard([0, 1, 0, 0, 1, 0, 0, 1, 0])
        self.assertEqual(board.checkWinner(), 1)

        board.setBoard([0, 2, 0, 0, 2, 0, 0, 2, 0])
        self.assertEqual(board.checkWinner(), 2)

        board.setBoard([0, 0, 1, 0, 0, 1, 0, 0, 1])
        self.assertEqual(board.checkWinner(), 1)

        board.setBoard([0, 0, 2, 0, 0, 2, 0, 0, 2])
        self.assertEqual(board.checkWinner(), 2)

        # Non wining tests

        board.setBoard([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(board.checkWinner(), 0)

        board.setBoard([0, 1, 2, 0, 1, 0, 0, 2, 0])
        self.assertEqual(board.checkWinner(), 0)

        board.setBoard([1, 1, 2, 2, 2, 1, 1, 2, 1])
        self.assertEqual(board.checkWinner(), 0)

        board.setBoard([2, 2, 1, 1, 1, 2, 2, 1])
        self.assertEqual(board.checkWinner(), 0)


    def test_checkValidMove(self):
        board = Board()
        #checkValidMove(self,move) --> Bool
        #Testing valid inputs in a empty board
        self.assertEqual(board.checkValidMove(1), True)
        self.assertEqual(board.checkValidMove(2), True)
        self.assertEqual(board.checkValidMove(3), True)
        self.assertEqual(board.checkValidMove(4), True)
        self.assertEqual(board.checkValidMove(5), True)
        self.assertEqual(board.checkValidMove(6), True)
        self.assertEqual(board.checkValidMove(7), True)
        self.assertEqual(board.checkValidMove(8), True)
        self.assertEqual(board.checkValidMove(9), True)

        #Testing invalid inputs
        self.assertEqual(board.checkValidMove(10), False)
        self.assertEqual(board.checkValidMove(0), False)
        self.assertEqual(board.checkValidMove(9), True)

        #Testing valid inputs in a non empty board
        board.updateBoard(1,1)
        self.assertEqual(board.checkValidMove(1), False)
        self.assertEqual(board.checkValidMove(2), True)
        board.updateBoard(9,1)
        self.assertEqual(board.checkValidMove(9), False)
        self.assertEqual(board.checkValidMove(8), True)

    def test_anySpaceLeft(self):
        board = Board()

        self.assertEqual(board.anySpaceLeft(),True)
        board.updateBoard(1, 1)
        self.assertEqual(board.anySpaceLeft(),True)
        board.updateBoard(2, 1)
        self.assertEqual(board.anySpaceLeft(),True)
        board.updateBoard(3, 1)
        self.assertEqual(board.anySpaceLeft(),True)
        board.updateBoard(4, 1)
        self.assertEqual(board.anySpaceLeft(),True)
        board.updateBoard(9, 1)
        self.assertEqual(board.anySpaceLeft(),True)
        board.updateBoard(8, 1)
        self.assertEqual(board.anySpaceLeft(),True)
        board.updateBoard(7, 1)

        self.assertEqual(board.anySpaceLeft(),True)
        board.updateBoard(6, 1)

        self.assertEqual(board.anySpaceLeft(),True)

        board.updateBoard(5, 1)
        self.assertEqual(board.anySpaceLeft(),False)

    def allTests(self):
        #self.test_playerMove()
        #self.test_numberOfFilledSquares()
        #self.test_AImove()
        #self.test_getAImove1()
        #self.test_getAImove2()
        #self.test_getAImove3()
        #self.test_updateBoard()
        #self.test_checkWinner()
        self.test_checkValidMove()
        #self.test_anySpaceLeft()

if __name__ == '__main__':
    t = TestGameEngine()
    t.allTests()
