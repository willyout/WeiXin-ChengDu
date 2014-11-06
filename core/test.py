# -*- coding: utf-8 -*-

textreply = u"""<xml>
            <ToUserName><![CDATA[{0}]]></ToUserName>
            <CreateTime>{1}</CreateTime>
            </xml>"""

content = u'你好'

content = textreply.format(content, content)
ss = 'http://update2.8684.cn/down/lincang.bus'
print(''ss.split('/')[-1])
