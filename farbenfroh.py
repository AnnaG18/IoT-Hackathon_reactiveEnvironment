#!/usr/bin/env python

"""Auslesen von Sensorwerte aus Home Assistant"""

__author__      = "FarbenFroh"

import homeassistant.remote as remote
import configparser
import ast
import time

#Config
Config = configparser.ConfigParser()
Config.read("config.ini")

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

values = {'temp_min':False,'temp_max':False,'temp_bright':0,'hum_min':False,'hum_max':False,'hum_bright':0,'Co2_max':False,'Co2_bright':0}

def callSetApi(api, exceeded, bright_max, color):
    bright = 1.0
    reachedmax = False
    lamp = Config.get('Sensors', 'Lamp')
    global goodRoom

    while (exceeded == True):
        print(bright)
        if bright <= bright_max and not reachedmax:
            bright = bright + 1
            if (bright == bright_max):
                reachedmax = True
        else:
            if bright == 1:
                exceeded = False
                reachedmax = False
                goodRoom = False

            bright = bright - 1

        remote.call_service(api, 'light', 'turn_on', {'entity_id': lamp, 'brightness': bright, 'rgb_color': color})
        time.sleep(0.1)

def setLightColor(api, values):
    lamp = Config.get('Sensors', 'Lamp')
    goodRoom = True

    color = ast.literal_eval(Config.get('Sectors', 'Temp_Min_Color'))
    callSetApi(api, values['temp_min'], values['temp_bright'], color)

    color = ast.literal_eval(Config.get('Sectors', 'Temp_Max_Color'))
    callSetApi(api, values['temp_max'], values['temp_bright'], color)

    color = ast.literal_eval(Config.get('Sectors', 'Hum_Min_Color'))
    callSetApi(api, values['hum_min'], values['hum_bright'], color)

    color = ast.literal_eval(Config.get('Sectors', 'Hum_Max_Color'))
    callSetApi(api, values['hum_max'], values['hum_bright'], color)

    color = ast.literal_eval(Config.get('Sectors', 'Co2_Max_Color'))
    callSetApi(api, values['Co2_max'], values['Co2_bright'], color)

    if goodRoom:
        color = ast.literal_eval(Config.get('Sectors', 'Default_Color'))
        remote.call_service(api, 'light', 'turn_on', {'entity_id': lamp, 'brightness': 1, 'rgb_color': color})

def maxBright(value):
    if(value>100):
        value = 100
    elif(value<1):
        value = 1
    return value

#Permament loop
run = True
while run:
    values = {'temp_min':False,'temp_max':False,'temp_bright':0,'hum_min':False,'hum_max':False,'hum_bright':0,'Co2_max':False,'Co2_bright':0}

    tempAvg = getStateAvg(api, temperature_ids)
    if tempAvg < int(Config.get('Sectors', 'Temp_Min')):
        values['temp_min'] = True
        values['temp_bright'] = maxBright((tempAvg - int(Config.get('Sectors', 'Temp_Min'))) * -10)
    elif tempAvg > int(Config.get('Sectors', 'Temp_Max')):
        values['temp_max'] = True
        values['temp_bright'] = maxBright((tempAvg - int(Config.get('Sectors', 'Temp_Max'))) * 10)

    humAvg = getStateAvg(api, humidity_ids)
    if humAvg < int(Config.get('Sectors', 'Hum_Min')):
        values['hum_min'] = True
        values['hum_bright'] = maxBright((humAvg - int(Config.get('Sectors', 'Hum_Min'))) * -5)
    elif humAvg > int(Config.get('Sectors', 'Hum_Max')):
        values['hum_max'] = True
        values['hum_bright'] = maxBright((humAvg - int(Config.get('Sectors', 'Hum_Max'))) * 5)

    Co2Avg =  getStateAvg(api, co2_ids)
    if Co2Avg > int(Config.get('Sectors', 'Co2_Max')):
        values['Co2_max'] = True
        values['Co2_bright'] = maxBright((Co2Avg - int(Config.get('Sectors', 'Co2_Max'))) * 0.1)

    setLightColor(api, values)

