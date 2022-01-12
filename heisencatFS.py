# Publish a virtual structure
import logging
import sys

import wsgidav.wsgidav_app
from heisenburg_fs.heisenburg_fs_provider import HeisenburgFSProvider
from cheroot.wsgi import Server as WSGIServer
from cheroot.wsgi import PathInfoDispatcher as WSGIPathInfoDispatcher

if __name__ == '__main__':

    heisenburgFS = HeisenburgFSProvider()

    config = {
        "host": "0.0.0.0",
        "http_authenticator": {
            "domain_controller": None
        },
        "simple_dc": {
            "user_mapping": {
                "*": True
            }
        },
        "port": 8086,
        "provider_mapping": {
            "/": heisenburgFS
        },
        "verbose": 5,
        "logging": {
            "enable_loggers": ["wsgidav", "util", "request_server", "request_resolver"]
        }
    }

    logger = logging.getLogger("wsgidav")
    app = wsgidav.wsgidav_app.WsgiDAVApp(config)
    d = WSGIPathInfoDispatcher({'/': app})
    server = WSGIServer(('0.0.0.0', 8086),d)
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()