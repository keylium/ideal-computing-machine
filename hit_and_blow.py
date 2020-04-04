import tkinter as tk
from tkinter import messagebox
from random import sample

alps = "QWERTYUIOP"
quest = sample(alps,4)
cnt = 0

def compare():
    global cnt
    cnt += 1
    hit, blow = 0, 0
    ans = textans.get().upper()
    for i in range(4):
        if ans[i] == quest[i]: hit+=1
        elif ans[i] in quest: blow+=1
    
    s = "{0} | {1}  Hit:{2}, Blow:{3}".format(cnt, ans, hit, blow)
    labelResult[cnt-1]["text"] = s
    
    if hit == 4:
        tk.messagebox.showinfo("Congratulations!", "You win!")
    elif cnt == 8:
        tk.messagebox.showinfo("Game over!", "You lose!")

def init_game():
    global cnt
    cnt = 0
    for i in range(8):
        labelResult[i]["text"] = "---"


win = tk.Tk()
win.title("hit&blow")
win.geometry("360x320")

labelans = tk.Label(win, text='Answer:', font="SimSun")
labelans.grid(column=1, row=0)

restartButton = tk.Button(win, text="リスタート", command=init_game)
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