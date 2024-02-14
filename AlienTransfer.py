# Setup server listening on ('localhost', 10000)
# receive data then send data back after XORing with the key
# attackthehumans
#
# If you get an address already in use error then try again in a few
# moments.
#
import socket

#set up tcp server on localhost at port 10000
host = 'localhost'
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print("Listening on port " + str(port))
while True:
    #accept connection
    conn, addr = s.accept()
    print("Connection from: " + str(addr))
    #receive data
    data = conn.recv(1024).decode()
    print("From client: " + str(data))
    #Xor data with key
    key = "attackthehumans"
    key = key.encode()
    data = data.encode()    
    result = bytearray()
    for i in range(len(data)):
        result.append(data[i] ^ key[i % len(key)])
    result = result.decode()
    print("XORed: " + str(result))
    #send data
    conn.send(result.encode())
    #recieve data
    data = conn.recv(1024).decode()
    print("From client: " + str(data))
    
