# -*- coding: utf-8 -*-

import functext

def gototext(keyword):
    if keyword['msgtype'] == 'text':
        print('type content', type(keyword['content']))
        content = keyword['content'].encode("utf-8")  
        for func in functext.funclist:
            result = func(content)
            if result is not None:
                return result
        return None
    return None

def gotoevent(keyword):
    if keyword['msgtype'] == 'event' and keyword['event'] == 'subscribe':
        echostr = static.welcome
        return echostr
    return None

funclist = (gotoevent, gototext)