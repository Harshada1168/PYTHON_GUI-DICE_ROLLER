from tkinter import *
from random import*
#making dictionary to store the dice values
#unicode characters of dice
dice={
0 : '🎲',
1 : '⚀',#1 on dice
2 : '⚁',#2 on dice
3 : '⚂',#3 on dice
4 : '⚃',#4 on dice
5 : '⚄',#5 on dice
6 : '⚅'#6 on dice
}
App=Tk()
App.geometry("250x250")
App.title("Dice Roller")
msg1=Label(App, text="Click the roll button to roll the dice")
msg1.grid()
msg=Label(App, text=dice[0], font=('Times', 100), foreground='white', background='black')
msg.grid(row=1, column=0, padx=50, pady=20)

def roll():
    value=randint(1, 6)
    msg=Label(App, text=dice[value],font=('Times', 100), foreground='white', width=2 , background='black')
    msg.grid(row=1, column=0, padx=25, pady=5)
b=Button(App, text="roll", command=roll, background='pink', foreground='black')
b.grid()
App.mainloop()