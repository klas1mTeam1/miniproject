__author__ = 'marce'

from tkinter import *
import tkinter as tk

# Functie aangemaakt om de startscherm weer te geven.
def create_window():
    global root
    root = Tk()                 # Dit is het basis window.
    root.title("NS Automaat")              # titel van de window.
    root.configure(background='gold')

# onderstaande code zorgt ervoor dat de scherm in het midden van je monitor wordt weergegeven.
    root.withdraw()
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
    root.geometry("%sx%s+%d+%d" % (800, 600, 400, 150))
    root.resizable(0,0)
    root.deiconify()

# onderstaande code maakt de topframe en wordt ingepakt in de root window.
    topframe = Frame(root)
    topframe.pack()
# onderstaande code maakt de bottomframe aan en wordt ingepakt in de root window.

    bottomframe = tk.Frame(root, bg='midnightblue', width=800, height=50)
    bottomframe.pack(side=BOTTOM)
    root.mainloop()




create_window()