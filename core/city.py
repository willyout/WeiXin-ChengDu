# -*- coding: utf-8 -*-

# SAE doesn't allow file read or write

citycode = {}

def init():
    global citycode
    if len(citycode) != 0:
        return
    citycode = loadcode()

def loadcode():
    code = {}
    with open('../data/citycode', 'r') as codefile:
        for line in codefile:
            text = line.decode('utf-8').strip().split()
            code[text[0]] = text[1]
    return code

def getcode(city):
    global citycode
    init()
    if citycode.has_key(city):
        return citycode[city]
    return None

def exist(city):
    global citycode
    init()
    return citycode.has_key(city)

if __name__ == '__main__':
    # print(getcode('成都'))
    # print(getcode(u'成都'))
    print(loadcode())