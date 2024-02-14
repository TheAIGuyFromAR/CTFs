# We need you to write a script which can connect over TCP to the following server - localhost:10000 and send 'GET' to retrieve the encrypted messages. You then need to decrypt them and send them back split by \n. We think you'll receive 3 sentences, and that they're encrypted with a caesar cipher with a different random offset per sentence.

# Finally, print the response after sending the decrypted messages to get the flag.

# Tip: Remember, each encrypted message has a different random offset.

import socket
import subprocess

HOST = '127.0.0.1'
PORT = 10000  # The port used by the server
method = "GET"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #send command to server
    s.sendall(method.encode())
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

#split data into three strings
data = data.split('\n')
string1 = data[0]
string2 = data[1]
string3 = data[2]

print(string1)
print(string2)
print(string3)
