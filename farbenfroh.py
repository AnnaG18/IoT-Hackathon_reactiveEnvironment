#!/usr/bin/env python

"""Auslesen von Sensorwerte aus Home Assistant zur Visuellen Rückmeldung der Raumqualität über eine im Raum angebrachte Lampe"""

__author__      = "FarbenFroh"

import homeassistant.remote as remote
import configparser
import ast
import time
import logging

#Config
Config = configparser.ConfigParser()
Config.read("config.ini")
logging.basicConfig(format='%(asctime)s;%(message)s', datefmt='%Y.%m.%d;%H:%M:%S', level=logging.INFO, filename='sensor.csv')

#Connect to Home Assistant
api = remote.API(Config.get('HomeAssistant', 'IP'), Config.get('HomeAssistant', 'PW'))

#Create lists for sensor IDs
temperature_ids = []
co2_ids = []
humidity_ids = []

#Global Variable
goodRoom = True

#Get relevant sensor IDs from Home Assistant
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


#Get Avergage State of on list with sensor values
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

#Let the light pulsating to a maximum brightness
def pulsatingLightCall(api, exceeded, bright_max, color):
    #actual brightness
    bright = 1.0
    #when the maximum brigthness is reached
    reachedmax = False
    lamp = Config.get('Sensors', 'Lamp')
    global goodRoom

    #Loop to control the light
    while (exceeded == True):
        if bright <= bright_max and not reachedmax:
            bright = bright + 1
            if (bright == bright_max):
                reachedmax = True
        else:
            if bright == 1:
                exceeded = False
                reachedmax = False
                #Set global variable that one value is out of the defined borders
                goodRoom = False

            bright = bright - 1

        #Call Home Assistant to set the light
        remote.call_service(api, 'light', 'turn_on', {'entity_id': lamp, 'brightness': bright, 'rgb_color': color})
        #Wait 0,1 seconds to make the brightness change smooth
        time.sleep(0.1)

#Call the diferent functions for the values
def setLightColor(api, values):

    #Mimimum temprature
    color = ast.literal_eval(Config.get('Sectors', 'Temp_Min_Color'))
    pulsatingLightCall(api, values['temp_min'], values['temp_bright'], color)

    #Maximum temprature
    color = ast.literal_eval(Config.get('Sectors', 'Temp_Max_Color'))
    pulsatingLightCall(api, values['temp_max'], values['temp_bright'], color)

    #Minimum humidity
    color = ast.literal_eval(Config.get('Sectors', 'Hum_Min_Color'))
    pulsatingLightCall(api, values['hum_min'], values['hum_bright'], color)

    #Maximum humidity
    color = ast.literal_eval(Config.get('Sectors', 'Hum_Max_Color'))
    pulsatingLightCall(api, values['hum_max'], values['hum_bright'], color)

    #Maximum Co2
    color = ast.literal_eval(Config.get('Sectors', 'Co2_Max_Color'))
    pulsatingLightCall(api, values['Co2_max'], values['Co2_bright'], color)

    #When no value border is exceeded set the light to default
    if goodRoom:
        color = ast.literal_eval(Config.get('Sectors', 'Default_Color'))
        remote.call_service(api, 'light', 'turn_on', {'entity_id': Config.get('Sensors', 'Lamp'), 'brightness': 1, 'rgb_color': color})
        time.sleep(10)

#Check that the brightness value is in the range from 0 to 100
def maxBright(value):
    if(value>100):
        value = 100
    elif(value<1):
        value = 1
    return value

#Logging function
#def logging(name):
#    print (name + " : " + str(time.ctime()))

values = {'temp_min':False,'temp_max':False,'temp_bright':0,'hum_min':False,'hum_max':False,'hum_bright':0,'Co2_max':False,'Co2_bright':0}

#Permament loop
run = True
while run:
    goodRoom = True
    tempAvg = getStateAvg(api, temperature_ids)
    if tempAvg < int(Config.get('Sectors', 'Temp_Min')):
        values['temp_bright'] = maxBright((tempAvg - int(Config.get('Sectors', 'Temp_Min'))) * -10)
        if values['temp_min'] == False:
            values['temp_min'] = True
            logging.info("Temp;Min;"+str(values['temp_bright']))
        if values['temp_max'] == True:
            values['temp_max'] = False
    elif tempAvg > int(Config.get('Sectors', 'Temp_Max')):
        values['temp_bright'] = maxBright((tempAvg - int(Config.get('Sectors', 'Temp_Max'))) * 10)
        if values['temp_max'] == False:
            values['temp_max'] = True
            logging.info("Temp;Max;"+str(values['temp_bright']))
        if values['temp_min'] == True:
            values['temp_min'] = False
    elif values['temp_min'] == True or values['temp_max'] == True:
        values['temp_min'] = False
        values['temp_max'] = False
        logging.info("Temp;Normal;0")

    humAvg = getStateAvg(api, humidity_ids)
    if humAvg < int(Config.get('Sectors', 'Hum_Min')):
        values['hum_bright'] = maxBright((humAvg - int(Config.get('Sectors', 'Hum_Min'))) * -5)
        if values['hum_min'] == False:
            values['hum_min'] = True
            logging.info("Hum;Min;"+str(values['hum_bright']))
        if values['hum_max'] == True:
            values['hum_max'] = False
    elif humAvg > int(Config.get('Sectors', 'Hum_Max')):
        values['hum_bright'] = maxBright((humAvg - int(Config.get('Sectors', 'Hum_Max'))) * 5)
        if values['hum_max'] == False:
            values['hum_max'] = True
            logging.info("Hum;Max;"+str(values['hum_bright']))
        if values['hum_min'] == True:
            values['hum_min'] = False
    elif values['hum_min'] == True or values['hum_max'] == True:
        values['hum_min'] = False
        values['hum_max'] = False
        logging.info("Hum;Normal;0")

    Co2Avg =  getStateAvg(api, co2_ids)
    if Co2Avg > int(Config.get('Sectors', 'Co2_Max')):
        values['Co2_bright'] = maxBright((Co2Avg - int(Config.get('Sectors', 'Co2_Max'))) * 0.1)
        if values['Co2_max'] == False:
            values['Co2_max'] = True
            logging.info("Co2;Max;"+str(values['Co2_bright']))
    elif values['Co2_max'] == True:
        values['Co2_max'] = False
        logging.info("Co2;Normal;0")

    logging.debug(values)
    setLightColor(api, values)
