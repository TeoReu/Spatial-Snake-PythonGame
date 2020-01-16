from tkinter import *
import random
import time


def story_screen():
    global x, skip
    x = x + 1
    canvas.delete("txt")
    txt4 = "We all have played in the past the  " \
           "Snake \nGame  on the old massive " \
           "Nokia phones.\n\n" \
           "Little lovely snake has been a " \
           "good \n friend to us, always " \
           "there \nin the hardest " \
           "times. \n\n" \
           "But now he decided to go in " \
           "his \nlifetime adventure, " \
           "right into space. \n" \
           "All these years spent on dark " \
           "screens\n" \
           "made him realise, he should " \
           "seek \n more for " \
           "purpose and answers. \n" \
           "What is the meaning of his life?\n\n" \
           "Come with him, be there for " \
           "him, \nthe way he  was there for you!\n" \
           "His adventure starts right in Manchester."
    canvas.create_text(290, 550 - x, fill="yellow",
                       font="Times 20 italic bold",
                       text=txt4, tag="txt")
    star_x = random.randint(0, width - snakeSize)
    star_y = random.randint(0, height - snakeSize)
    canvas.create_oval(star_x, star_y, star_x + 1,
                       star_y + 1, fill="white")
    buttons = Button(window, text="Skip", fg="black",
                     font="Times 14 italic bold",
                     command=skip_pressed, anchor=W)
    buttons.configure(width=20, background="yellow",
                      activebackground="#33B5E5", relief=FLAT)
    canvas.create_window(472, 500, anchor=CENTER, window=buttons)
    if skip == 1 or x > 470:
        skip_not_pressed = 0

    if "skip_not_pressed" not in locals():
        window.after(50, story_screen)
    else:
        loading()


def skip_pressed():
    global skip
    skip = 1


def loading():
    global skip_not_pressed
    skip_not_pressed = 0
    canvas.delete("txt")
    canvas.delete("all")
    canvas.create_image(275, 270, image=img)
    button3 = Button(window,
                     text="  Begin Spatial Adventure", fg="blue",
                     font="Times 14 italic bold",
                     command=menu, anchor=W)
    button3.configure(width=20, background="yellow",
                      activebackground="#33B5E5",
                      relief=FLAT)
    canvas.create_window(272, 270, anchor=CENTER,
                         window=button3)


def menu():
    global img
    canvas.delete("all")
    canvas.create_image(275, 270, image=img)
    canvas.create_text(270, 220, fill="yellow",
                       font="Times 20 italic bold",
                       text="Menu")

    button1 = Button(window, text="Start new game",
                     bg="yellow", fg="blue",
                     font="Times 12 italic bold",
                     command=start_game, anchor=W)
    button1.configure(width=15, activebackground="#33B5E5",
                      relief=FLAT)
    canvas.create_window(270, 270,
                         anchor=CENTER, window=button1)

    button2 = Button(window, text="High Scores",
                     command=high_score, fg="blue",
                     font="Times 12 italic bold",
                     anchor=W)
    button2.configure(width=15, activebackground="#33B5E5",
                      bg="yellow", relief=FLAT)
    canvas.create_window(270, 310, anchor=CENTER, window=button2)

    button4 = Button(window, text="Saved Games",
                     command=saved_games, fg="blue",
                     font="Times 12 italic bold", anchor=W)
    button4.configure(width=15, activebackground="#33B5E5",
                      bg="yellow", relief=FLAT)
    canvas.create_window(270, 350, anchor=CENTER, window=button4)

    button5 = Button(window, text="Quit", command=window.quit,
                     fg="blue", font="Times 12 italic bold", anchor=W)
    button5.configure(width=15, activebackground="#33B5E5",
                      bg="yellow", relief=FLAT)
    canvas.create_window(270, 390, anchor=CENTER, window=button5)


