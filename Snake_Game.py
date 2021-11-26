# my screen resolution: 1920x1080

import os
import random
import time
from tkinter import *
import tkinter as tk


# create window
from tkinter.messagebox import showinfo

top = tk.Tk()
# title of window
top.title("Snake Game")


def placeFood():
    global food, foodX, foodY
    food = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="purple")
    foodX = random.randint(0, 1100 - snakeSize)
    foodY = random.randint(0, 800 - snakeSize)
    canvas.move(food, foodX, foodY)


def leftKey(event):
    global direction
    direction = "left"


def rightKey(event):
    global direction
    direction = "right"


def upKey(event):
    global direction
    direction = "up"


def downKey(event):
    global direction
    direction = "down"


def pauseKey(key):
    global speed
    direction = key
    if (direction == key):
        speed = 9999
        showinfo('You have paused', 'Press p ONCE to Continue(maybe wait for few seconds)')


def continueKey(key):
    direction = key
    if (direction == key):
        speed = 100
        top.after(speed, moveSnake)


def speedUpKey(event):
    moveSnake()


def bossKey():
    top.withdraw()
    timer.withdraw()
    txt = showinfo('Warm reminder', 'You are working now!')
    if txt == "ok":
        top.update()
        top.deiconify()
        respawn()


def growSnake():
    lastElement = len(snake) - 1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.append(canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="#009700"))
    if direction == "left":
        canvas.coords(snake[lastElement + 1], lastElementPos[0] + snakeSize, lastElementPos[1],
                      lastElementPos[2] + snakeSize, lastElementPos[3])
    elif direction == "right":
        canvas.coords(snake[lastElement + 1], lastElementPos[0] - snakeSize, lastElementPos[1],
                      lastElementPos[2] - snakeSize, lastElementPos[3])
    elif direction == "up":
        canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] + snakeSize, lastElementPos[2],
                      lastElementPos[3] + snakeSize)
    else:
        canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] - snakeSize, lastElementPos[2],
                      lastElementPos[3] - snakeSize)
    global score
    score += 10
    txt = "score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)



def moveFood():
    global food, foodX, foodY
    canvas.move(food, (foodX * (-1)), (foodY * (-1)))
    foodX = random.randint(0, 1100 - snakeSize)
    foodY = random.randint(0, 800 - snakeSize)
    canvas.move(food, foodX, foodY)


def overlapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False


def moveSnake():
    canvas.pack()
    positions = []
    positions.append(canvas.coords(snake[0]))
    if positions[0][0] < 0:
        canvas.coords(snake[0], 1100, positions[0][1], 1100 - snakeSize, positions[0][3])
    elif positions[0][2] > 1100:
        canvas.coords(snake[0], 0 - snakeSize, positions[0][1], 0, positions[0][3])
    elif positions[0][3] > 800:
        canvas.coords(snake[0], positions[0][0], 0 - snakeSize, positions[0][2], 0)
    elif positions[0][1] < 0:
        canvas.coords(snake[0], positions[0][0], 800, positions[0][2], 800 - snakeSize)
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
    sHeadPos = canvas.coords(snake[0])
    foodPos = canvas.coords(food)
    if overlapping(sHeadPos, foodPos):
        moveFood()
        growSnake()
    for i in range(1, len(snake)):
        if overlapping(sHeadPos, canvas.coords(snake[i])):
            gameOver = True
            canvas.create_text(550, height / 2, fill="dark blue", font=("Times 20 italic bold", 35), text="Game Over!")
            timer.destroy()
            if score >= 390:
                showinfo('Warm reminder', 'Good job! Your score is higher enough, please contact the administrator to update leader board!')
    for i in range(1, len(snake)):
        positions.append(canvas.coords(snake[i]))
    for i in range(len(snake) - 1):
        canvas.coords(snake[i + 1], positions[i][0], positions[i][1], positions[i][2], positions[i][3])
    if 'gameOver' not in locals():
        top.after(speed, moveSnake)
    if speed == 999999:
        canvas.create_text(550, height / 2, fill="dark blue", font=("Times 20 italic bold", 35), text="Time out!")


def respawn():
    top.destroy()
    os.system("python3 Snake_Game.py")


def timeConsumer():
    global seconds
    consumed = time.time() - start
    minutes = int(consumed / 60)
    seconds = int(consumed - minutes * 60.0)
    variable.set('%02d:%02d' % (minutes, seconds))
    timer.after(1, timeConsumer)
    if seconds == 10:
        global speed
        speed = 130
    elif seconds == 30:
        speed = 150
    elif seconds == 45:
        speed = 200
    if minutes == 1:
        speed = 999999
        timer.destroy()


def save():
    global speed
    global score
    global seconds
    saver = open("saver.txt", "w")
    saver.write(str(speed)+"\n")
    saver.write(str(seconds)+"\n")
    saver.write(str(score)+"\n")
    top.destroy()



# width of snake’s world
width = 1500
# height of snake’s world
height = 800

# computers screen size
ws = top.winfo_screenwidth()
hs = top.winfo_screenheight()
# calculate center
x = (ws / 2) - (width / 2)
y = (hs / 2) - (height / 2)
# window size
top.geometry('%dx%d+%d+%d' % (width, height, x, y))
respawnBtn = tk.Button(top, text="Restart", bg="red", fg="white", font=50, command=respawn)
respawnBtn.pack(side=RIGHT, fill="y")
bossBtn = tk.Button(top, text="Boss is coming!", bg="black", fg="red", font=50, command=bossKey)
bossBtn.pack(side=LEFT, fill="y")
saveBtn = tk.Button(top, text="Save and Quit", bg="light blue", fg="white", font=50, command=save)
saveBtn.pack(side=RIGHT, fill="y")

canvas = Canvas(top, bg="teal", width=1100, height=800)

# snack objects
snake = []
snakeSize = 25
snake.append(canvas.create_rectangle(snakeSize, snakeSize, snakeSize * 2, snakeSize * 2, fill="red"))

# score
score = 0
txt = "Score:" + str(score)
scoreText = canvas.create_text(550, 23, fill="black", font=("Times", 30, "italic bold"), text=txt)


# set directions
canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.bind("<s>", speedUpKey)
canvas.bind("<space>", pauseKey)
canvas.bind("<p>", continueKey)
canvas.focus_set()
direction = "right"

#timer
start = time.time()
timer = tk.Toplevel()
timer.title("TIME CONSUME")
timer.geometry("300x100")
variable = tk.StringVar()
Label = tk.Label(timer, textvariable=variable, fg='blue', font=("Arial", 50))
Label.pack()
timeConsumer()

seconds = 0

speed = 90

placeFood()

moveSnake()

top.mainloop()
