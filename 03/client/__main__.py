import json
import socket
import sys
import re

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print('''Command includes 2 arguments: ip-address [port]. 
    Default port = 7777''')
    sys.exit()
else:
    addr = sys.argv[1]
    if len(sys.argv) == 3:
        port = sys.argv[2]
        if port.isdigit():
            port = int(port)
        else:
            print('Port should be int')
            sys.exit()
    else: 
        port = 7777

regex = r"\d+(.)\d+(.)\d+(.)\d+"
right_addr = re.findall(regex, addr)
if len(right_addr) != 1:
    print('ip-address should be in format: d.d.d.d')
    sys.exit()

print(addr)
print(port)
socket = socket.socket()
socket.connect((addr, port))

action = input('Enter action: ')
data = input('Data: ')

request_string = json.dumps(
    {
        'action': action,
        'data': data
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