def high_score():
    global img, allPlayers
    canvas.delete("all")
    canvas.create_image(275, 270, image=img)
    canvas.create_text(270, 220, fill="yellow",
                       font="Times 20 italic bold",
                       text="High Scores")
    h = 270
    allPlayers = {k: v for k, v in sorted(allPlayers.items(),
                                          key=lambda x: x[1],
                                          reverse=True)}
    for keys in allPlayers.keys():
        line = keys + " " + str(allPlayers[keys])
        canvas.create_text(270, h, fill="yellow",
                           font="Times 15 italic bold",
                           text=line)
        h += 20
    button_back = Button(window, text="Go Back",
                         command=menu, fg="blue",
                         font="Times 12 italic bold",
                         anchor=W)
    button_back.configure(width=15,
                          activebackground="#33B5E5",
                          bg="yellow",
                          relief=FLAT)
    canvas.create_window(390, 350, anchor=SW, window=button_back)


def start_game():
    def add_player():
        global snake, snakeSize, direction, \
            pause, start, scoreText, color, \
            allPlayers, name, img2, img3, img4, img5
        name = e1.get()
        color = e2.get()
        background_string = e3.get()
        if background_string == "Manchester":
            background_image = img2
        elif background_string == "Lake District":
            background_image = img4
        elif background_string == "Moon":
            background_image = img3
        else:
            background_image = img5

        file = open("players.txt", "r")
        line = file.readline()
        player = line.split(" ")
        for i in range(len(player)):
            if i % 2:
                allPlayers[player[i - 1]] = int(player[i])
        if name not in allPlayers.keys():
            allPlayers[name] = 0
        print(allPlayers)

        canvas.delete("all")
        canvas.create_image(260, 280,
                            image=background_image)
        snake.append(canvas.create_rectangle(snakeSize,
                                             snakeSize,
                                             snakeSize * 2,
                                             snakeSize * 2,
                                             fill=color))
        scoreText = canvas.create_text(width / 2, 10,
                                       fill="yellow",
                                       font="Times 20 italic bold",
                                       text=txt)
        txt3 = "Special keys:\n <p> " \
               "for pause \n <b> for " \
               "bossKey \n <1> and  <2> " \
               "for score\n" \
               "<c> continue \nafter " \
               "GameOver,\n <s> to save "
        canvas.create_text(85, 75, fill="yellow",
                           font="Times 12 bold",
                           text=txt3)
        canvas.bind("<Left>", left_key)
        canvas.bind("<Right>", right_key)
        canvas.bind("<Up>", up_key)
        canvas.bind("<Down>", down_key)
        canvas.bind("<b>", boss_key)
        canvas.bind("<p>", pause_key)
        canvas.bind("<c>", cheat_key)
        canvas.bind("<s>", save_key)
        canvas.bind("1", cheat_score_key)
        canvas.bind("2", cheat_grow_snake)
        canvas.focus_set()

        start = time.time()
        time.perf_counter()
        place_food()
        place_obstacles()
        move_snake()
        window.mainloop()

    global img
    canvas.delete("all")
    canvas.create_image(275, 270, image=img)
    canvas.create_text(210, 200, fill="yellow",
                       font="Times 15 italic bold",
                       text="Customization:")
    canvas.create_text(210, 250, fill="yellow",
                       font="Times 15 italic bold",
                       text="Name:")
    e1 = Entry(canvas)
    canvas.create_window(280, 250, window=e1, height=20, width=70)
    canvas.create_text(185, 280, fill="yellow",
                       font="Times 15 italic bold",
                       text="Snake Color:")
    e2 = Entry(canvas)
    canvas.create_window(280, 280, window=e2,
                         height=20, width=70)
    canvas.create_text(165, 310, fill="yellow",
                       font="Times 15 italic bold",
                       text="Place to explore:")
    e3 = Entry(canvas)
    canvas.create_window(280, 310, window=e3, height=20, width=70)
    txt2 = "You can choose between: \n <Manchester>, " \
           "<Lake District>\n, <Moon>" \
           "and \n<On The Way To Moon>."

    canvas.create_text(430, 290, fill="yellow",
                       font="Times 9 italic bold",
                       text=txt2)
    button4 = Button(window, text="Begin", anchor=W)
    button4.configure(width=15, background="yellow",
                      activebackground="#33B5E5",
                      font="Times 12 italic bold",
                      fg="blue", relief=FLAT, command=add_player)
    canvas.create_window(250, 350, anchor=CENTER, window=button4)


