#
# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory
#
#connect to server
#send command to server
#recieve data from server
#display data from server
#
import socket
import subprocess
import sys
import time


HOST = 'localhost'
PORT = 10000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #send command to server
    s.sendall(b"ls /tmp")
    #recieve data from server
    data = s.recv(1024)
    
print(f"Received {data!r}")
