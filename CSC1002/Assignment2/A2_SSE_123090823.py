'''
This is Hanson's sliding puzzle game with GUI.
Python turtle, math, and random libs are used.
Window size is written to be 720*720.
The animation looks good by the way.
'''

#Imports
import turtle
from math import tanh
from random import shuffle, randint

#constants
RAMP = 3
ANIMATION_SPEED = 10
PROMPT_TO_MOVEMENT = ((-1,0),(1,0),(0,-1),(0,1))

#GUI functions
def validate_input(prompt:str, valid)->str: #Prompt users to input only valid inputs
    global s
    while True:
        user_input = s.numinput("size",prompt)
        if user_input in valid:
            return user_input
        else:
            print("Invalid input")

def smooth_animation(t:turtle.Turtle, distance:float, direction:int)->None:    #Smooth animation based on ramp function
    def ramp(x:float)->float:   #tanh ramp function
        return (1/tanh(RAMP)) * tanh(RAMP*x)

    origin = (t.xcor(), t.ycor())
    for i in range(1, int(distance), ANIMATION_SPEED):  #Control animation with difference on position
        target_x = origin[0] - (PROMPT_TO_MOVEMENT[direction][0]) * ramp(i/distance)*distance
        target_y = origin[1] + (PROMPT_TO_MOVEMENT[direction][1]) * ramp(i/distance)*distance
        t.goto(target_x, target_y)
    t.goto(origin[0] - (PROMPT_TO_MOVEMENT[direction][0]) * distance, origin[1] + (PROMPT_TO_MOVEMENT[direction][1]) * distance)    #Solve errors in float->int conversion

def switch(direction)->None:    #Operations on blocks are seen as switching the target block with blank block
    global puzzle
    global turtles
    global current_0_pos

    next_0_pos = [current_0_pos[0] + PROMPT_TO_MOVEMENT[direction][0], current_0_pos[1] + PROMPT_TO_MOVEMENT[direction][1]] #Find target block

    def switch_num(puzzle, current_0_pos:tuple, next_0_pos:tuple, direction)->list: #Switch puzzle memory
        #Switch blocks
        puzzle[current_0_pos[1]][current_0_pos[0]], puzzle[next_0_pos[1]][next_0_pos[0]]\
        = puzzle[next_0_pos[1]][next_0_pos[0]], puzzle[current_0_pos[1]][current_0_pos[0]]

        return puzzle

    def switch_turtle(turtles, current_0_pos:tuple, next_0_pos:tuple, direction)->list: #Display animation and switch turtle objects
        global isAnimating
        
        #Display animation
        isAnimating = True
        turtles[current_0_pos[0]][current_0_pos[1]].goto(turtles[next_0_pos[0]][next_0_pos[1]].xcor(), turtles[next_0_pos[0]][next_0_pos[1]].ycor())
        smooth_animation(turtles[next_0_pos[0]][next_0_pos[1]], 600/board_size + 120/(board_size+1), direction)
        isAnimating = False

        #Switch turtles
        turtles[current_0_pos[0]][current_0_pos[1]], turtles[next_0_pos[0]][next_0_pos[1]]\
        = turtles[next_0_pos[0]][next_0_pos[1]], turtles[current_0_pos[0]][current_0_pos[1]]

        return turtles

    puzzle = switch_num(puzzle, current_0_pos, next_0_pos, direction)
    turtles = switch_turtle(turtles, current_0_pos, next_0_pos, direction)

    current_0_pos = next_0_pos  #Refresh blank position

def index_to_pos(x:float, y:float)->tuple:  #Conversion from index coordinate to pixel coordinate
    pos_x = -360 + (300+600*x)/board_size + 120*(x+1)/(board_size+1)
    pos_y = 360 - (300+600*y)/board_size - 120*(y+1)/(board_size+1)
    return pos_x, pos_y

def pos_to_index(x:float, y:float)->tuple:  #Conversion from pixel coordinate to index coordinate
    index_x = int((x+360) / (600/board_size + 120/(board_size+1)))
    index_y = board_size - 1 - int((y+360) / (600/board_size + 120/(board_size+1)))
    return index_x, index_y

def write_num(nums:list, first_write=False)->None: #Write numbers on blocks
    global puzzle
    global last_puzzle
    global current_0_pos

    if first_write: #Only refresh location and tracer in the first write
        for i in range(board_size):
            for j in range(board_size):
                    nums[i][j].goto(index_to_pos(j, i)[0], index_to_pos(j, i)[1] - font_size)
                    turtle.tracer(1)

    for i in range(board_size):
        for j in range(board_size):
            if puzzle[i][j] != last_puzzle[i][j]:   #Only refresh operated blocks to enhance performance
                nums[i][j].clear()
                nums[i][j].write(puzzle[i][j] if puzzle[i][j] != 0 else '', align="center", font=("Arial", int(font_size), "normal"))

                last_puzzle[i][j] = puzzle[i][j]    #Refresh last puzzle for operate detection

def onclick_hdlr(x:float, y:float)->None:   #Main onclick event handler
    global puzzle
    global counter
    global current_0_pos
    global solved_puzzle
    global nums
    global isAnimating

    if not isAnimating:
        i, j = pos_to_index(x, y)   #Convert mouse click position to index

        try:
            direction = PROMPT_TO_MOVEMENT.index((i-current_0_pos[0], j-current_0_pos[1]))  #Convert index to moving direction (if it is a valid move)
        except ValueError:
            direction = -1

        if direction != -1:
            counter += 1
            switch(direction)   #Operate switch when move is valid
            write_num(nums)     #Refresh numbers

        #Winning detection
        if puzzle == solved_puzzle:
            winning_hdlr(nums, counter)