def grow_snake():
    global score, snake, txt, scoreText, color
    last_element = len(snake) - 1
    last_element_pos = canvas.coords(snake[last_element])
    snake.append(canvas.create_rectangle(0, 0,
                                         snakeSize,
                                         snakeSize,
                                         fill=color))
    if direction == "left":
        canvas.coords(snake[last_element + 1],
                      last_element_pos[0] + snakeSize,
                      last_element_pos[1],
                      last_element_pos[2] + snakeSize,
                      last_element_pos[3])
    elif direction == "right":
        canvas.coords(snake[last_element + 1],
                      last_element_pos[0] - snakeSize,
                      last_element_pos[1],
                      last_element_pos[2] - snakeSize,
                      last_element_pos[3])
    elif direction == "up":
        canvas.coords(snake[last_element + 1], last_element_pos[0],
                      last_element_pos[1] + snakeSize,
                      last_element_pos[2], last_element_pos[3] + snakeSize)
    else:
        canvas.coords(snake[last_element + 1],
                      last_element_pos[0], last_element_pos[1] - snakeSize,
                      last_element_pos[2], last_element_pos[3] - snakeSize)
    global score
    score += 10
    txt = "Score: " + str(score)
    canvas.itemconfigure(scoreText, text=txt)


def move_food():
    global food, foodX, foodY
    canvas.move(food, (foodX * (-1)), (foodY * (-1)))
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)
    canvas.move(food, foodX, foodY)


def move_obstacle():
    global obstacle, obstacleX, obstacleY
    canvas.move(obstacle, (obstacleX * (-1)), (obstacleY * (-1)))
    obstacleX = random.randint(0, width - snakeSize)
    obstacleY = random.randint(0, height - snakeSize)
    canvas.move(obstacle, obstacleX, obstacleY)


def overlapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False


def move_snake():
    global ok, start, pause, snake, snakeSize, \
        direction, start, allPlayers, score, \
        start_pause, after_pause, portal
    canvas.pack()
    positions = [canvas.coords(snake[0])]
    if positions[0][0] < 0:
        canvas.coords(snake[0], width, positions[0][1],
                      width - snakeSize, positions[0][3])
    elif positions[0][2] > width:
        canvas.coords(snake[0], 0 - snakeSize,
                      positions[0][1], 0, positions[0][3])
    elif positions[0][3] > height:
        canvas.coords(snake[0], positions[0][0],
                      0 - snakeSize, positions[0][2], 0)
    elif positions[0][1] < 0:
        canvas.coords(snake[0], positions[0][0],
                      height, positions[0][2],
                      height - snakeSize)
    positions.clear()
    positions.append(canvas.coords(snake[0]))

    if direction == "left":
        canvas.move(snake[0], -snakeSize, 0)
    elif direction == "right":
        canvas.move(snake[0], snakeSize, 0)
    elif direction == "up":
        canvas.move(snake[0], 0, -snakeSize)
    elif direction == "down":
        canvas.move(snake[0], 0, snakeSize)

    s_head_pos = canvas.coords(snake[0])
    food_pos = canvas.coords(food)
    obstacle_pos = canvas.coords(obstacle)

    if pause is True and after_pause == 1:
        print(time.time() - start_pause)
        canvas.delete("pause_tag")
        canvas.create_text(270, 220,
                           fill="yellow",
                           font="Times 20 italic bold",
                           text="3...",
                           tag="pause3")
        window.after(750, pause3)

    if score % 20 and ok == 1:
        move_obstacle()
        ok = 0
    if score % 20 == 0 and ok == 0:
        ok = 1

    if time.time() - start > 10:
        move_food()
        start = time.time()

    if overlapping(s_head_pos, food_pos):
        move_food()
        grow_snake()

    if overlapping(s_head_pos, obstacle_pos):
        game_over = True
        canvas.create_text(width / 2, height / 2,
                           fill="white",
                           font="Times 20 italic bold",
                           text="Game Over!")

    for i in range(1, len(snake)):
        if overlapping(s_head_pos, canvas.coords(snake[i])):
            game_over = True
            canvas.create_text(width / 2, height / 2,
                               fill="white",
                               font="Times 20 italic bold",
                               text="Game Over!",
                               tag="txt_over")

    if "game_over" not in locals() and pause is False:
        window.after(90, move_snake)

    if "game_over" in locals():
        button_back = Button(window, text="Go  to Menu",
                             command=menu, fg="blue",
                             font="Times 12 italic bold", anchor=W)
        button_back.configure(width=15, activebackground="#33B5E5",
                              bg="yellow", relief=FLAT)
        canvas.create_window(390, 450, anchor=SW, window=button_back)
        if allPlayers[name] < score:
            allPlayers[name] = score
        update = open("players.txt", "w")
        for keys in allPlayers.keys():
            update.write(keys + " " + str(allPlayers[keys]) + " ")
        print(allPlayers)

    for i in range(1, len(snake)):
        positions.append(canvas.coords(snake[i]))

    for i in range(len(snake) - 1):
        canvas.coords(snake[i + 1], positions[i][0],
                      positions[i][1], positions[i][2], positions[i][3])


