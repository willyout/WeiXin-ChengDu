# -*- coding: utf-8 -*-

import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))

import tornado.web

from core import router

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            signature = self.get_argument('signature')
            timestamp = self.get_argument('timestamp')
            nonce = self.get_argument('nonce')
            echostr = self.get_argument('echostr')
            self.write(echoverify(signature, timestamp, nonce, echostr))
        except Exception, e:
            raise tornado.web.HTTPError(403) 

    def post(self):
        # self.set_header('Content-Type', 'application/xml; charset=utf-8')  
        self.set_header('Content-Type', 'application/xml')  
        self.write(router.route(self.request.body))

settings = {
    "debug": False,
}

application = tornado.web.Application([
    (r"/", MainHandler),
    # (r"/cron/news", MainHandler),
], **settings)
