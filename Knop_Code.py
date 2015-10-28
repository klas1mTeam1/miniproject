from tkinter import *
import tkinter as tk
import os

# Geeft een tekstvakje en "OK" knop onder de knop "Ander station" als je er op klikt. (Returned de ingevoerde tekst nog niet)
def tekstvak():
    tekstvakje = tk.Entry(window, bg='white')
    tekstvakje.pack(pady=5)
    tekstvakje.focus_set()
    # Zorgt voor het returnen van de ingevulde tekst.
    def callback():
        content = tekstvakje.get()
        print(content)
        # exit(window)
    ok_knop = Button(window, text='OK', fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", command = callback)
    ok_knop.pack(pady=5)

# Geeft functionaliteit aan de "Terug naar het hoofdmenu" knop.
def terug_hoofdmenu():
    window.destroy()
    os.system('Startscherm.py')

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

# Geeft het venster standaard NS geel achtergrond.
window.tk_setPalette(background='#FECE22')

# Standaard venster met keuze.
window.title("Actuele vertrektijden")
titel = Label(window, text='Actuele vertrektijden.\n', fg='#003399', font = ('Ariel',24, 'bold'))
titel.pack()
subtitel = Label(window, text='Van welk station wilt u de actuele vertrektijden opvragen?\n', fg='#003399', font = ('Ariel',18, 'bold'))
subtitel.pack()


# Voegt een knop aan het venster om te kiezen voor het huidige station. (Doet nog niks)
knop_huidig_station = Button(window, text="Utrecht\nCentraal", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 10)
knop_huidig_station.pack(pady=5)

# Voegt een knop aan het venster om te kiezen voor een ander station.
knop_ander_station = Button(window, text="Ander\nstation", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 10, command = (tekstvak))
knop_ander_station.pack(pady=5)

# Voegt een aan het venster om te kiezen om terug te gaan naar het hoofdmenu. (Doet nog niks)
knop_terug = Button(window, text="Terug naar\nhet hoofdmenu", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 15, command = terug_hoofdmenu)
knop_terug.pack()
knop_terug.place(relx=0.01, rely=0.9)

window.mainloop()