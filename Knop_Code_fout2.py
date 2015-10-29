__author__ = 'Youri'

from tkinter import *
import tkinter as tk
import requests
import codecs
import Startscherm
import Knop_Code_fout
import Utrecht_centraal_in_tkinter_interface

# Geeft een tekstvakje en "OK" knop onder de knop "Ander station" als je er op klikt.
def tekstvak():
    knop_ander_station.configure(state = DISABLED)
    tekstvakje = tk.Entry(window, bg='white')
    tekstvakje.pack(pady=5)
    tekstvakje.focus_set()
    # Zorgt voor het returnen van de ingevulde tekst en gaat naar het volgende venster.
    def callback():
        global content
        content = tekstvakje.get()

        auth_details = ('martijn.dull@student.hu.nl', '0yZyZgme8551xHmiqvTNBxl-iMl0xOPZ0pDQxbTN2-R5ZWQQXrvRwA') #inlogcodes NS-API

        try:
            url = 'http://webservices.ns.nl/ns-api-avt?station='
            as_id = content
            new_url = "{}{}".format(url,as_id)
            actueel_as = requests.get(new_url, auth=auth_details) #actuele vertrekinformatie van de gewenste station
        except:
            print("Kan geen verbinding maken met de NS API.")
            sys.exit()

        def schrijf_actueel_as_xml(): #schrijft een xml bestand van de actuele vertrekinformatie van de gewenste station
            bestand = open('actueel_as.xml', 'w')
            bestand = codecs.open('actueel_as.xml', "w", "utf-8")
            bestand.write(str(actueel_as.text))
            bestand.close()

        schrijf_actueel_as_xml()

        def check_station():
            error = "No station found for input"
            error2 = "station parameter should be provided"
            bestand = open('actueel_as.xml', 'r')
            data = bestand.read()
            if error in data:
                window.destroy()
                Knop_Code_fout.scherm()
            elif error2 in data:
                window.destroy()
                Knop_Code_fout.scherm()
            else:
                print('Goed')
                window.destroy()
            bestand.close()
        check_station()
    ok_knop = Button(window, text='OK', fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", command = callback)
    ok_knop.pack(pady=5)

# Geeft functionaliteit aan de "Terug naar het hoofdmenu" knop.
def terug_hoofdmenu():
    window.destroy()
    Startscherm.create_window()

# Geeft functionaliteit aan de "Utrecht Centraal" knop.
def knop_utrecht():
    window.destroy()
    Utrecht_centraal_in_tkinter_interface.utrecht_scherm()

def scherm():
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
    window.title("Actuele vertrektijden")
    titel = Label(window, text='\nActuele vertrektijden.\n', fg='#003399', font = ('Ariel',24, 'bold'))
    titel.pack()
    subtitel = Label(window, text='Van welk station wilt u de actuele vertrektijden opvragen?\n', fg='#003399', font = ('Ariel',18))
    subtitel.pack()
    error_tekst = Label(window, text = 'Het ingevoerde station bestaat niet.\n', fg='red', font = ('Ariel', 14, 'bold'))
    error_tekst.pack()


    # Voegt een knop aan het venster om te kiezen voor het huidige station.
    knop_huidig_station = Button(window, text="Utrecht\nCentraal", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 10, command = knop_utrecht)
    knop_huidig_station.pack(pady=5)

    # Voegt een knop aan het venster om te kiezen voor een ander station.
    knop_ander_station = Button(window, text="Ander\nstation", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 10, command = tekstvak)
    knop_ander_station.pack(pady=5)

    # Voegt een aan het venster om te kiezen om terug te gaan naar het hoofdmenu.
    knop_terug = Button(window, text="Terug naar\nhet hoofdmenu", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 15, command = terug_hoofdmenu)
    knop_terug.pack()
    knop_terug.place(relx=0.01, rely=0.9)

    window.mainloop()
