import json
import socket
from datetime import datetime
import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default = 7777, type = int)
    parser.add_argument('-a', '--addr', default = '')
 
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])


sock = socket.socket()
sock.bind((namespace.addr, namespace.port))
sock.listen(5)

while True:
    client, address = sock.accept()
    print(address)
    print('Client detected: ' +  str(address))
    data = client.recv(1024)
    request = json.loads(
        data.decode('utf-8')
    )
    status = (200, 'OK')
    if request.get('action') == 'get_time':
        date = datetime.now()
        response_string = date.strftime('%d-%m-%yT%H:%M:%S')

    elif request.get('action') == 'upper_text':
        client_data = request.get('data')
        response_string = client_data.upper()
    else:
        response_string = 'Wrong action'
        status = (404, 'NOT_FOUND')
    response_json = json.dumps(
        {
        'status': status,
        'body': response_string
        }
    )
    client.send(response_json.encode('utf-8'))
    client.close()


