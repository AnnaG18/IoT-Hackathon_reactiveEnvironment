#!/usr/bin/env python

"""Auslesen von Sensorwerte aus Home Assistant"""

__author__      = "FarbenFroh"

import homeassistant.remote as remote
import configparser
import time

#Config
Config = configparser.ConfigParser()
Config.read("config.conf")

ROOM = Config.get('Sensors', 'Room')

#Connect to Home Assistant
api = remote.API(Config.get('HomeAssistant', 'IP'), Config.get('HomeAssistant', 'PW'))

#get all sensor entities

temperature_ids = []
co2_ids = []
humidity_ids = []

entities = remote.get_states(api)
for entity in entities:
    if str(entity).__contains__(ROOM) and not str(entity).__contains__("group"):
        #print(entity)
        if str(entity).__contains__("TEMP"):
            temperature_ids.append(entity.entity_id)
        elif str(entity).__contains__("V_LEVEL"):
            co2_ids.append(entity.entity_id)
        elif str(entity).__contains__("HUM"):
            humidity_ids.append(entity.entity_id)



def getState(api, list):
    i = 0
    sum = 0
    for list_item in list:
        value = remote.get_state(api, list_item)
        sum = sum + float(value.state)
        i = i + 1
    avg = sum/i
    return avg

run = True
while run:
    print(getState(api, temperature_ids))
    print(getState(api, humidity_ids))
    print(getState(api, co2_ids))

    time.sleep(Config.get('System', 'Delay'))
