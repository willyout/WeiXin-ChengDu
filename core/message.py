# -*- coding: utf-8 -*-

class RecvMessage(object):
    def __init__(self, **kwargs):
        if 'fromusername' in kwargs:
            self.fromusername = kwargs['kwargs']
    def __init__(self, **kwargs):
        if 'tousername' in kwargs:
            self.tousername = kwargs['tousername']
    def __init__(self, **kwargs):
        if 'msgid' in kwargs:
            self.msgid = kwargs['msgid']
    def __init__(self, **kwargs):
        if 'createtime' in kwargs:
            self.createtime = kwargs['createtime']
         
class RecvTextMessage(RecvMessage):
    def __init__(self, **kwargs):
        RecvMessage.__init__(self, **kwargs)
        self.type = 'text'
        if 'content' in kwargs:
            self.content = kwargs['content']
