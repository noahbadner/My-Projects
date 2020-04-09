import numpy as np
from Sudoku import SudokuGame

example_game = np.asmatrix([[3, 0, 4, 0],
                            [0, 1, 0, 2],
                            [0, 4, 0, 3],
                            [2, 0, 1, 0]])

solved_game = np.asmatrix([[2, 1, 4, 3],
                           [4, 3, 1, 2],
                           [1, 2, 3, 4],
                           [3, 4, 2, 1]])


class FourdokuGame(SudokuGame):
    def __init__(self, input_matrix=None):
        self._game_matrix = np.zeros([4, 4], int)
        self._locked_cells = []
        self.dimension = 4
        self.guesses = 0
        self.moves = 0

        if input_matrix is not None:
            self._game_matrix = input_matrix
            for i in range(4):
                for j in range(4):
                    if self._get_cell([i, j]) != 0:
                        self._locked_cells.append((i, j))

    def _subgrid_collision(self, value, position):
        x = 2
        while position[0] >= x:
            x += 2
        sg_rows = [(x - 2), x]

        y = 2
        while position[1] >= y:
            y += 2
        sg_cols = [(y - 2), y]

        subgrid = self._game_matrix[sg_rows[0]:sg_rows[1], sg_cols[0]:sg_cols[1]]

    def reset(self):
        self.moves = 0
        self.guesses = 0
        for i in range(4):
            for j in range(4):
                if (i, j) not in self._locked_cells:
                    self.clear_cell((i, j))

    def check_solution(self):
        if 0 in self._game_matrix:
            return False
        else:
            for i in range(4):
                for j in range(4):
                    pos = [i, j]
                    if self._check_cell(pos):
                        print(f"Collision at {pos}")
                        return False
            print(f"Solved in {self.guesses} guesses and {self.moves} moves.")
            return True
