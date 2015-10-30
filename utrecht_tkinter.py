__author__ = 'Team1'

from tkinter import *
import tkinter as tk
import os

#Deze code haalt data uit de NS-API en verwerkt de benodigde data met betrekking tot actuele vertrekinformatie.

import requests
import codecs
import xmltodict
import sys

auth_details = ('martijn.dull@student.hu.nl', '0yZyZgme8551xHmiqvTNBxl-iMl0xOPZ0pDQxbTN2-R5ZWQQXrvRwA') #inlogcodes NS-API

try:
    actueel_utrecht = requests.get('http://webservices.ns.nl/ns-api-avt?station=ut', auth=auth_details) #actuele vertrekinformatie Utrecht Centraal
except:
    print("Kan geen verbinding maken met de NS API.")
    sys.exit()


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

def gegevens_actueel_utrecht(actueel_utrecht_dict): #de actuele vertrekinformatie van Station Utrecht Centraal
    index = 0
    global treinsoort, vertrektijd, richting, spoor, routetekst, opmerkingen, vertraging
    for rit in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein']:
        vertrektijd = (rit['VertrekTijd'][11:16])
        treinsoort = (rit['TreinSoort'])
        richting = (rit['EindBestemming'])
        spoor = (rit['VertrekSpoor']['#text'])
        if 'RouteTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            routetekst = ('Deze trein reist via ' + str(rit['RouteTekst']) + '.')
        else:
            routetekst = ""
        if 'Opmerkingen' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            opmerkingen = (rit['Opmerkingen']['Opmerking'])
        else:
            opmerkingen = ""
        if 'VertrekVertragingTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
             vertraging = (rit['VertrekVertragingTekst'])
        else:
            vertraging = ""
        index += 1

actueel_utrecht_dict = verwerk_actueel_utrecht_xml()
gegevens_actueel_utrecht(actueel_utrecht_dict)

window = Tk()
window.wm_title("Utrecht Centraal")

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

label = Label(window, text= treinsoort + vertrektijd + richting + spoor + routetekst + opmerkingen + vertraging )
label.grid(row=0, column=0)


# Geeft het venster standaard NS geel achtergrond.
window.tk_setPalette(background='#FECE22')

window.mainloop()