'''
    This is Shuhan's Snake game. For players, you may alter the difficulty by changing the DIFFICULTY variable.
'''

#Import modules
import turtle
import random
from functools import partial

#Game Config
DIFFICULTY = "Normal"    # "Easy", "Normal", "Hard", "Nightmare", "Asian"

#Difficulty details
TIMER_SNAKE = 300
if DIFFICULTY == "Easy":
    MONSTER_COUNT, FOOD_COUNT, TIMER_MONSTER, TIMER_FOOD = 1, 3, (TIMER_SNAKE+50, TIMER_SNAKE+300), (100000, 100000)
elif DIFFICULTY == "Normal":
    MONSTER_COUNT, FOOD_COUNT, TIMER_MONSTER, TIMER_FOOD = 4, 5, (TIMER_SNAKE-50, TIMER_SNAKE+200), (5000, 10000)
elif DIFFICULTY == "Hard":
    MONSTER_COUNT, FOOD_COUNT, TIMER_MONSTER, TIMER_FOOD = 5, 6, (TIMER_SNAKE-50, TIMER_SNAKE+200), (5000, 10000)
elif DIFFICULTY == "Nightmare":
    MONSTER_COUNT, FOOD_COUNT, TIMER_MONSTER, TIMER_FOOD = 6, 7, (TIMER_SNAKE-50, TIMER_SNAKE+200), (2000, 5000)
elif DIFFICULTY == "Asian":
    MONSTER_COUNT, FOOD_COUNT, TIMER_MONSTER, TIMER_FOOD = 10, 15, (TIMER_SNAKE-50, TIMER_SNAKE+100), (1000, 2000)

g_screen = None
g_snake = None     # snake's head
g_snake_sz = 1     # size of the snake's tail
g_intro = None
g_key_pressed = None
g_status = None
g_in_progress = True
g_paused = False

COLOR_BODY = ("blue", "black")
COLOR_HEAD = "red"
COLOR_MONSTER = "purple"
FONT_FOOD = ("Arial",12,"normal")
FONT_DONE = ("Arial",24,"normal")
FONT_INTRO = ("Arial",16,"normal")
FONT_STATUS = ("Arial",20,"normal")
SZ_SQUARE = 20      # square size in pixels

DIM_PLAY_AREA = 500
DIM_STAT_AREA = 40 # !!! multiple of 40
DIM_MARGIN = 30
DIM_CLOSEST_MONSTER = 100

PEN_OFFSET = 10

KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_SPACE = "Up", "Down", "Left", "Right", "space"

HEADING_BY_KEY = {KEY_UP:90, KEY_DOWN:270, KEY_LEFT:180, KEY_RIGHT:0}

def in_boarder(pos):    #Capsuled boarder checker
    return -(DIM_PLAY_AREA)//2 < pos[0] < (DIM_PLAY_AREA)//2 and \
           -(DIM_PLAY_AREA+2*SZ_SQUARE)//2 < pos[1] < (DIM_PLAY_AREA-2*SZ_SQUARE)//2

def create_turtle(x, y, color="red", border="black"):   #Capsuled turtle creation
    t = turtle.Turtle("square")
    t.color(border, color)
    t.up()
    t.goto(x,y)
    return t

