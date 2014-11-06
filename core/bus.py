# -*- coding: utf-8 -*-

import static
import mylib

def getlocation(num, station):
    url = static.buslocationbase.format(mylib.quote(num), mylib.quote(station))
    text = mylib.fetchtext(url, static.buslocationjquery)
    texts = text.split()
    if len(texts) >= 3:
    	return render(texts[0:len(texts) -1])
    return text

def render(texts):
    return static.busfenge.join(texts)

if __name__ == '__main__':
    print(getlocation('21', '金站'))