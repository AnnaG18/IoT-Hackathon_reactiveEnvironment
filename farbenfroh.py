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

#Create Lists for Sensor IDs
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
    print(values['temp_min'])

#Permament loop
run = True
while run:
    #Get average values
    values = {'temp_min':False, 'temp_min_bright':0,'temp_max':False,'temp_max_bright':0,'hum_min':False,'hum_min_bright':0,'hum_max':False,'hum_max_bright':0,'Co2_max':False,'Co2_max_bright':0}


    tempAvg = getStateAvg(api, temperature_ids)
    if tempAvg < int(Config.get('Sectors', 'Temp_Min')):
        values['temp_min'] = True
    elif tempAvg > int(Config.get('Sectors', 'Temp_Max')):
        values['temp_max'] = True

    getStateAvg(api, humidity_ids), getStateAvg(api, co2_ids)
    setLightColor(api, values)

    #Delay between call
    time.sleep(int(Config.get('System', 'Delay')))
