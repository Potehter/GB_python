import json
import socket
from datetime import datetime
import logging
#from .log import client_log_config

logger = logging.getLogger('app.client')
socket = socket.socket()
socket.connect(('localhost', 8888))

action = input('Enter action: ')
data = input('Data: ')

request_string = json.dumps(
    {
        'action': action,
        'time': datetime.now().timestamp(),
        'data': data,
    }
)

socket.send(request_string.encode())
while True:
    response = socket.recv(1024)

    if response:

        logger.info(
            response.decode()
        )

        socket.close()

        break
