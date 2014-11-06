# -*- coding: utf-8 -*-

import static

def getcode(city):
    if static.citycode.has_key(city):
        return static.citycode[city]
    return None

def exist(city):
    return static.citycode.has_key(city)

if __name__ == '__main__':
    print(getcode('成都'))
    print(getcode(u'成都'))
    print(exist(u'\u6210\u90fd'))