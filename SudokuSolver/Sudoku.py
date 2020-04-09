import numpy as np

example_game = np.asmatrix([[0, 8, 0, 0, 7, 0, 3, 0, 5],
                            [2, 5, 7, 0, 0, 8, 0, 0, 0],
                            [0, 0, 0, 0, 0, 5, 0, 7, 0],
                            [4, 0, 9, 3, 6, 0, 0, 0, 0],
                            [0, 6, 1, 0, 0, 0, 0, 4, 0],
                            [3, 7, 8, 0, 1, 0, 0, 2, 0],
                            [0, 3, 0, 0, 0, 1, 9, 0, 4],
                            [7, 0, 5, 0, 0, 0, 1, 8, 2],
                            [0, 0, 6, 4, 8, 2, 5, 0, 0]])

solved_game = np.asmatrix([[8, 2, 7, 1, 5, 4, 3, 9, 6],
                           [9, 6, 5, 3, 2, 7, 1, 4, 8],
                           [3, 4, 1, 6, 8, 9, 7, 5, 2],
                           [5, 9, 3, 4, 6, 8, 2, 7, 1],
                           [4, 7, 2, 5, 1, 3, 6, 8, 9],
                           [6, 1, 8, 9, 7, 2, 4, 3, 5],
                           [7, 8, 6, 2, 3, 5, 9, 1, 4],
                           [1, 5, 4, 7, 9, 6, 8, 2, 3],
                           [2, 3, 9, 8, 4, 1, 5, 6, 7]])


class SudokuGame:

    def __init__(self, input_matrix=None):
        self._game_matrix = np.zeros([9, 9], int)
        self._locked_cells = []
        self.dimension = 9
        self.guesses = 0
        self.moves = 0

        if input_matrix is not None:
            self._game_matrix = input_matrix
            for i in range(9):
                for j in range(9):
                    if self._get_cell([i, j]) != 0:
                        self._locked_cells.append((i, j))

    def __str__(self):
        return str(self._game_matrix)

    def _get_cell(self, position):
        return self._game_matrix[position[0], position[1]]

    def _set_cell(self, value, position):
        self._game_matrix[position[0], position[1]] = value

    def _cell_filled(self, position):
        return self._game_matrix[position[0], position[1]] != 0

    def _row_collision(self, value, position):
        return value in self._game_matrix[position[0], :]

    def _column_collision(self, value, position):
        return value in self._game_matrix[:, position[1]]

    def _subgrid_collision(self, value, position):
        x = (position[0] // 3) * 3
        sg_rows = [x, (x + 3)]

        y = (position[1] // 3) * 3
        sg_cols = [y, (y + 3)]

        subgrid = self._game_matrix[sg_rows[0]:sg_rows[1], sg_cols[0]:sg_cols[1]]
        return value in subgrid

    def _check_collision(self, value, position):
        # returns True if there is a collision
        if self._row_collision(value, position):
            # print("Row collision")
            return True
        elif self._column_collision(value, position):
            # print("Column collision")
            return True
        elif self._subgrid_collision(value, position):
            # print("Subgrid collision")
            return True
        else:
            return False

    def _check_cell(self, position):
        current_value = self._get_cell(position)
        self.clear_cell(position)
        collision_check = self._check_collision(current_value, position)
        self._set_cell(current_value, position)
        return collision_check

    def get_cell(self, position):
        return self._get_cell(position)

    def clear_cell(self, position):
        if position in self._locked_cells:
            self._locked_cells.remove(position)
        self._set_cell(0, position)

    def reset(self):
        self.moves = 0
        self.guesses = 0
        for i in range(9):
            for j in range(9):
                if (i, j) not in self._locked_cells:
                    self.clear_cell((i, j))

    def guess(self, value, position):
        self.guesses += 1
        print(f"Guess: {value} at {position}")
        if position in self._locked_cells:
            print(f"{position} is a locked cell.")
            return False
        guess_collision = self._check_collision(value, position)
        if not guess_collision:
            self._set_cell(value, position)
        return not guess_collision

    def check_solution(self):
        if 0 in self._game_matrix:
            return False
        else:
            for i in range(9):
                for j in range(9):
                    pos = [i, j]
                    if self._check_cell(pos):
                        print(f"Collision at {pos}")
                        return False
            print(f"Solved in {self.guesses} guesses and {self.moves} moves.")
            return True
