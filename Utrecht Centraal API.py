__author__ = 'Martijn'

#Deze code haalt data uit de NS-API en verwerkt de benodigde data met betrekking tot actuele vertrekinformatie.

import requests
import codecs
import xmltodict

auth_details = ('martijn.dull@student.hu.nl', '0yZyZgme8551xHmiqvTNBxl-iMl0xOPZ0pDQxbTN2-R5ZWQQXrvRwA') #inlogcodes NS-API

actueel_utrecht = requests.get('http://webservices.ns.nl/ns-api-avt?station=ut', auth=auth_details) #actuele vertrekinformatie Utrecht Centraal

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

def print_actueel_utrecht(actueel_utrecht_dict): #print de actuele vertrekinformatie van Station Utrecht Centraal
    index = 0
    for rit in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein']:
        print('De ' + str(rit['TreinSoort'])
              + ' van ' + str(rit['VertrekTijd'][11:16])
              + ' richting ' + str(rit['EindBestemming'])
              + ' vertrekt vanaf spoor ' + str(rit['VertrekSpoor']['#text']) + '.')
        if 'RouteTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print('Deze trein reist via ' + str(rit['RouteTekst']) + '.')
        if 'VertrekVertragingTekst' in actueel_utrecht_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print('De vertraging bedraagt ' + str(rit['VertrekVertragingTekst']) + '.')
        print('\n')
        index += 1

actueel_utrecht_dict = verwerk_actueel_utrecht_xml()
print_actueel_utrecht(actueel_utrecht_dict)
