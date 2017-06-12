#!/usr/bin/env python

"""Auslesen von Sensorwerte aus Home Assistant"""

__author__      = "FarbenFroh"

import homeassistant.remote as remote
import configparser
import time

#Config
Config = configparser.ConfigParser()
Config.read("config.conf")

#Connect to Home Assistant
api = remote.API(Config.get('HomeAssistant', 'IP'), Config.get('HomeAssistant', 'PW'))

#Create lists for sensor IDs
temperature_ids = []
co2_ids = []
humidity_ids = []

#Get Sensor IDs from Home Assistant
entities = remote.get_states(api)
for entity in entities:
    if str(entity).__contains__(Config.get('Sensors', 'Room')) and not str(entity).__contains__("group"):
        #print(entity)
        if str(entity).__contains__("V_TEMP"):
            temperature_ids.append(entity.entity_id)
        elif str(entity).__contains__("V_LEVEL"):
            co2_ids.append(entity.entity_id)
        elif str(entity).__contains__("V_HUM"):
            humidity_ids.append(entity.entity_id)


#Get Avergage State of on Sensor Class
def getStateAvg(api, list):
    i = 0
    sum = 0
    for list_item in list:
        value = remote.get_state(api, list_item)
        sum = sum + float(value.state)
        i = i + 1
    if(i>0):
        avg = sum/i
    else:
        avg = 0
    return avg

def setLightColor(api, values):

    print("Do Light")
    print("Temp Min: " + str(values['temp_min']))
    print(values['temp_bright'])

    print("Hum Max: " + str(values['hum_max']))
    print(values['hum_bright'])

#Permament loop
run = True
while run:
    #Get average values
    values = {'temp_min':False,'temp_max':False,'temp_bright':0,'hum_min':False,'hum_max':False,'hum_bright':0,'Co2_max':False,'Co2_bright':0}


    tempAvg = getStateAvg(api, temperature_ids)
    if tempAvg < int(Config.get('Sectors', 'Temp_Min')):
        values['temp_min'] = True
        values['temp_bright'] = (tempAvg - int(Config.get('Sectors', 'Temp_Min'))) * -10
    elif tempAvg > int(Config.get('Sectors', 'Temp_Max')):
        values['temp_max'] = True
        values['temp_bright'] = (tempAvg - int(Config.get('Sectors', 'Temp_Max'))) * 10

    humAvg = getStateAvg(api, humidity_ids)
    if humAvg < int(Config.get('Sectors', 'Hum_Min')):
        values['hum_min'] = True
        values['hum_bright'] = (humAvg - int(Config.get('Sectors', 'Hum_Min'))) * -5
    elif humAvg > int(Config.get('Sectors', 'Hum_Max')):
        values['hum_max'] = True
        values['hum_bright'] = (humAvg - int(Config.get('Sectors', 'Hum_Max'))) * 5

    Co2Avg =  getStateAvg(api, co2_ids)
    if Co2Avg > int(Config.get('Sectors', 'Co2_Max')):
        values['Co2_max'] = True
        values['Co2_bright'] = (Co2Avg - int(Config.get('Sectors', 'Co2_Max'))) * 500

    setLightColor(api, values)

    #Delay between call
    time.sleep(int(Config.get('System', 'Delay')))
