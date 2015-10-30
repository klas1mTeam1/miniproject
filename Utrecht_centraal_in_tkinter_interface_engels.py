__author__ = 'Team1'

from tkinter import *
import requests
import codecs
import xmltodict
import Startscherm_engels
import Knop_Code_engels
import geen_verbinding_api

def terug_hoofdmenu():
    window.destroy()
    Startscherm_engels.create_window()

def terug():
    window.destroy()
    Knop_Code_engels.scherm()

auth_details = ('martijn.dull@student.hu.nl', '0yZyZgme8551xHmiqvTNBxl-iMl0xOPZ0pDQxbTN2-R5ZWQQXrvRwA') #inlogcodes NS-API

try:
    actueel_utrecht = requests.get('http://webservices.ns.nl/ns-api-avt?station=ut', auth=auth_details) #actuele vertrekinformatie Utrecht Centraal
except:
    window.destroy()
    geen_verbinding_api.scherm_geen()


def schrijf_actueel_utrecht_xml(actueel_utrecht): #schrijft een xml bestand van de actuele vertrekinformatie Station Utrecht Centraal
    bestand = open('actueel_utrecht.xml', 'w')
    bestand = codecs.open('actueel_utrecht.xml', "w", "utf-8")
    bestand.write(str(actueel_utrecht.text))
    bestand.close()

schrijf_actueel_utrecht_xml(actueel_utrecht)

def verwerk_actueel_utrecht_xml(): #verwerkt actuele vertrekinformatie Utrecht Centraal xml naar dictionary
    bestand = open('actueel_utrecht.xml', 'r')
    xml_string = bestand.read()
    bestand.close()
    return xmltodict.parse(xml_string)

def plaats_actueel_utrecht_op_grid(root, actueel_utrecht_dict): #print de actuele vertrekinformatie van Station Utrecht Centraal
    index = 0

    Label(topframe, text='Time', fg='#003399', font = ('Ariel',9, 'bold')).grid(row=0,column=0, sticky=NW)
    Label(topframe, text='To', fg='#003399', font = ('Ariel',9, 'bold')).grid(row=0,column=1, sticky=NW)
    Label(topframe, text='Track', fg='#003399', font = ('Ariel',9, 'bold')).grid(row=0,column=2, sticky=NW)
    Label(topframe, text='Direction', fg='#003399', font = ('Ariel',9, 'bold')).grid(row=0,column=3, sticky=NW)
    Label(topframe, text='Journey Details', fg='#003399', font = ('Ariel',9, 'bold')).grid(row=0,column=4, sticky=NW)

    result = ""
    for rit in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein']:
        if index==18:
            break


        if 'RouteTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            routetekst  =  str(rit['RouteTekst'])
        else:
            routetekst   = ""

        if 'Opmerkingen' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            opmerkingen = ', ' + (str(rit['Opmerkingen']['Opmerking']))
        else:
            opmerkingen  = ""

        if 'VertrekVertragingTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            VertekVertragingTekst = (str(rit['VertrekVertragingTekst']))
        else:
            VertekVertragingTekst = ""

        Label(topframe, text=str(rit['VertrekTijd'][11:16]) + ' ' + str(VertekVertragingTekst), fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index+1,column=0, sticky=NW)
        Label(topframe, text=str(rit['EindBestemming']), fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index+1,column=1, sticky=NW)
        Label(topframe, text=str(rit['VertrekSpoor']['#text']), fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index+1,column=2, sticky=NW)
        Label(topframe, text=str(routetekst), fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index+1,column=3, sticky=NW)
        Label(topframe, text=str(rit['TreinSoort']) + (opmerkingen), wraplength = 100, justify = LEFT, fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index+1,column=4, sticky=NW)

        index += 1

    return result

actueel_utrecht_dict = verwerk_actueel_utrecht_xml()

def utrecht_scherm():
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

    global topframe
    topframe = Frame(window)
    topframe.pack()

    global bottomframe
    bottomframe = Frame(window, width=800, height=60)
    bottomframe.pack(side=BOTTOM)
    bottomframe.pack_propagate(0)

    plaats_actueel_utrecht_op_grid(window, actueel_utrecht_dict)

    # Standaard venster met keuze.
    window.title("Current departures")

    knop_terug_hoofdmenu = Button(bottomframe, text="Return to\nmain menu", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 15, command = terug_hoofdmenu)
    knop_terug_hoofdmenu.pack()
    knop_terug_hoofdmenu.place(relx=0.19, rely=0.2)

    knop_terug = Button(bottomframe, text="Return", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 15, command = terug)
    knop_terug.pack()
    knop_terug.place(relx=0.01, rely=0.2)

    window.mainloop()
