import os

import cherrypy
from jinja2 import Environment, FileSystemLoader


ENV = Environment(loader=FileSystemLoader('templates'))


def get_params():
    params = {'message': os.environ.get('message', ''),
              'user': os.environ.get('user', '')}
    return params


class Root(object):
    @cherrypy.expose
    def index(self):
        tmpl = ENV.get_template('index.html')
        params = get_params()
        return tmpl.render(params)

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': int(os.environ.get('PORT',
                                                                 '80'))})

cherrypy.quickstart(Root())
