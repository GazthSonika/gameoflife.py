from random import randint
import copy

class Life(object):

    def __init__(self, board_size=(100, 100), to_birth=3, keep_allive=(2,3)):
        self.board_size = board_size
        self.to_birth = to_birth
        self.keep_allive = keep_allive
        
        self._max_allive = max(keep_allive)
        self._board = self.__get_random_board(board_size)

    def __get_random_board(self, size):
        return [
            [randint(0, 1) for i in xrange(size[1])] for j in xrange(size[0])
        ]

    def set_board_cell(self, x, y, val):
        self._board[x][y] = val

    def get_board(self):
        return self._board

    def __check_allive(self, _x, _y):
        living_cells = 0
        board_check_cell = self._board[_x][_y]

        for x in xrange(_x-1, _x+2):
            if x < 0 or x >= self.board_size[0]:
                continue

            for y in xrange(_y-1, _y+2):
                if y < 0 or y >= self.board_size[1] or x == _x and y == _y:
                    continue

                if self._board[x][y] == 1:
                    living_cells += 1
                    continue

                if board_check_cell == 1 and living_cells > self._max_allive:                
                    return False;
                                
        if living_cells == self.to_birth or (
                board_check_cell == 1 and living_cells in self.keep_allive):
            return True
        return False

    def advance(self):
        bs = self.board_size
        new_board = [[0 for i in xrange(bs[1])] for j in xrange(bs[0])]

        for x in xrange(bs[0]):    
            for y in xrange(bs[1]):                
                new_board[x][y] = 1 if self.__check_allive(x, y) else 0
        
        self._board = copy.copy(new_board)