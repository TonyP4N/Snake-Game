# my screen resolution: 1920x1080

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
# title of window
root.title("Menu")
root.geometry("500x630")


def methodOfGame():
    top1 = tk.Toplevel()
    top1.title("HELP")
    top1.geometry("600x300")
    bg1 = tk.PhotoImage(file="helpBg.png")
    # canvas = tk.Canvas(top1, width=600, height=300)
    # canvas.create_image(600, 300, image=bg1)
    # canvas.pack()
    guide1 = Label(top1, text="Use ↑ to change the direction of the snake's movement to up" + "\n"
                              + "Use ↓ to change the direction of the snake's movement to down" + "\n"
                              + "Use ← to change the direction of the snake's movement to left" + "\n"
                              + "Use → to change the direction of the snake's movement to right" + "\n"
                              + "When the snake eat a food, it will grow up once!" + "\n"
                              + "You have 1 minute to eat food, each food worth 10 points!" + "\n"
                              + "You can pause the game use 'SPACE'(and have a cup of tea?)", fg="white",
                   font=('Times', 14, 'bold italic'), image=bg1, compound=CENTER)
    guide1.pack()
    guide5 = Label(top1, text="However, if the head collide with the body, GAMEOVER!!", fg="red",
                   font=('Times', 14, 'bold italic'))
    guide5.pack()
    top1.mainloop()


def leaderBoard():
    leaderboard = tk.Toplevel()
    leaderboard.title("Leader Board")
    leaderboard.geometry("500x800")
    global leaderboardbg
    leaderboardbg = tk.PhotoImage(file="leaderboard1.png")
    leaderboard1 = Canvas(leaderboard, width=500, height=800)
    leaderboard1.create_image(250, 400, image=leaderboardbg)
    leaderboard1.create_text(70, 20, text="Rank", fill="#483d8b", font=('Times', 25, 'bold'))
    leaderboard1.create_text(230, 20, text="Player", fill="#483d8b", font=('Times', 25, 'bold'))
    leaderboard1.create_text(400, 20, text="Score", fill="#483d8b", font=('Times', 25, 'bold'))
    leaderboard1.create_text(70, 100, text="1", fill="#ff8c00", font=('Arial', 20))
    leaderboard1.create_text(230, 100, text="Yan Fei", fill="#ff8c00", font=('Arial', 20))
    leaderboard1.create_text(400, 100, text="720", fill="#ff8c00", font=('Arial', 20))
    leaderboard1.create_text(70, 160, text="2", fill="silver", font=('Arial', 20))
    leaderboard1.create_text(230, 160, text="Amy Wang", fill="silver", font=('Arial', 20))
    leaderboard1.create_text(400, 160, text="680", fill="silver", font=('Arial', 20))
    leaderboard1.create_text(70, 220, text="3", fill="#b8860b", font=('Arial', 20))
    leaderboard1.create_text(230, 220, text="Jeremy Lin", fill="#b8860b", font=('Arial', 20))
    leaderboard1.create_text(400, 220, text="600", fill="#b8860b", font=('Arial', 20))

    leaderboard1.create_text(70, 280, text="4", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(230, 280, text="Kenny Stark", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(400, 280, text="590", fill="#6495ed", font=('Arial', 20))

    leaderboard1.create_text(70, 340, text="5", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(230, 340, text="Mike", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(400, 340, text="550", fill="#6495ed", font=('Arial', 20))

    leaderboard1.create_text(70, 400, text="6", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(230, 400, text="Tony Pan", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(400, 400, text="520", fill="#6495ed", font=('Arial', 20))

    leaderboard1.create_text(70, 460, text="7", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(230, 460, text="Pam", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(400, 460, text="500", fill="#6495ed", font=('Arial', 20))

    leaderboard1.create_text(70, 520, text="8", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(230, 520, text="Leo", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(400, 520, text="480", fill="#6495ed", font=('Arial', 20))

    leaderboard1.create_text(70, 580, text="9", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(230, 580, text="LeBron", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(400, 580, text="430", fill="#6495ed", font=('Arial', 20))

    leaderboard1.create_text(70, 640, text="10", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(230, 640, text="Christopher James", fill="#6495ed", font=('Arial', 20))
    leaderboard1.create_text(400, 640, text="390", fill="#6495ed", font=('Arial', 20))

    leaderboard1.create_text(240, 690, text="The leader board shows the Greatest 10 Players!",
                             fill="#a52a2a", font=('Times', 15, 'underline'))

    backBtn = Button(leaderboard, text="Back", font=('Times', 17, 'italic'), command=leaderboard.destroy)
    backBtn.configure(width=10, height=1, bg="#008b8b")
    leaderboard1.create_window(420, 750, window=backBtn)

    leaderboard1.pack()


def tricks():
    tricks = tk.Toplevel()
    tricks.title("Some tricks")
    tricks.geometry("400x400")
    global tricksbg
    tricksbg = PhotoImage(file="tricksbg.png")
    trick1 = Canvas(tricks, width=400, height=400)
    trick1.create_image(200, 200, image=tricksbg)
    trick1.create_text(200, 40, text="Wow, you find me!\n Here are some tips and tricks for you!", fill="white",
                       font=('Arial', 15, 'italic'))
    trick1.create_text(200, 115, text="Actually, the speed of snake\nwill be slower\nwith the time pass by.",
                       fill="green", font=('Arial', 15, 'italic', 'bold'))
    trick1.create_text(200, 195, text="However, you can use 's' to\nspeed up! It's a kind of cheat,\nso use LESS.",
                       fill="orange", font=('Arial', 15, 'italic', 'bold'))
    trick1.create_text(200, 300, text="If you're secretly playing at work,\nremember to use the boss button\non the "
                                      "left side of the game and\ndon't thank me for protecting your salary.\n:D",
                       fill="#dc143c", font=('Arial', 13, 'italic', 'bold'))
    trick1.pack()


def quitGame():
    if messagebox.askokcancel("Quit", "Do you want to stop gaming?"):
        root.destroy()


def start():
    root.withdraw()
    leaderBoard()
    os.system("python3 Snake_Game.py")
    root.update()
    root.deiconify()


def continueL():
    root.withdraw()
    leaderBoard()
    os.system("python3 snakeGameContinue.py")
    root.update()
    root.deiconify()


leaderboardbg = None
tricksbg = None

btn1 = Button(root, text="Start New Game", width=15, height=2, bg="black", fg="red", font=("Arial", 25),
              command=start).pack(pady=10)
btn2 = Button(root, text="Continue Last Game", width=15, height=2, bg="black", fg="red", font=("Arial", 25),
              command=continueL).pack(pady=10)
btn3 = Button(root, text="Help", width=12, height=2, bg="black", fg="yellow", font=("Arial", 25),
              command=methodOfGame).pack(pady=10)
btn4 = Button(root, text="Leader Board", width=12, height=2, bg="black", fg="green", font=("Arial", 25),
              command=leaderBoard).pack(pady=10)
btn5 = Button(root, text="Quit", width=10, height=1, bg="black", fg="white", font=("Arial", 25),
              command=quitGame).pack(pady=10)
btn6 = Button(root, text="Some....tricks!", width=30, height=1, bg="white", fg="white",
              font=("Arial", 15), command=tricks).pack(side=BOTTOM, fill="x")


root.protocol('WM_DELETE_WINDOW', quitGame)

root.mainloop()
