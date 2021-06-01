import cherrypy

from lambda_function import lambda_handler

SECRET_KEY = "abc iii 990918"

class Server:
    @cherrypy.expose()
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def index(self):
        req = cherrypy.request.json

        if req['secret_key'] != SECRET_KEY:
            raise AttributeError('key is not matching')

        return lambda_handler({
            'data': req['data'],
            'class_args': req['class_args'],
            'make_future_dataframe_args': req['make_future_dataframe_args'],
        })

cherrypy.config.update({
    'server.socket_host':'0.0.0.0',
    'server.socket_port': 4128,
    'tools.trailing_slash.on': False # True is default
})

cherrypy.quickstart(Server())
