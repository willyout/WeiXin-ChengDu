# -*- coding: utf-8 -*-

import weixin
import static
import funcall

def route(xmlstr):
    echostr = static.down
    try:
        keyword = weixin.parsemessage(xmlstr)
        echostr = decide(keyword)
    except Exception, e:
        print('i got exception', str(e))
    finally:
        return weixin.echomessage(keyword['fromusername'], keyword['tousername'], echostr)

def decide(keyword):
    for func in funcall.funclist:
        result = func(keyword)
        if result is not None:
            return result
            
    return static.fault
