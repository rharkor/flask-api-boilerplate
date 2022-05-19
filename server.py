from flask import Flask
from flask_cors import CORS

import config

server = Flask(__name__)
server.debug = config.DEBUG


CORS(
    server,
    resources={r"/*": {"origins": "*"}},
    headers=['Content-Type', 'X-Requested-With', 'Authorization']
)

from routes.common import common_blueprint
server.register_blueprint(common_blueprint)


if __name__ == '__main__':
    if config.HOST == '0.0.0.0':
        print(f'Server is running at http://127.0.0.1:{config.PORT}')
    print(f'Server is running at http://{config.HOST}:{config.PORT}')
    server.run(host=config.HOST, port=config.PORT)
