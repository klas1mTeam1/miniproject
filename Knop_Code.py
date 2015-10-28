from tkinter import *
import tkinter as tk

window = Tk()

#Zet het venster in het midden van het scherm.
window.withdraw()
window.update_idletasks()
w = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2.1
h = (window.winfo_screenheight() - window.winfo_reqheight()) / 2.1
window.geometry("+%d+%d" % (w, h))
window.deiconify()

#Geeft het venster standaard NS geel achtergrond.
window.tk_setPalette(background='#FECE22')

#Standaard venster met keuze.
window.title("Actuele vertrektijden")
label = Label(window, text='Van welk station wilt u de actuele vertrektijden opvragen?', fg='#003399')
label.pack()

#Geeft een tekstvakje en "OK" knop onder de knop "Ander station" als je er op klikt. (Returned de ingevoerde tekst nog niet)
def tekstvak():
    tekstvakje = tk.Entry(window, bg='white')
    tekstvakje.pack(pady=5)
    tekstvakje.focus_set()
    #Zorgt voor het returnen van de ingevulde tekst.
    def callback():
        content = tekstvakje.get()
        print(content)
    ok_knop = Button(window, text='OK', fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", command = callback)
    ok_knop.pack(pady=5)

#Voegt een knop aan het venster om te kiezen voor het huidige station. (Doet nog niks)
knop_huidig_station = Button(window, text="Utrecht Centraal", fg="white", bg="#003399", activebackgroun = "white", activeforeground = "#003399")
knop_huidig_station.pack(pady=5)

#Voegt een knip aan het venster om te kiezen voor een ander station.
knop_ander_station = Button(window, text="Ander station", fg="white", bg="#003399", activebackgroun = "white", activeforeground = "#003399", command = (tekstvak))
knop_ander_station.pack(pady=5)

window.mainloop()