__author__ = 'marce'

import requests
import codecs
import xmltodict
import sys


auth_details = ('martijn.dull@student.hu.nl', '0yZyZgme8551xHmiqvTNBxl-iMl0xOPZ0pDQxbTN2-R5ZWQQXrvRwA') #inlogcodes NS-API

try:
    url = 'http://webservices.ns.nl/ns-api-avt?station='
    as_id = input('Station: ')
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

def verwerk_actueel_as_xml(): #verwerkt actuele vertrekinformatie van de gewenste station xml naar dictionary
    bestand = open('actueel_as.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)
    bestand.close()

def print_actueel_as(actueel_as_dict): #print de actuele vertrekinformatie van de gewenste station
    index = 0
    for rit in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein']:
        print('De ' + str(rit['TreinSoort'])
              + ' van ' + str(rit['VertrekTijd'][11:16])
              + ' richting ' + str(rit['EindBestemming'])
              + ' vertrekt vanaf spoor ' + str(rit['VertrekSpoor']['#text']) + '.')
        if 'RouteTekst' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print('Deze trein reist via ' + str(rit['RouteTekst']) + '.')
        if 'Opmerkingen' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print(str(rit['Opmerkingen']['Opmerking']) + '.')
        if 'VertrekVertragingTekst' in actueel_as_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print('De vertraging bedraagt ' + str(rit['VertrekVertragingTekst']) + '.')
        print('\n')
        index += 1

actueel_as_dict = verwerk_actueel_as_xml()
print_actueel_as(actueel_as_dict)