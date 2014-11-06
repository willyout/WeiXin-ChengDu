# -*- coding: utf-8 -*-

import static
import mylib

def getdict(word):
    url = static.frenchbase.format(mylib.quote(word))
    mylib.debug(url)
    text = mylib.fetchtext(url, static.frenchjquery, static.frenchnonejquery)
    return text

if __name__ == '__main__':
    print(getdict('pouvoir'))