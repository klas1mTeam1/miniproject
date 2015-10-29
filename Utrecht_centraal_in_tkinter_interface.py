__author__ = 'Akshay, Martijn'
from tkinter import *
import tkinter as tk
import os
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
    return xmltodict.parse(xml_string)
    bestand.close()

def plaats_actueel_utrecht_op_grid(root, actueel_utrecht_dict): #print de actuele vertrekinformatie van Station Utrecht Centraal
    index = 0
    result = ""
    for rit in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein']:

        if 'RouteTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            routetekst  =  str(rit['RouteTekst'])
        else:
            routetekst   = ""

        if 'Opmerkingen' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            opmerkingen = (str(rit['Opmerkingen']['Opmerking']) + '.')
        else:
            opmerkingen  = ""

        if 'VertrekVertragingTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            VertekVertragingTekst = (str(rit['VertrekVertragingTekst']) + '.')
        else:
            VertekVertragingTekst = ""

        Label(root, text=str(rit['TreinSoort']), fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index,column=0)
        Label(root, text=str(rit['VertrekTijd'][11:16]), fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index,column=1)
        Label(root, text=str(rit['EindBestemming']), fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index,column=2)
        Label(root, text=str(routetekst), fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index,column=3)
        Label(root, text=str(opmerkingen), fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index,column=4)

        result = result + 'De ' + str(rit['TreinSoort'])
        result = result + ' van ' + str(rit['VertrekTijd'][11:16])
        result = result + ' richting ' + str(rit['EindBestemming'])
        result = result + ' vertrekt vanaf spoor ' + str(rit['VertrekSpoor']['#text']) + '.'
        if 'RouteTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print('Deze trein reist via ' + str(rit['RouteTekst']) + '.')
        if 'Opmerkingen' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print(str(rit['Opmerkingen']['Opmerking']) + '.')
        if 'VertrekVertragingTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print('De vertraging bedraagt ' + str(rit['VertrekVertragingTekst']) + '.')
        print('\n')
        index += 1

    return result

actueel_utrecht_dict = verwerk_actueel_utrecht_xml()





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

plaats_actueel_utrecht_op_grid(window, actueel_utrecht_dict)

# Standaard venster met keuze.
window.title("Actuele vertrektijden")



window.mainloop()

