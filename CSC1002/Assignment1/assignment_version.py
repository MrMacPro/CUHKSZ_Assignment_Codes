'''
This is Hanson's sliding puzzle game.
Only python basic random and re library imported.
'''

import random as rd
import re

#Constants
BOARD_WIDTH = 3
BOARD_HEIGHT = 3

DISRUPTION_TIMES = 1000
PROMPT_TO_MOVEMENT = ((0,1),(0,-1),(1,0),(-1,0))
HINT = ("left-","right-","up-","down-")
INTRO = "\nWelcome to Sliding Puzzle - 2024, a classic and fun game that challenges your logic and problem-solving skills.\n\n\
\
In this game, you will face a square-framed board with 8 numbered tiles and an empty space.\n\
The tiles are placed in random order, and your goal is to slide them around until they are arranged in sequential order from left to right, top to bottom.\n\
You can only move one tile at a time into the adjacent empty space.\n\n\
\
Can you solve the puzzle in the fewest moves possible? Try it out and see how fast you can complete it!\n"

def shuffle(times:int):
    #Shuffle the puzzle
    for _ in range(times):   #Disrupt from a solved puzzle to guarantee the solvability 
        try:
            move(rd.randint(0,3))
        except ValueError:
            pass

def create_referrence()->list:
    solved_puzzle = [[i * BOARD_WIDTH + j + 1 for j in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]
    solved_puzzle[BOARD_HEIGHT-1][BOARD_WIDTH-1] = 0   #The last block should be left blank
    return solved_puzzle

def move(direction:int):   #0:Left 1:Right 2:Up 3:Down
    global puzzle
    global current_0_pos

    #Check availablility: Raise value error if the 0 block is trying to move out of the frame
    try_move(direction)
    
    #Target next position
    next_0_pos = [current_0_pos[0] + PROMPT_TO_MOVEMENT[direction][0], current_0_pos[1] + PROMPT_TO_MOVEMENT[direction][1]]
    
    #Switch blocks
    puzzle[current_0_pos[0]][current_0_pos[1]], puzzle[next_0_pos[0]][next_0_pos[1]]\
    = puzzle[next_0_pos[0]][next_0_pos[1]], puzzle[current_0_pos[0]][current_0_pos[1]]

    #Refresh 0 position
    current_0_pos = next_0_pos

def try_move(direction:int):  #Only check availability without moving anything
    global current_0_pos

    #Check availablility: Raise value error if the 0 block is trying to move out of the frame
    if current_0_pos[0] + PROMPT_TO_MOVEMENT[direction][0] < 0 or current_0_pos[0] + PROMPT_TO_MOVEMENT[direction][0] > BOARD_HEIGHT-1 \
    or current_0_pos[1] + PROMPT_TO_MOVEMENT[direction][1] < 0 or current_0_pos[1] + PROMPT_TO_MOVEMENT[direction][1] > BOARD_WIDTH-1:
        raise ValueError("Invalid move")

def solved(puzzle:list)->bool: #Check if the puzzle is solved
    return puzzle == create_referrence()

def display_puzzle(puzzle:list)->str:  #Display puzzle
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            print(str(puzzle[i][j]) if puzzle[i][j] != 0 else " ", end = " ")
        print()

def init_prompt()->list:    #0:Left 1:Right 2:Up 3:Down
    while True:
        cmd = input("Enter the four letters used for left, right, up and down move >").lower()
        if all(char.isalpha() or char.isspace() for char in cmd):   #Only works if the command has letters and spaces only
            letters = re.findall("[a-zA-Z]", cmd)
            if len(letters) == 4:   #Only works when there are exact 4 letters (case insensitive)
                if len(set(letters)) == 4:  #Only works if there is no repeating letters
                    return letters
                else:
                    print("Invalid input: Repeated letters.")
            elif len(letters) < 4:
                print("Invalid length: Too short, 4 letters expected.")
            elif len(letters) > 4:
                print("Invalid length: Too long, 4 letters expected.")
        else:
            print("Invalid input: Exist characters other than letters and spaces")

def take_action(prompts:list)->int: #This is the function that takes and solves input into standard form
    hint = ""
    for i in range(4):  #Get the hint of operable moves
        try:
            try_move(i)
            hint += (HINT[i]+prompts[i]+", ")
        except:
            pass
    hint = hint[:-2]

    while True: #Solve input
        action = input(f"Enter your move ({hint})>").lower().replace(" ","")    #Take letters only
        if action not in prompts:   #Only registered commands works
            print(f"Invalid action, there is no prompt named {action}")
        else:
            try:    #Only operable moves works
                try_move(prompts.index(action))
                break
            except:
                print("You can't go further on this direction.")
    
    return prompts.index(action)    #The output is in standard form (0/1/2/3)

if __name__ == "__main__":
    #Init
    print(INTRO)
    prompts = init_prompt()
    while True: #Infinite loop for everything
        #Init puzzle
        current_0_pos = [BOARD_WIDTH-1, BOARD_HEIGHT-1]  #0(first element) for x direction | 1(second element) for y direction     #Memorize the location of 0 for convenience
        puzzle = create_referrence()
        shuffle(DISRUPTION_TIMES)

        counter = 0
        while True: #Infinite loop for game play
            #Initial state of puzzle before this action
            display_puzzle(puzzle)

            #Winning detection
            if solved(puzzle):
                print(f"Congratulations!  You solved the puzzle in {counter} moves!")
                break

            #Take action
            action = take_action(prompts)

            #Move
            move(action)

            counter += 1
        
        #Check if continue
        while True:
            cmd = input("\nEnter “n” for another game, or “q” to end the game >")
            if cmd == "n":
                break
            elif cmd == "q":
                print("Goodbye!")
                exit()
            else:
                print("Invalid command, 'n' or 'q' expected.")