def winning_hdlr(nums:list, counter:int)->None:
    def winning_text(counter:int)->None:   #Write winning prompt
        global font_size

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(index_to_pos(board_size-1, board_size-1))
        t.write(f"Congratulations!\nYou solved the puzzle in\n {counter} moves!", align="center", font=("Arial", int(font_size/2.5), "normal"))

    global board_size
    global turtles
    global last_puzzle
    for i in range(board_size):
        for j in range(board_size):
            if i == board_size-1 and j == board_size-1:
                turtles[i][j].color("white")    #Leave the blank turtle white
            else:
                turtles[i][j].color("red")      #Change the rest to red
    last_puzzle = [[0 for _ in range(board_size)] for _ in range(board_size)]
    write_num(nums) #Refresh numbers
    winning_text(counter)  #Writing winning prompt

#Non-GUI functions
def disrupt(board_size:int)->tuple: #Disrupt puzzle
    def is_solvable(puzzle):    #Sovability detection
        def count_inversions(arr):
            inv_count = 0
            n = len(arr)
            for i in range(n):
                for j in range(i + 1, n):
                    if arr[i] and arr[j] and arr[i] > arr[j]:
                        inv_count += 1
            return inv_count

        def find_blank_row(puzzle):
            for i in range(len(puzzle)):
                for j in range(len(puzzle)):
                    if puzzle[i][j] == 0:
                        return i
            return -1

        def is_even(n):
            return n % 2 == 0

        size = len(puzzle)
        flattened_puzzle = [val for row in puzzle for val in row]
        inversions = count_inversions(flattened_puzzle)
        blank_row = find_blank_row(puzzle)

        if size % 2 == 0:
            if is_even(blank_row):
                return not is_even(inversions)
            else:
                return is_even(inversions)
        else:
            return is_even(inversions)

    while True:
        #Shuffle random puzzle
        zero_pos = randint(0, board_size-1)
        numbers = list(range(1, board_size**2))
        shuffle(numbers)
        puzzle = [[0 if i == zero_pos and j == zero_pos else numbers.pop(0) for i in range(board_size)] for j in range(board_size)] #Create puzzle

        if is_solvable(puzzle): #Check sovability
            return puzzle, (zero_pos, zero_pos)

#Init functions
def init_screen()->turtle.Screen:
    s = turtle.Screen()
    s.colormode(255)
    s.setup(720,720)
    return s

def init_puzzle()->tuple:
    board_size = int(validate_input("Please enter the board size (in 3,4,5)", range(3,100)))
    numbers = list(range(1, board_size**2 + 1))
    solved_puzzle = [[0 if i == board_size-1 and j == board_size-1 else numbers.pop(0) for i in range(board_size)] for j in range(board_size)]
    puzzle, current_0_pos = disrupt(board_size) #Disrupt puzzle
    last_puzzle = [[0 for _ in range(board_size)] for _ in range(board_size)]   #Create last puzzle memory to detect movement
    return board_size, numbers, solved_puzzle, puzzle, current_0_pos, last_puzzle

def create_puzzle_box(board_size)->list:
    def create_box_ref(board_size:int)->turtle.Turtle:
        box_ref = turtle.Turtle()
        box_ref.hideturtle()
        box_ref.shape("square")
        box_ref.color(149, 242, 149)
        box_ref.shapesize(30/board_size, 30/board_size, 10)
        box_ref.penup()
        box_ref.speed(0)
        return box_ref
    
    #Init a reference to block objects to enhance performance
    box_ref = create_box_ref(board_size)

    turtles = [[box_ref.clone() for i in range(board_size)] for j in range(board_size)]
    for j in range(board_size):
        for i in range(board_size):
            if i == current_0_pos[1] and j == current_0_pos[0]:
                turtles[i][j].color("white")
            turtles[i][j].goto(index_to_pos(i, j))
            turtles[i][j].onclick(onclick_hdlr)
            turtles[i][j].showturtle()
    return turtles

def create_puzzle_nums(board_size:int)->list:
    def create_num_ref()->turtle.Turtle:
        num_ref = turtle.Turtle()
        num_ref.hideturtle()
        num_ref.color("blue")
        num_ref.penup()
        num_ref.speed(0)
        return num_ref

    #Init a reference to number writing objects to enhance performance
    num_ref = create_num_ref()

    nums = [[num_ref.clone()for i in range(board_size)] for j in range(board_size)]
    return nums

if __name__ == "__main__":
    #Init counter
    counter = 0

    #Init turtle turtle.Screen
    s = init_screen()

    #Init puzzle
    board_size, numbers, solved_puzzle, puzzle, current_0_pos, last_puzzle = init_puzzle()

    #Animation Lock
    isAnimating = False

    #Init tracer off
    turtle.tracer(0)

    #Create block turtles
    turtles = create_puzzle_box(board_size)

    #Create number turtles
    font_size = int(120/board_size)
    nums = create_puzzle_nums(board_size)
    
    #Init numbers
    write_num(nums, first_write=True)

    s.mainloop()