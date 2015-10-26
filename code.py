__author__ = 'marce'

from tkinter import *

root = Tk()
root.title("Super Wonder Captain")

root.withdraw()
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
root.geometry("+%d+%d" % (x, y))
root.deiconify()

frontpic = PhotoImage(file="frontpage_pic.gif")
label = Label(root, image=frontpic)
label.pack()

start_knop = Button(text="Click here to start the game", fg="blue")
start_knop.pack(side=BOTTOM)


root.mainloop()