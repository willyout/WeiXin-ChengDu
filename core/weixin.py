# -*- coding: utf-8 -*-

import static
import hashlib
import lxml.etree
import mylib
import time

def echoverify(signature, timestamp, nonce, echostr):
    token = static.token
    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = ''.join(tmplist)
    hashstr = hashlib.sha1(tmpstr).hexdigest()
    if hashstr == signature:
        return echostr
    return 'Error: ' + echostr

def echomessage(tousername, fromusername, content, msgtype = 'text'):
    createtime = str(int(time.time()))
    # echostr = static.textreply.format(tousername, fromusername, createtime, msgtype, content)
    echostr = static.textreply % (tousername, fromusername, createtime, msgtype, content)
    return echostr

def parsemessage(xmlstr):
    root = lxml.etree.fromstring(xmlstr)
    child = list(root)
    keyword = {}
    for i in child:
        # keyword[i.tag.lower()] = mylib.tostr(i.text)
        keyword[i.tag.lower()] = i.text
    return keyword

if __name__ == '__main__':
    print(int(time.time()))
    print(static.testmessage)
    print(parsemessage(static.testmessage))