def saved_games():
    def start_saved_game():
        global name, score, img5, scoreText, start, color
        info_extract = open("savedinfo.txt", "r")
        line = info_extract.readline()
        line = line.split(" ")
        name = line[0]
        score = int(line[1])
        color = line[2]
        canvas.delete("all")
        canvas.create_image(260, 280, image=img5)
        snake.append(canvas.create_rectangle(snakeSize, snakeSize,
                                             snakeSize * 2,
                                             snakeSize * 2,
                                             fill=color))
        scoreText = canvas.create_text(width / 2, 10,
                                       fill="yellow",
                                       font="Times 20 italic bold",
                                       text=txt)
        txt3 = "Special keys:\n <p> for pause" \
               " \n <b> for bossKey \n <1> and " \
               " <2> for score\n" \
               "<c> continue \nafter GameOver," \
               "\n <s> to save "
        canvas.create_text(width - 80, 80,
                           fill="yellow", font="Times 12 bold",
                           text=txt3)
        canvas.bind("<Left>", left_key)
        canvas.bind("<Right>", right_key)
        canvas.bind("<Up>", up_key)
        canvas.bind("<Down>", down_key)
        canvas.bind("<b>", boss_key)
        canvas.bind("<p>", pause_key)
        canvas.bind("<c>", cheat_key)
        canvas.bind("<s>", save_key)
        canvas.bind("1", cheat_score_key)
        canvas.bind("2", cheat_grow_snake)
        canvas.focus_set()
        file = open("players.txt", "r")
        line = file.readline()
        player = line.split(" ")
        for i in range(len(player)):
            if i % 2:
                allPlayers[player[i - 1]] = int(player[i])
        if name not in allPlayers.keys():
            allPlayers[name] = 0
        print(allPlayers)
        start = time.time()
        time.perf_counter()
        place_food()
        place_obstacles()
        move_snake()
        window.mainloop()

    global name, score, start
    canvas.delete("all")
    canvas.create_image(275, 270, image=img)
    button_save = Button(window, text="Saved game1",
                         bg="yellow", fg="blue", font="Times 12 italic bold",
                         command=start_saved_game, anchor=W)
    button_save.configure(width=15, activebackground="#33B5E5", relief=FLAT)
    canvas.create_window(270, 270, anchor=CENTER, window=button_save)


def pause0():
    global pause, after_pause
    canvas.delete("pause0")
    pause = False
    after_pause == -1
    move_snake()


