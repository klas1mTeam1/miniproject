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
    root.geometry("%sx%s+%d+%d" % (700, 500, 400, 150))
    root.resizable(0,0)
    root.deiconify()

# onderstaande code maakt de topframe en wordt ingepakt in de root window.
    global topframe
    topframe = Frame(root)
    topframe.pack()
# onderstaande code maakt de bottomframe aan en wordt ingepakt in de root window.
    global bottomframe
    bottomframe = tk.Frame(root, bg='midnightblue', width=800, height=50)
    bottomframe.pack(side=BOTTOM)
    bottomframe.pack(fill=BOTH)

# onderstaande code voegt de vlag icons voor nederlands en engels.
    photo_nl = PhotoImage(file='nl_icon.gif')
    label_nl = Label(bottomframe, image=photo_nl)
    label_nl.pack(side=LEFT, padx=5, pady=5)

    photo_uk = PhotoImage(file='uk_icon.gif')
    label_uk = Label(bottomframe, image=photo_uk)
    label_uk.pack(side=LEFT, padx=5, pady=5)

# onderstaande de code voor de welkomtekst
    welkom = Label(topframe, text='\n\nWelkom bij NS')
    welkom.config(foreground='navy', background='gold', font=('Ariel',25,'bold'))
    welkom.pack()

# onderstaande de code voor een canvas
    canvas = Canvas(bg='white', height=160, width=290)
    canvas.config(highlightbackground='navy')
    tekst_canvas = Label(text='Houd uw\nOV-chipkaart\nvoor de\nkaartlezer\nrechtsonder\nnaast het scherm.',
                         bg='white', fg='navy', font=('Ariel',10, 'bold'))
    canvas.pack()
    tekst_canvas.pack()
    tekst_canvas.place(width=120, height=150, relx=0.3, rely=0.25)

    canvas_af1 = PhotoImage(file='ov_hand.GIF')
    label_af1 = Label(image=canvas_af1)
    label_af1.pack(padx=5, pady=5)
    label_af1.place(relx=0.5, rely=0.3)

    canvas_af2 = PhotoImage(file='arrow.gif')
    label_af2 = Label(image=canvas_af2)
    label_af2.pack(padx=5, pady=5)
    label_af2.place(relx=0.65, rely=0.48)

# Hieronder maken we de knoppen
    knop1 = Button(text='Ik wil naar\nAmsterdam', bg='navy', fg='white')
    knop2 = Button(text='Kopen\nlos kaartje', bg='navy', fg='white')
    knop3 = Button(text='Kopen\nOV-chipkaart', bg='navy', fg='white')
    knop4 = Button(text='Ik wil naar\nhet buitenland', bg='navy', fg='white')
    knop5 = Button(text='Vertrektijden\ntreinen', bg='navy', fg='white')


    knop1.pack()
    knop1.place(width=100, height=50, relx=0.15, rely=0.65)
    knop2.pack()
    knop2.place(width=100, height=50, relx=0.30, rely=0.65)
    knop3.pack()
    knop3.place(width=100, height=50, relx=0.45, rely=0.65)
    knop4.pack()
    knop4.place(width=100, height=50, relx=0.6, rely=0.65)
    knop5.pack()
    knop5.place(width=100, height=50, relx=0.75, rely=0.65)




    root.mainloop()


create_window()
