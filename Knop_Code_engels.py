__author__ = 'Team1'

from tkinter import *
import tkinter as tk
import requests
import codecs
import Startscherm_engels
import Knop_Code_fout_engels
import Utrecht_centraal_in_tkinter_interface_engels
import ander_station_in_tkinter_interface_engels
import geen_verbinding_api_engels

def tekstvak():
    """Geeft een tekstvakje en "OK" knop onder de knop "Ander station" als je er op klikt."""
    knop_ander_station.configure(state = DISABLED)
    tekstvakje = tk.Entry(window, bg='white')
    tekstvakje.pack(pady=5)
    tekstvakje.focus_set()
    def callback():
        """Zorgt voor het returnen van de ingevulde tekst en gaat naar het volgende venster."""
        global content
        content = tekstvakje.get()

        auth_details = ('martijn.dull@student.hu.nl', '0yZyZgme8551xHmiqvTNBxl-iMl0xOPZ0pDQxbTN2-R5ZWQQXrvRwA') #inlogcodes NS-API

        try:
            url = 'http://webservices.ns.nl/ns-api-avt?station='
            as_id = content
            new_url = "{}{}".format(url,as_id)
            actueel_as = requests.get(new_url, auth=auth_details) #actuele vertrekinformatie van de gewenste station
        except:
            window.destroy()
            geen_verbinding_api_engels.scherm_geen()

        def schrijf_actueel_as_xml():
            """Schrijft een xml bestand van de actuele vertrekinformatie van de gewenste station"""
            bestand = open('actueel_as.xml', 'w')
            bestand = codecs.open('actueel_as.xml', "w", "utf-8")
            bestand.write(str(actueel_as.text))
            bestand.close()

        schrijf_actueel_as_xml()

        def check_station_bestand():
            """Schrijft de ingevoerde tekst naar een bestand zodat het later gecontroleerd kan worden."""
            bestand = open('check_station.txt', 'w')
            bestand.write(content)
            bestand.close()

        check_station_bestand()

        def check_station():
            """Controle voor het ingevulde station. Als er een error voor komt wordt er een error tekst weergeven."""
            error = "error"
            bestand = open('actueel_as.xml', 'r')
            data = bestand.read()
            if error in data:
                window.destroy()
                Knop_Code_fout_engels.scherm()
            else:
                window.destroy()
                ander_station_in_tkinter_interface_engels.as_scherm()
            bestand.close()
        check_station()
    ok_knop = Button(window, text='OK', fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", command = callback)
    ok_knop.pack(pady=5)

def terug_hoofdmenu():
    """Deze functie is gekoppeld aan de knop terug hoofdmenu, deze code zorgt ervoor dat het huidige scherm wordt gesloten en opent de functi
    create_window() van het bestand Startscherm.py"""
    window.destroy()
    Startscherm_engels.create_window()

def knop_utrecht():
    """Deze functie is gekoppeld aan de knop Utrecht Centraal, deze code zorgt ervoor dat het huidige scherm wordt gesloten en opent de functi
    utrecht_scherm() van het bestand Utrecht_centraal_in_tkinter.py"""
    window.destroy()
    Utrecht_centraal_in_tkinter_interface_engels.utrecht_scherm()

def scherm():
    """Deze functie maakt het venster en verzorgt de opmaak van het scherm."""
    global window
    global knop_ander_station

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
    window.title("Current departures")
    titel = Label(window, text='\nCurrent departures.\n', fg='#003399', font = ('Ariel',24, 'bold'))
    titel.pack()
    subtitel = Label(window, text='What station would you like to request current departures of?\n', fg='#003399', font = ('Ariel',18))
    subtitel.pack()


    # Voegt een knop aan het venster om te kiezen voor het huidige station.
    knop_huidig_station = Button(window, text="Utrecht\nCentraal", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 10, command = knop_utrecht)
    knop_huidig_station.pack(pady=5)

    # Voegt een knop aan het venster om te kiezen voor een ander station.
    knop_ander_station = Button(window, text="Different\nstation", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 10, command = tekstvak)
    knop_ander_station.pack(pady=5)

    # Voegt een aan het venster om te kiezen om terug te gaan naar het hoofdmenu.
    knop_terug = Button(window, text="Back to\nmain menu", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 15, command = terug_hoofdmenu)
    knop_terug.pack()
    knop_terug.place(relx=0.01, rely=0.9)

    window.mainloop()
