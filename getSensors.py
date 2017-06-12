#!/usr/bin/env python

"""Auslesen von Sensorwerte aus Home Assistant"""

__author__      = "FarbenFroh"

import homeassistant.remote as remote

#Config
HASS_IP = '192.168.1.188'
HASS_PW = ''
ROOM = "eg125"

#Connect to Home Assistant
api = remote.API(HASS_IP, HASS_PW)

#get all sensor entities
print('\n-- Available entities:')
entities = remote.get_states(api)
for entity in entities:
    if str(entity).__contains__(ROOM) and not str(entity).__contains__("group"):
        print(entity)