def configure_play_area():  #Play area init
    # motion border
    m = create_turtle(0,0,"","black")
    sz = DIM_PLAY_AREA//SZ_SQUARE
    m.shapesize(sz, sz, 3)
    m.goto(0,-DIM_STAT_AREA//2)  # shift down half the status

    # status border
    s = create_turtle(0,0,"","black")
    sz_w, sz_h = DIM_STAT_AREA//SZ_SQUARE, DIM_PLAY_AREA//SZ_SQUARE
    s.shapesize(sz_w, sz_h, 3)
    s.goto(0,DIM_PLAY_AREA//2)  # shift up half the motion

    # turtle to write introduction
    intro = create_turtle(-200,50)
    intro.hideturtle()
    intro.write("Snake by Shuhan\n\nClick anywhere to start, have fun!!!!", font=FONT_INTRO)

    # turtle to write status
    status = create_turtle(0,0,"","black")
    status.hideturtle()
    status.goto(-240,s.ycor()-15)

    return intro, status

def configure_screen(): #UI init
    s = turtle.Screen()
    s.tracer(0)    # disable auto screen refresh, 0=disable, 1=enable
    s.title("Snake by Shuhan")
    w = DIM_PLAY_AREA + DIM_MARGIN*2
    h = DIM_PLAY_AREA + DIM_MARGIN*2 + DIM_STAT_AREA
    s.setup(w, h)
    s.mode("standard")
    return s

def update_status():    #Status update handler
    global g_in_progress
    if g_in_progress:
        g_status.clear()
        status = f'Key-{g_key_pressed}  Tail length-{g_snake_sz}  Mode {DIFFICULTY}'
        g_status.write(status, font=FONT_STATUS)
        g_screen.update()

def on_arrow_key_pressed(key):  #Arrow key stroke detector
    global g_key_pressed
    global g_paused
    g_key_pressed = key
    g_paused = False
    update_status()

def on_space_key_pressed():  #Space key stroke detector
    global g_paused
    g_paused = not g_paused

def on_timer_snake():   #Snake event callback
    global g_in_progress
    if g_in_progress:
        #Check new position in boarder.
        if g_key_pressed is None:
            g_screen.ontimer(on_timer_snake, TIMER_SNAKE)
            return

        # Clone the head as body
        g_snake.color(*COLOR_BODY)
        g_snake.stamp()
        g_snake.color(COLOR_HEAD)

        # Advance snake
        g_snake.setheading(HEADING_BY_KEY[g_key_pressed])
        g_snake.forward(SZ_SQUARE)
        if not in_boarder(g_snake.pos()) or g_paused:   #Boarder limitation and pausing
            g_snake.backward(SZ_SQUARE)

        # Consume food
        for g_food in g_foods:
            if g_snake.distance(g_food) <= SZ_SQUARE/2:
                consume_food(g_foods.index(g_food)+1)
                g_food.clear()
                g_food.goto(DIM_PLAY_AREA + SZ_SQUARE,0)
                break
        
        # Win or Lose
        if g_snake_sz >= ((1+FOOD_COUNT)*FOOD_COUNT)//2+1:
            done(True)
        for g_monster in g_monsters:
            if g_snake.distance(g_monster) <= SZ_SQUARE:
                done()

        # Shifting or extending the tail.
        # Remove the last square on Shifting.
        if len(g_snake.stampItems) > g_snake_sz:
            g_snake.clearstamps(1)

    g_screen.update()

    g_screen.ontimer(on_timer_snake, TIMER_SNAKE)


def on_timer_monster(g_monster):    #Monster move callback
    global g_in_progress
    if g_in_progress:
        angle = g_monster.towards(g_snake)
        qtr = angle//45 # (0,1,2,3,4,5,6,7)
        heading = qtr * 45 if qtr % 2 == 0 else (qtr+1) * 45

        g_monster.setheading(heading)
        g_monster.forward(SZ_SQUARE)
        if not in_boarder(g_monster.pos()):
            g_monster.backward(SZ_SQUARE)

    g_screen.update()
    delay = random.randint(TIMER_MONSTER[0], TIMER_MONSTER[1])
    g_screen.ontimer(partial(on_timer_monster, g_monster), delay)

def consume_food(num):  #Food consume handler
    global g_snake_sz
    if g_snake_sz < 100:
        g_snake_sz += num
        update_status()

def on_timer_food(g_food):  #Food shuffle callback
    global g_in_progress
    if g_in_progress:
        if g_food.pos() != (DIM_PLAY_AREA + SZ_SQUARE,0):
            g_food.clear()
            while True:
                new_pos = (g_food.xcor() + random.randint(-5,5)*SZ_SQUARE,\
                            g_food.ycor() + random.randint(-5,5)*SZ_SQUARE)
                if in_boarder(new_pos):
                    break
            g_food.goto(new_pos)
            g_food.goto(g_food.xcor(), g_food.ycor()-PEN_OFFSET)
            g_food.write(str(g_foods.index(g_food)+1), align="center", font=FONT_FOOD)
            g_food.goto(g_food.xcor(), g_food.ycor()+PEN_OFFSET)

    g_screen.update()
    delay = random.randint(TIMER_FOOD[0], TIMER_FOOD[1])
    g_screen.ontimer(partial(on_timer_food, g_food), delay)

def cb_start_game(x, y):    #Game main program
    g_screen.onscreenclick(None)
    g_intro.clear()

    for key in (KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT):
        g_screen.onkey(partial(on_arrow_key_pressed,key), key)
    g_screen.onkey(on_space_key_pressed, KEY_SPACE)

    on_timer_snake()
    for i in g_monsters:
        on_timer_monster(i)
    for i in g_foods:
        on_timer_food(i)


def done(win=False):    #Game over handler
    global g_in_progress
    g_in_progress = False
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    t.color("red")
    t.write("Winner!!" if win else "Game over!!", align="center", font=FONT_DONE)
    

if __name__ == "__main__":
    g_screen = configure_screen()
    g_intro, g_status = configure_play_area()

    update_status()

    g_monsters = []
    pos_range = list(range((-DIM_PLAY_AREA+SZ_SQUARE)//SZ_SQUARE, -DIM_CLOSEST_MONSTER//SZ_SQUARE))\
                      + list(range(DIM_CLOSEST_MONSTER//SZ_SQUARE, (DIM_PLAY_AREA-SZ_SQUARE)//SZ_SQUARE))
    random.shuffle(pos_range)
    for i in range(MONSTER_COUNT):
        g_monsters.append(create_turtle(pos_range[i] * SZ_SQUARE/2, pos_range[len(pos_range)-i-1] * SZ_SQUARE/2, COLOR_MONSTER, "black"))

    g_foods = []
    pos_range = list(range(-DIM_PLAY_AREA//2//SZ_SQUARE, DIM_PLAY_AREA//2//SZ_SQUARE))
    random.shuffle(pos_range)
    for i in range(FOOD_COUNT):
        food = create_turtle(pos_range[i] * SZ_SQUARE, pos_range[len(pos_range)-i-1] * SZ_SQUARE, COLOR_BODY[0], "black")
        food.hideturtle()
        g_foods.append(food)

    g_snake = create_turtle(0,0, COLOR_HEAD, "black")

    g_screen.onscreenclick(cb_start_game) # set up a mouse-click call back

    g_screen.update()
    g_screen.listen()
    g_screen.mainloop()