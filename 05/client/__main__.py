import json
import socket
from datetime import datetime


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

        print(
            response.decode()
        )

        socket.close()

        break
