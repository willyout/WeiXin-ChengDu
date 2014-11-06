# -*- coding: utf-8 -*-

import static

import sqlite3 

def tostr(word):
    if isinstance(word, unicode):
        return word
    return str(word)

def writebusdata():
    conn = sqlite3.connect('../data/8684/download/chengdu')
    cur = conn.cursor()
    cnbus = cur.execute('''select * from cnbus''')
    with open('../data/8684/modify/chengdu/cnbus', 'w') as cnbusfile:
        for bus in cnbus:
            bustr = map(tostr, bus)
            cnbusfile.write(' '.join(bustr).encode('utf-8'))
            cnbusfile.write('\n')

def getbusfileurl():
    from pyquery import PyQuery as pq
    page = pq('http://mobile.8684.cn/down', headers = static.UA)
    city = page('a')

    citydict = {}
    for c in city:
        cc = pq(c)
        href = cc.attr('href')
        title = cc.attr('title')
        if href.startswith('http://update2.8684.cn/down/') or href.startswith('http://update1.8684.cn/down/'):
            citydict[title] = 'http://update1.8684.cn/down/' + href.split('/')[-1][:-4]

    return citydict

def tohtml():
    html = '<!DOCTYPE html><html><head></head><body>{0}</body></html>'
    href = '<a href = {}>link</a>'
    body = ''
    for key, value in getbusfileurl().items():
        body = body + href.format(value)
    html = html.format(body)
    print(html)
    with open('../data/8684/web/down.html', 'w') as down:
        html = html.encode('utf-8')
        down.write(html)

def tofile():
    with open('../data/8684/web/down.txt', 'w') as down:
        for key, value in getbusfileurl().items():
            body = key + ' ' + value
            down.write(body.encode('utf-8'))
            down.write('\n')

if __name__ == '__main__':
    tofile()