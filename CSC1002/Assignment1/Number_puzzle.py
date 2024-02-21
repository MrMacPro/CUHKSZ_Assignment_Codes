'''
import os
#os.system("pip install streamlit")  #Check installation of streamlit lib
#os.system("cls")
import streamlit as st
'''
import random as rd
import re
import turtle

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
'''
#Environment operations
@st.cache_resource
def run_st():   #Run streamlit only once
    os.system("echo st_started > cmd.txt")
    os.system("streamlit run Number_puzzle.py")

def env_start():    #Run streamlit cmd if the program is invoked with "python assignment1.py"
    try:
        fhand = open("cmd.txt", "r")
        fhand.close()
        st.title("Number Puzzle")
    except FileNotFoundError:
        print("excepting")
        run_st()

def env_end():  #Remove the cmd file
    os.remove("cmd.txt")
'''

#Puzzle Class
class Puzzle():
    def __init__(self):
        self.current_0_pos = [BOARD_WIDTH-1,BOARD_HEIGHT-1]  #0 for x direction | 1 for y direction     #Memorize the location of 0 for convenience
        
        #Create a solved puzzle
        self.puzzle = self.create_referrence()

        self.shuffle(DISRUPTION_TIMES)
    
    def shuffle(self,times:int):
        #Shuffle the puzzle
        for _ in range(times):   #Disrupt from a solved puzzle to guarantee the solvability 
            try:
                self.move(rd.randint(0,3))
            except ValueError:
                pass

    def create_referrence(self)->list:
        solved_puzzle = []
        counter = 1
        for i in range(BOARD_HEIGHT):   #Remain the capability of creating puzzles other than 3*3
            this_row = []
            for j in range(BOARD_WIDTH):
                this_row.append(counter)
                counter += 1
            solved_puzzle.append(this_row)
        solved_puzzle[BOARD_HEIGHT-1][BOARD_WIDTH-1] = 0   #The last block should be left blank
        return solved_puzzle

    def move(self, direction:int):   #0:Left 1:Right 2:Up 3:Down
        #Check availablility: Raise value error if the 0 block is trying to move out of the frame
        self.try_move(direction)
        
        #Target next position
        next_0_pos = [self.current_0_pos[0] + PROMPT_TO_MOVEMENT[direction][0], self.current_0_pos[1] + PROMPT_TO_MOVEMENT[direction][1]]
        
        #Switch blocks
        self.puzzle[self.current_0_pos[0]][self.current_0_pos[1]], self.puzzle[next_0_pos[0]][next_0_pos[1]]\
        = self.puzzle[next_0_pos[0]][next_0_pos[1]], self.puzzle[self.current_0_pos[0]][self.current_0_pos[1]]

        #Refresh 0 position
        self.current_0_pos = next_0_pos

    def try_move(self, direction:int):  #Only check availability without moving anything
        #Check availablility: Raise value error if the 0 block is trying to move out of the frame
        if self.current_0_pos[0] + PROMPT_TO_MOVEMENT[direction][0] < 0 or self.current_0_pos[0] + PROMPT_TO_MOVEMENT[direction][0] > BOARD_HEIGHT-1 \
        or self.current_0_pos[1] + PROMPT_TO_MOVEMENT[direction][1] < 0 or self.current_0_pos[1] + PROMPT_TO_MOVEMENT[direction][1] > BOARD_WIDTH-1:
            raise ValueError("Invalid move")

    def solved(self)->bool: #Check if the puzzle is solved
        return self.puzzle == self.create_referrence()
    
    def print_board(self):
        global win
        
        # 创建一个窗口
        win = turtle.Screen()

        # 创建一个二维列表来存储所有的按钮
        buttons = [[None]*BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

        # 创建所有的按钮
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                # 创建一个新的turtle对象作为按钮
                button = turtle.Turtle()
                button.speed(0)  # 设置画笔移动的速度为最快
                button.shape('square')  # 设置形状为正方形
                button.shapesize(2)  # 设置大小
                button.penup()
                # 将按钮移动到窗口中间的指定位置
                button.goto(j*60 - BOARD_WIDTH*30, i*60 - BOARD_HEIGHT*30)
                buttons[i][j] = button

        # 绑定点击事件
        win.onclick(turtle_on_click)

    def __str__(self)->str:  #Display puzzle
        output = ""
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                output += str(self.puzzle[i][j]) if self.puzzle[i][j] != 0 else " "
                output += " "
            output += "\n"
        return output

#UI abstraction
def init_prompt()->list:    #0:Left 1:Right 2:Up 3:Down
    while True:
        cmd = input("Enter the four letters used for left, right, up and down move >")
        cmd = cmd.lower()
        if all(char.isalpha() or char.isspace() for char in cmd):   #Only works if the command has letters and spaces only
            letters = re.findall("[a-zA-Z]", cmd)
            if len(letters) == 4:   #Only works when there are exact 4 letters (case insensitive)
                if len(set(letters)) == 4:  #Only works if there is no repeating letters
                    return letters
                else:
                    print("Invalid input: Repeated letters")
            elif len(letters) < 4:
                print("Invalid length: Too short")
            elif len(letters) > 4:
                print("Invalid length: Too long")
        else:
            print("Invalid input: Exist characters other than letters and spaces")

def take_action(prompts:list)->int: #This is the function that takes and solves input into standard form
    hint = ""
    for i in range(4):  #Get the hint of operable moves
        try:
            puzzle.try_move(i)
            hint += (HINT[i]+prompts[i]+", ")
        except:
            pass

    while True: #Solve input
        action = input(f"Enter your move ({hint})>")
        action = action.lower()
        if action not in prompts:   #Only registered commands works
            print("Invalid action")
        else:
            try:    #Only operable moves works
                puzzle.try_move(prompts.index(action))
                break
            except:
                print("You can't go further on this direction")
    
    return prompts.index(action)    #The output is in standard form (0/1/2/3)

def turtle_on_click(x,y):
    global this_click
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            # 检查点击位置是否在按钮内
            if j*60-20 - BOARD_WIDTH*30 < x < j*60+20 - BOARD_WIDTH*30 and i*60-20 - BOARD_HEIGHT*30 < y < i*60+20 - BOARD_HEIGHT*30:
                this_click = [i,j]

def take_action_with_gui():
    global this_click
    while True:
        this_click = [None,None]
        while this_click == [None,None]:
            pass
        if abs(this_click[0] - puzzle.current_0_pos[0]) + abs(this_click[1] - puzzle.current_0_pos[1]) < 2:
            return PROMPT_TO_MOVEMENT.index((this_click[0] - puzzle.current_0_pos[0], this_click[1] - puzzle.current_0_pos[1]))
        else:
            print("You can't move this block")
                
if __name__ == "__main__":
    #Init
    #env_start()
    print(INTRO)
    #prompts = init_prompt()
    while True: #Infinite loop for everything
        #Init puzzle
        puzzle = Puzzle()
        puzzle.print_board()

        counter = 0
        while True: #Infinite loop for game play
            #Initial state of puzzle before this action
            print(puzzle)

            #Winning detection
            if puzzle.solved():
                print(f"Congratulations!  You solved the puzzle in {counter} moves!")
                break

            #Take action
            #action = take_action(prompts)
            action = take_action_with_gui()

            #Move
            puzzle.move(action)

            counter += 1
        
        #Check if continue
        while True:
            cmd = input("\nEnter “n” for another game, or “q” to end the game >")
            if cmd == "n":
                break
            elif cmd == "q":
                print("Goodbye!")
                #env_end()
                exit()
            else:
                print("Invalid command")