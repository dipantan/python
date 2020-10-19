import tkinter as tk
from tkinter import filedialog

top = tk.Tk()
M = tk.Menu()
top.title("Hello")
counter = 1


def call():
    global counter
    L1.configure(text=f"You clicked:  {counter} times")
    counter += 1


def file1():
    filedialog.askopenfile()


B = tk.Button(top, text="button", command=call)
L = tk.Label(top, text="Label")
L1 = tk.Label(top, text="You clicked: 0 times")
B1 = tk.Button(top, text="Open", command=file1)


L.pack()
B.pack()
L1.pack()
# B1.pack()

top.mainloop()
