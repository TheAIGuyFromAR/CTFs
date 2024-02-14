


#access services.cyberprotection.agency at port 9999  and recieve three numbers
#add the three numbers together and send the result back to the server

import socket

host = 'services.cyberprotection.agency'
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
#    while True:
data = s.recv(1024).decode()

print("From server: " + str(data))
data = data.split()
print(data)
added = int(data[0]) * int(data[1])
print(added)
divided = added // int(data[2])
result = str(divided)
print(result)
s.send(result.encode())
ans = s.recv(1024).decode()
print(ans)
s.close()