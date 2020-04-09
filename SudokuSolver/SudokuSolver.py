def solver(sudoku_game_object):
    print("Current game state:")
    print(sudoku_game_object)

    if sudoku_game_object.check_solution():
        return True
    else:
        current_cell = _first_empty_cell(sudoku_game_object)
        for i in range(1, (sudoku_game_object.dimension + 1)):
            if sudoku_game_object.guess(i, current_cell):
                if solver(sudoku_game_object):
                    return True
        sudoku_game_object.clear_cell(current_cell)
        print("Current game state:")
        print(sudoku_game_object)
        return False


def _first_empty_cell(sudoku_game_object):
    for i in range(sudoku_game_object.dimension):
        for j in range(sudoku_game_object.dimension):
            if sudoku_game_object.get_cell((i, j)) == 0:
                return i, j
    return None
