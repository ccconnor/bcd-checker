import tornado.ioloop
import tornado.web
from bitcoinrpc.authproxy import AuthServiceProxy

rpc_user = 'bitcoinrpc'
rpc_password = 'PealniejCytnemPhoocCooft'
rpc_host = '127.0.0.1'
rpc_port = 7116
rpc_url = "http://%s:%s@%s:%s" % (rpc_user, rpc_password, rpc_host, rpc_port)


class DefaultHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Error: 404')
        self.finish()


class MainHandler(tornado.web.RequestHandler):
    def get(self, height=None):
        try:
            bcd_server = AuthServiceProxy(rpc_url)
            blockhash = bcd_server.getblockhash(int(height))
            self.write(blockhash)
        except Exception as e:
            print('Error', e)
            self.write(str(e).split(':')[0])


def make_app():
    return tornado.web.Application([
        (r"/(\d{1,})", MainHandler),
        (r".*", DefaultHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
