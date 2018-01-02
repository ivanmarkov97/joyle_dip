import sys
import os
from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.wsgi
from django.core.wsgi import get_wsgi_application

define('port', type=int, default=8888)

class WSHandlerTest(tornado.web.RequestHandler):
    waiters = set()
    messages = []

    def get(self):
        if self in self.waiters:
            pass
        else:
            self.waiters.add(self)
        self.write('WebSocket connection' + ' ' + str(len(self.waiters)))
        #self.write(str(self.waiters))
        try:
            #message = self.get_argument("message", default="Nope")
            message = str(self.request.arguments['message'])
            self.messages.append(message)
            for mes in self.messages:
                self.write("<br>" + str(mes) + " from:" + str(self))
        except:
            self.write('epmty message')

    def open(self):
        self.write('Added new connection')
        self.waiters.add(self)

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'joyle.settings'
    sys.path.append('./joyle')
    parse_command_line()
    wsgi_app = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(wsgi_app)

    tornado_app = tornado.web.Application(
        [
            ('/ws_test/?.*', WSHandlerTest),
            ('/ws', WSHandler),
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ])

    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
