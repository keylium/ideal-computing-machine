import tkinter as tk
from tkinter import messagebox
from random import sample

class HitAndBlow:
    "Encapsulate the global variables into objects"
    def __init__(self):
        self.cnt = 0
        self.quest = sample("QWERTYUIOP",4)

game = HitAndBlow()

def compare():
    game.cnt += 1
    hit, blow = 0, 0
    ans = textans.get()
    for i in range(4):
        if ans[i] == game.quest[i]:
            hit+=1
        elif ans[i] in game.quest:
            blow+=1

    labelResult[game.cnt - 1]["text"] = f"{game.cnt} | {ans}  Hit:{hit}, Blow:{blow}"

    if hit == 4:
        tk.messagebox.showinfo("Congratulations!", "You win!")
    elif game.cnt == 8:
        tk.messagebox.showinfo("Game over!", "You lose!")

def restart():
    game.cnt = 0
    game.quest = sample("QWERTYUIOP",4)

    for i in range(8):
        labelResult[i]["text"] = "---"


win = tk.Tk()
win.title("hit&blow")
win.geometry("360x320")

labelans = tk.Label(win, text='Answer:', font="SimSun")
labelans.grid(column=1, row=0)

restartButton = tk.Button(win, text="リスタート", command=restart)
restartButton.grid(column=0, row=1)

textans = tk.Entry(font="SimSun", width=23, justify="center")
textans.insert(tk.END, "QWER")
textans.grid(column=1, row=1)

compareButton = tk.Button(win, text="チェック", command=compare)
compareButton.grid(column=2, row=1)

labelexplain = tk.Label(win,text='Q,W,E,R,T,Y,U,I,O,Pの\n中から4つ選んで下さい。')
labelexplain.grid(column=1, row=2)

labelResult = [tk.Label(win,text='---', font="SimSun") for _ in range(8)]
for i, result in enumerate(labelResult):
    result.grid(column=1, row=i+3)

win.mainloop()
