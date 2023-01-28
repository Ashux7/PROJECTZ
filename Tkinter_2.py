from tkinter import *
from playsound import playsound
root = Tk()


root.geometry("690x690")
def music():
    playsound("D:\\ASHU\\codes\\PYTHON\\projects\\Make Me Move.mp3")

btn = Button(root,text="Click Krde bhai.",borderwidth=10,relief=GROOVE,font=('Algerian 20 italic'),command=music)
btn.pack()

root.mainloop()