from tkinter import *
master = Tk()

def callback():
    print("you clicked the button")

btn = Button(master,text="ok",command=callback())
btn.pack()
mainloop()
