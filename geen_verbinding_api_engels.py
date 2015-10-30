__author__ = 'Team1'

from tkinter import *
import Startscherm_engels


# Geeft functionaliteit aan de "Terug naar het hoofdmenu" knop.
def terug_hoofdmenu():
    """Deze functie is gekoppeld aan de knop terug hoofdmenu, deze code zorgt ervoor dat het huidige scherm wordt gesloten en opent de functi
    create_window() van het bestand Startscherm.py"""
    window.destroy()
    Startscherm_engels.create_window()

def scherm_geen():
    """Hier wordt een scherm geprogrameerd die aangeeft dat er geen verbinding mogelijk is, tevens wordt er een knop aangemaakt die je de optie
    geeft om terug te gaan naar de hoofdscherm"""
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
    window.title("Can't connect to the NS servers.")
    error_tekst = Label(window, text = 'No connection to the NS servers could be established.\nPlease retry\nor request help at the service desk.', fg='red', font = ('Ariel', 14, 'bold'))
    error_tekst.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Voegt een aan het venster om te kiezen om terug te gaan naar het hoofdmenu.
    knop_terug = Button(window, text="Back to\nmain menu", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 15, command = terug_hoofdmenu)
    knop_terug.pack()
    knop_terug.place(relx=0.01, rely=0.9)

    window.mainloop()