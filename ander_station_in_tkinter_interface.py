from tkinter import *
import requests
import codecs
import xmltodict
import Startscherm
import Knop_Code
import geen_verbinding_api

def as_scherm():
    def terug_hoofdmenu():
        window.destroy()
        Startscherm.create_window()

    def terug():
        window.destroy()
        Knop_Code.scherm()

    def get_input():
        global content
        bestand = open('check_station.txt', 'r')
        content = bestand.read()
        bestand.close()

    get_input()

    auth_details = ('martijn.dull@student.hu.nl', '0yZyZgme8551xHmiqvTNBxl-iMl0xOPZ0pDQxbTN2-R5ZWQQXrvRwA') #inlogcodes NS-API

    try:
        url = 'http://webservices.ns.nl/ns-api-avt?station='
        as_id = content
        new_url = "{}{}".format(url,as_id)
        actueel_as = requests.get(new_url, auth=auth_details) #actuele vertrekinformatie van de gewenste station
    except:
        window.destroy()
        geen_verbinding_api.scherm_geen()

    def schrijf_actueel_as_xml(actueel_as): #schrijft een xml bestand van de actuele vertrekinformatie station
        bestand = open('actueel_as.xml', 'w')
        bestand = codecs.open('actueel_as.xml', "w", "utf-8")
        bestand.write(str(actueel_as.text))
        bestand.close()

    schrijf_actueel_as_xml(actueel_as)

    def verwerk_actueel_as_xml(): #verwerkt actuele vertrekinformatie station xml naar dictionary
        bestand = open('actueel_as.xml', 'r')
        xml_string = bestand.read()
        bestand.close()
        return xmltodict.parse(xml_string)

    def plaats_actueel_as_op_grid(root, actueel_as_dict): #print de actuele vertrekinformatie van station
        index = 0

        Label(topframe, anchor = NW, bg = '#FECE22').grid(row =0, column=0, sticky=NSEW)
        Label(topframe, anchor = NW, bg = '#FECE22').grid(row =0, column=1, sticky=NSEW)
        Label(topframe, anchor = NW, bg = '#FECE22').grid(row =0, column=2, sticky=NSEW)
        Label(topframe, anchor = NW, bg = '#FECE22').grid(row =0, column=3, sticky=NSEW)
        Label(topframe, anchor = NW, bg = '#FECE22').grid(row =0, column=4, sticky=NSEW)

        Label(topframe, text='Tijd', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, sticky=NSEW,)
        Label(topframe, text='Naar', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1, sticky=NSEW)
        Label(topframe, text='Spoor', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2, sticky=NSEW)
        Label(topframe, text='Via', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3, sticky=NSEW)
        Label(topframe, text='Reisdetails', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=4, sticky=NSEW)

        result = ""
        for rit in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein']:

            if index % 2 == 0:
                kleur = '#FFF5D6'
            else:
                kleur = 'white'

            if index > 16:
                break

            if 'RouteTekst' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
                routetekst  =  str(rit['RouteTekst'])
            else:
                routetekst   = ""

            if '#text' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]['VertrekSpoor']:
                VertrekSpoor = (str(rit['VertrekSpoor']['#text']))
            else:
                VertrekSpoor = ""

            if 'Opmerkingen' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
                Opmerkingen = ', ' + (str(rit['Opmerkingen']['Opmerking']))
            else:
                Opmerkingen  = ""

            if 'VertrekVertragingTekst' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
                VertrekVertragingTekst = (str(rit['VertrekVertragingTekst']))
            else:
                VertrekVertragingTekst = ""

            if 'VertrekTijd' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
                VertrekTijd = (str(rit['VertrekTijd'][11:16]))
            else:
                VertrekTijd = ""

            if 'EindBestemming' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
                EindBestemming = (str(rit['EindBestemming']))
            else:
                EindBestemming = ""

            if 'TreinSoort' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
                TreinSoort = (str(rit['TreinSoort']))
            else:
                TreinSoort = ""

            Label(topframe, text=str(VertrekTijd) + ' ' + str(VertrekVertragingTekst), background = kleur, anchor = NW, fg='#003399', font = ('Ariel',9, 'bold')).grid(row=index+2,column=0, sticky = NSEW)
            Label(topframe, text=EindBestemming, bg = kleur, fg='#003399', anchor = NW, font = ('Ariel',9, 'bold')).grid(row=index+2,column=1, sticky = NSEW)
            Label(topframe, text=VertrekSpoor, bg = kleur, fg='#003399', anchor = NW, font = ('Ariel',9, 'bold')).grid(row=index+2,column=2, sticky=NSEW)
            Label(topframe, text=str(routetekst), background = kleur, fg='#003399', anchor = NW, font = ('Ariel',9, 'bold')).grid(row=index+2,column=3, sticky=NSEW)
            Label(topframe, text=TreinSoort + Opmerkingen, wraplength = 100, justify = LEFT, bg = kleur, fg='#003399', anchor = NW, font = ('Ariel',9, 'bold')).grid(row=index+2,column=4, sticky=NSEW)

            index += 1

        return result

    actueel_as_dict = verwerk_actueel_as_xml()



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

    # Geeft het venster standaard NS geel achtergrond.
    window.tk_setPalette(background='#FECE22')

    global topframe
    topframe = Frame(window)
    topframe.pack()

    global bottomframe
    bottomframe = Frame(window, width=800, height=60)
    bottomframe.pack(side=BOTTOM)
    bottomframe.pack_propagate(0)
    bottomframe.place(relx=0, rely=0.88)

    plaats_actueel_as_op_grid(window, actueel_as_dict)

    # Standaard venster met keuze.
    window.title("Actuele vertrektijden van Station " + str(content))

    knop_terug = Button(bottomframe, text="Terug", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 15, command = terug)
    knop_terug.pack()
    knop_terug.place(relx=0.01, rely=0.2)

    knop_terug_hoofdmenu = Button(bottomframe, text="Terug naar\nhet hoofdmenu", fg="white", bg="#003399", activebackground = "white", activeforeground = "#003399", height = 2, width = 15, command = terug_hoofdmenu)
    knop_terug_hoofdmenu.pack()
    knop_terug_hoofdmenu.place(relx=0.165, rely=0.2)

    window.mainloop()