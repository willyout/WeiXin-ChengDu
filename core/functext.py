# -*- coding: utf-8 -*-

import bus
import static
import weather
import citysae

def gotohelp(content):
    if content.startswith(static.help):
        return static.helpyou
    return None

def gotobus(content):
    if content.startswith(static.bus):
        print('i am in bus')
        buscon = content.split() 

        print('len(buscon)', len(buscon))
        if len(buscon) == 3:
            return  bus.getlocation(buscon[1], buscon[2])
    return None

def gotoweather(content):
    if content.startswith(static.weather):
        citytext = content.split() 

        if len(citytext) == 2:
            print(citytext[1])
            cityun = citytext[1].decode('utf-8')
            print(repr(cityun))

            if not citysae.exist(cityun):
                return static.cityfault
            else:
                return weather.getdetails(cityun)
    return None

funclist = (gotohelp, gotobus, gotoweather)