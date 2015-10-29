__author__ = 'marce'

from tkinter import *
import tkinter as tk
import Knop_Code

# Hieronder een functie om knop 5 een opdracht te kunnen geven
def naar_knop_code():
    root.destroy()
    Knop_Code.scherm()

# Functie aangemaakt om de startscherm weer te geven.
def create_window():
    global root
    root = Tk()                 # Dit is het basis window.
    root.title("NS Automaat")              # titel van de window.
    root.configure(background='#FECE22')    # Achtergrond kleur

# onderstaande code zorgt ervoor dat de scherm in het midden van je monitor wordt weergegeven.
# Instellingen voor venster grootte en positie.
    root.withdraw()
    root.update_idletasks()
    w = 700 # Breedte van het venster.
    h = 500 # Hoogte van het venster.

    ws = root.winfo_screenwidth() # Breedte van het scherm.
    hs = root.winfo_screenheight() # Hoogte van het scherm.

# x en y coordinaten berekenen van het venster.
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

# Zet het venster op de goede plek met de goede grootte.
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.deiconify()

# onderstaande code maakt de topframe en wordt ingepakt in de root window.
    global topframe
    topframe = Frame(root)
    topframe.pack()
# onderstaande code maakt de bottomframe aan en wordt ingepakt in de root window.
    global bottomframe
    bottomframe = Frame(root, bg='midnightblue', width=800, height=60)
    bottomframe.pack(side=BOTTOM)
    bottomframe.pack_propagate(0)


# onderstaande code voegt de vlag knoppen voor nederlands en engels.
    photo_nl = PhotoImage(file='nl_icon.gif')
    label_nl = Button(bottomframe,image=photo_nl, bg='#003399')
    label_nl.pack()
    label_nl.place(relx=0.02, rely=0.1)

    photo_uk = PhotoImage(file='uk_icon.gif')
    label_uk = Button(bottomframe, image=photo_uk, bg='#003399')
    label_uk.pack()
    label_uk.place(relx=0.133, rely=0.1)

# onderstaande de labels voor tekst onder de vlaggen.
    tekst_nl = Label(bottomframe, text='Nederlands', bg='#003399', fg='white', font=('Ariel',10,'bold'))
    tekst_nl.pack()
    tekst_nl.place(relx=0.01, rely=0.7)

    tekst_uk = Label(bottomframe, text='English', bg='#003399', fg='white', font=('Ariel',10,'bold'))
    tekst_uk.pack()
    tekst_uk.place(relx=0.142, rely=0.7)


# onderstaande code voegt de logos van de betaalmogelijkheden
    photo_maestro = PhotoImage(file='maestro.gif')
    maestro_label = Label(bottomframe, image=photo_maestro, bg='#003399')
    maestro_label.pack()
    maestro_label.place(relx=0.4, rely=0.08)

    photo_vpay = PhotoImage(file='vpay.gif')
    vpay_label = Label(bottomframe, image=photo_vpay, bg='#003399')
    vpay_label.pack()
    vpay_label.place(relx=0.475, rely=0.07)

    photo_visa = PhotoImage(file='visa.gif')
    visa_label = Label(bottomframe, image=photo_visa, bg='#003399')
    visa_label.pack()
    visa_label.place(relx=0.538, rely=0.08)

    photo_mastercard = PhotoImage(file='mastercard.gif')
    mastercard_label = Label(bottomframe, image=photo_mastercard, bg='#003399')
    mastercard_label.pack()
    mastercard_label.place(relx=0.615, rely=0.08)

# onderstaande de code voor de welkomtekst.
    welkom = Label(topframe, text='\n\nWelkom bij NS')
    welkom.config(foreground='#003399', background='#FECE22', font=('Ariel',25,'bold'))
    welkom.pack()

# onderstaande de code voor een canvas
    canvas = Canvas(bg='white', height=160, width=290)      # Canvas parameters, achtergrond kleur, hoogdte en breedte.
    canvas.config(highlightbackground='#003399')            # hier wordt er een omranding van de kanvas toegevoegd.
    tekst_canvas = Label(text='Houd uw\nOV-chipkaart\nvoor de\nkaartlezer\nrechtsonder\nnaast het scherm.',
                         bg='white', fg='#003399', font=('Ariel',10, 'bold'))
    canvas.pack()
    tekst_canvas.pack()
    tekst_canvas.place(width=120, height=150, relx=0.3, rely=0.25)  #canvas positie en dimensies.

    canvas_af1 = PhotoImage(file='ov_hand.GIF')
    label_af1 = Label(image=canvas_af1, bg='#003399')
    label_af1.pack(padx=5, pady=5)
    label_af1.place(relx=0.5, rely=0.3)

    canvas_af2 = PhotoImage(file='arrow.gif')
    label_af2 = Label(image=canvas_af2, bg='white')
    label_af2.pack(padx=5, pady=5)
    label_af2.place(relx=0.65, rely=0.48)

# Hieronder maken we de knoppen
    knop1 = Button(text='Ik wil naar\nAmsterdam', bg='#003399', fg='white')
    knop2 = Button(text='Kopen\nlos kaartje', bg='#003399', fg='white')
    knop3 = Button(text='Kopen\nOV-chipkaart', bg='#003399', fg='white')
    knop4 = Button(text='Ik wil naar\nhet buitenland', bg='#003399', fg='white')
    knop5 = Button(text='Actuele\nvertrektijden', bg='#003399', fg='white', command=naar_knop_code)


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
