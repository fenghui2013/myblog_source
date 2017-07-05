import tornado
import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])

def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
