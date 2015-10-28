__author__ = 'Martijn'

#Deze code haalt data uit de NS-API en verwerkt de benodigde data met betrekking tot actuele vertrekinformatie.

import requests
import codecs
import xmltodict
import sys

auth_details = ('martijn.dull@student.hu.nl', '0yZyZgme8551xHmiqvTNBxl-iMl0xOPZ0pDQxbTN2-R5ZWQQXrvRwA') #inlogcodes NS-API

try:
    lijst_stations = requests.get('http://webservices.ns.nl/ns-api-stations-v2', auth=auth_details)
except:
    print("Kan geen verbinding maken met de NS API.")
    sys.exit()

def schrijf_lijst_stations_xml(lijst_stations): #schrijft een xml bestand van lijst met alle stations.
    bestand = open('lijst_stations.xml', 'w')
    bestand = codecs.open('lijst_stations.xml', "w", "utf-8")
    bestand.write(str(lijst_stations.text))
    bestand.close()

schrijf_lijst_stations_xml(lijst_stations)

def verwerk_lijst_stations_xml(): #verwerkt lijst alle stations xml naar dictionary
    bestand = open('lijst_stations.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)
    bestand.close()

try:
    actueel_ander_station = requests.get('http://webservices.ns.nl/ns-api-avt?station=ut', auth=auth_details) #actuele vertrekinformatie gekozen station
except:
    print("Kan geen verbinding maken met de NS API.")
    sys.exit()


def schrijf_actueel_ander_station_xml(actueel_ander_station): #schrijft een xml bestand van de actuele vertrekinformatie gekozen station.
    bestand = open('actueel_ander_station.xml', 'w')
    bestand = codecs.open('actueel_ander_station.xml', "w", "utf-8")
    bestand.write(str(actueel_ander_station.text))
    bestand.close()

schrijf_actueel_ander_station_xml(actueel_ander_station)

def verwerk_actueel_ander_station_xml(): #verwerkt actuele vertrekinformatie gekozen station xml naar dictionary
    bestand = open('actueel_ander_station.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)
    bestand.close()

def print_actueel_ander_station(actueel_ander_station_dict): #print de actuele vertrekinformatie van gekozen station.
    index = 0
    for rit in actueel_ander_station_dict['ActueleVertrekTijden']['VertrekkendeTrein']:
        print('De ' + str(rit['TreinSoort'])
              + ' van ' + str(rit['VertrekTijd'][11:16])
              + ' richting ' + str(rit['EindBestemming'])
              + ' vertrekt vanaf spoor ' + str(rit['VertrekSpoor']['#text']) + '.')
        if 'RouteTekst' in actueel_ander_station_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print('Deze trein reist via ' + str(rit['RouteTekst']) + '.')
        if 'Opmerkingen' in actueel_ander_station_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print(str(rit['Opmerkingen']['Opmerking']) + '.')
        if 'VertrekVertragingTekst' in actueel_ander_station_dict['ActueleVertrekTijden']['VertrekkendeTrein'][index]:
            print('De vertraging bedraagt ' + str(rit['VertrekVertragingTekst']) + '.')
        print('\n')
        index += 1

actueel_ander_station_dict = verwerk_actueel_ander_station_xml()
print_actueel_ander_station(actueel_ander_station_dict)