def pause1():
    canvas.delete("pause1")
    canvas.create_text(270, 220, fill="yellow",
                       font="Times 20 italic bold", text="Start", tag="pause0")
    window.after(500, pause0)


def pause2():
    canvas.delete("pause2")
    canvas.create_text(270, 220, fill="yellow",
                       font="Times 20 italic bold", text="1...", tag="pause1")
    window.after(750, pause1)


def pause3():
    canvas.delete("pause3")
    canvas.create_text(270, 220, fill="yellow",
                       font="Times 20 italic bold", text="2...", tag="pause2")
    window.after(750, pause2)


def place_food():
    global food, foodX, foodY
    food = canvas.create_rectangle(0, 0, snakeSize, snakeSize,
                                   fill="steel blue")
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)
    canvas.move(food, foodX, foodY)


def place_obstacles():
    global obstacleX, obstacleY, obstacle
    obstacle = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="red")
    obstacleX = random.randint(0, width - snakeSize)
    obstacleY = random.randint(0, height - snakeSize)
    canvas.move(obstacle, obstacleX, obstacleX)


def left_key(event):
    global direction
    direction = "left"


def right_key(event):
    global direction
    direction = "right"


def up_key(event):
    global direction
    direction = "up"


def down_key(event):
    global direction
    direction = "down"


def boss_key(event):
    global pause, boss
    boss = -boss
    if boss == -1:
        pause = True
        bk = Toplevel()
        bk.title("PyCharm")
        ws = bk.winfo_screenwidth()
        hs = bk.winfo_screenheight()
        bk.geometry('%dx%d+%d+%d' % (ws, hs, 0, 0))
        canvas2 = Canvas(bk, bg="black", width=ws, height=hs)
        img2 = PhotoImage(file="bossKey.GIF")
        canvas2.create_image(680, 370, image=img2)
        canvas2.pack()
        bk.mainloop()

        # close bossWindow() issue


def pause_key(event):
    global pause, start_pause, after_pause
    if pause is False:
        pause = True
        canvas.create_text(270, 220, fill="yellow",
                           font="Times 20 italic bold", text="Pause",
                           tag="pause_tag")
        after_pause = 0
    else:
        start_pause = time.time()
        after_pause = 1
        print(start_pause, pause, after_pause)
        move_snake()


# slowing or fastening the game
# bypass obstacle

def cheat_key(event):
    canvas.delete("txt_over")
    window.after(90, move_snake)


def cheat_grow_snake(event):
    grow_snake()


def cheat_score_key(event):
    global score
    score += 10
    grow_snake()


def save_key(event):
    global score, color, name, pause
    pause = True
    save_information = open("savedinfo.txt", "w+")
    save_information.write(name + " " + str(score) + " " + color)


def set_window_dimensions(w, h):
    window_gui = Tk()
    window_gui.title("Snake Game")
    ws = window_gui.winfo_screenwidth()
    hs = window_gui.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window_gui.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window_gui


skip = 0
x = 0
after_pause = -1
foodX = 0
foodY = 0
obstacleX = 0
obstacleY = 0
name = ""
allPlayers = {}
start = 0
start_pause = 0
ok = 0
pause = False
snake = []
snakeSize = 15
score = 0
txt = "Score: " + str(score)
direction = "right"
key = -1
boss = 1
width = 550
height = 550
color = "white"
players = {}
window = set_window_dimensions(width, height)
canvas = Canvas(window, bg="#000918", width=width, height=height)
img = PhotoImage(file="spatial3.GIF")
food = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="steel blue")
portal = canvas.create_rectangle(0, 0, snakeSize, snakeSize)
obstacle = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="red")
scoreText = canvas.create_text(200, 200, text="")
img2 = PhotoImage(file="manchester.gif")
img3 = PhotoImage(file="bg2.gif")
img4 = PhotoImage(file="bg.gif")
img5 = PhotoImage(file="bg3.gif")
canvas.pack()
story_screen()
window.mainloop()
