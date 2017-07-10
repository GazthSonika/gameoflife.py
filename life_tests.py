from life import Life
import unittest

class TestLifeLogic(unittest.TestCase):
    def compare_next(self, before, after, name=""):
        life = Life((len(before[0]), len(before)))
        life._board = before
        life.advance()
        board = life.get_board()
        for x in xrange(0, 5):
            for y in xrange(0, 5):  
                self.assertEquals(board[x][y], after[x][y], name)
        return board

    def test_oscilator1(self):
        self.compare_next([
          #before         
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ],[
         #after
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]), "test_oscilator1"

    def test_cube1(self):
        self.compare_next([
          #before         
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],[
         #after
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]), "test_cube1"

if __name__ == '__main__':
    unittest.main()