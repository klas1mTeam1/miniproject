__author__ = 'Team1'

from tkinter import *
import Startscherm


# Geeft functionaliteit aan de "Terug naar het hoofdmenu" knop.
def terug_hoofdmenu():
    window.destroy()
    Startscherm.create_window()

def scherm_geen():
    global window
    window = Tk()

    # Instellingen voor venster grootte en positie.
    window.withdraw()
    window.update_idletasks()
    w = 700 # Breedte van het venster.
    h = 500 # Hoogte van het venster.

    ws = window.winfo_screenwidth() # Breedte van het scherm.
    hs = window.winfo_screenheight() # Hoogte van het scherm.

    # x en y coordinaten berekenen van het venster.
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Zet het venster op de goede plek met de goede grootte.
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.deiconify()
    window.resizable(0, 0)

    # Geeft het venster standaard NS geel achtergrond.
    window.tk_setPalette(background='#FECE22')

    # Standaard venster met keuze.
    window.title("Kan geen verbinding worden gemaakt met de NS servers")
    error_tekst = Label(window, text = 'Er kan geen verbinding worden gemaakt\nProbeer het opnieuw\nof vraag het aan de service balie ', fg='red', font = ('Ariel', 14, 'bold'))
    error_tekst.pack()

    # Voegt een aan het venster om te kiezen om terug te gaan naar het hoofdmenu.
    knop_terug = Button(window, text="Terug naar\nhet hoofdmenu", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 15, command = terug_hoofdmenu)
    knop_terug.pack()
    knop_terug.place(relx=0.01, rely=0.9)

    window.mainloop()
