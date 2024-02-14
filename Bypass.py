# #connect on tcp to services.cyberprotection.agency at port 13880

# import socket

# host = 'services.cyberprotection.agency'
# port = 13880
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((host,port))
# print("Connected to server")
# data = s.recv(1024).decode()
# print("From server: " + str(data))
# #send blank string repeatedly until server sends that does not contain "Password:"

# while "Password:" in data:
#     s.send("".encode())
#     data = s.recv(1024).decode()
#     print("From server: " + str(data))
#     if "Password:" not in data:
#         #wait for keypress
#         input("Press Enter to continue...")
#         continue

#use netcat to connect to services.cyberprotection.agency at port 13880
#send blank string repeatedly until server sends that does not contain "Password:"
#wait for keypress









