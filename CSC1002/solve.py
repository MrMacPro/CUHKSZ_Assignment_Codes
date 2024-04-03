DIRECTION_TO_MOVEMENT=((0, -1), (0, 1), (-1, 0), (1, 0))
def move(direction, puzzle):    #0:up 1:down 2:left 3:right
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                try:
                    puzzle[i][j], puzzle[i+DIRECTION_TO_MOVEMENT[direction]][j+DIRECTION_TO_MOVEMENT[direction]]=puzzle[i+DIRECTION_TO_MOVEMENT[direction]][j+DIRECTION_TO_MOVEMENT[direction]], puzzle[i][j]
                except IndexError:
                    raise IndexError("Out of puzzle")
    return puzzle 
              
def solve(puzzle):
    for direction in range(4):
        try:
            puzzle = move(direction, puzzle)
            solve(puzzle)
        except:
            pass