from tkinter import *
from functools import partial
win = Tk()
win.title("Calc is short for Calculator btw")
screen = Label(win, text="", bg="gray", height=2, width=16, font=("Century Gothic", 18), relief = "sunken")
screen.grid(row=0, column=0, columnspan=4, sticky="nsew") # it's getting stickkyy, so the button expands to the extra space 
def ketamene(btn, screen):
    dawg = screen.cget("text")
    if btn == "=":
        try: screen.config(text=str(eval(dawg)))
        except: screen.config(text="U stupid 😭🙏💯")
    elif btn == "C": screen.config(text="")
    else: screen.config(text=dawg + btn)
# app.winfo_screenwidth and app.winfo_screenheight takes the pixels of the screen
win.geometry("400x400+{}+{}".format(win.winfo_screenwidth() // 2 - 200, win.winfo_screenheight() // 2 - 200))
buttons = [
    ("**", 1, 0), ("//", 1, 1), ("%", 1, 2), ("C", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("*", 4, 3),
    (".", 5, 0), ("0", 5, 1), ("=", 5, 2), ("/", 5, 3) ]
for (text, rw, clmn) in buttons:
    Button(win, text=text, width=5, height=2,
           bg="orange" if text == "C" else "gray", # for coloring of the calculator 
           command=partial(ketamene, text, screen)).grid(row=rw, column=clmn, sticky="nsew") # sticky is used to make the buttons expand as the window expands
for i in range(1, 6): 
    win.grid_rowconfigure(i, weight=1) # weight is the prioritization of the buttons growing if there's extra space 
    win.grid_columnconfigure(i % 4, weight=1)
win.mainloop()