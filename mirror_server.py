#
# Send server ('localhost', 10000) GET_KEY to retrieve key,
# user needs to reverse and send back to server to get flag.
# It will change each execution so the
# user can not manually achieve this.
#

import socket
import subprocess

HOST = '127.0.0.1'
PORT = 10000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #send command to server
    s.sendall(b"GET_KEY")
    #recieve data from server
    data = s.recv(1024)
    #decode data
    data = data.decode('utf-8')
    #reverse data
    data = data[::-1]
    #send reversed data back to server
    s.sendall(data.encode())
    #recieve data from server
    data = s.recv(1024)
    #decode data
    data = data.decode('utf-8')
    #print data
    print(data)
    
