# -*- coding: utf-8 -*-
import sys
from pyquery import PyQuery
import static

py3k = sys.version_info.major == 3
py2k = not py3k

# if py3k:
#     basestring = unicode = str

def quote(unistr):
    if py2k:
        import urllib
        return urllib.quote(unistr)
    import urllib.parse
    return urllib.parse.quote(unistr)

def fetchtext(quoteurl, jquerytxt, jquerynonetxt = None):
    page = PyQuery(quoteurl, headers = static.UA)
    text = page(jquerytxt).text()
    if text is None and jquerynonetxt is not None:
        text = page(jquerynonetxt).text()
    return text

def debug(info):
    if static.DEBUG:
        print('DEBUG: ', str(id(info)) + '@' + info)

class mydict(dict):
    def __missing__(self, key):
        return None