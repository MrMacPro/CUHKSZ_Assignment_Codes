def solve(puzzle:list):
    memory = [puzzle]
    def recursive_solve(puzzle:list)->None:
        new_puzzle = puzzle.copy()