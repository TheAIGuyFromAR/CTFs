#
# Connect to alien server ('localhost', 10000)
#
# Then send each of these values...
# USER
# aliensignal
# PASS
# unlockserver
# SEND
# moonbase
# END
# ...and receive the response from each.
#
# Note: You must receive data back from the server after you send each value
#

import socket
data = ""
def main(user,alien_signal,passw,unlock_server,send,moonbase,end):
    host = 'localhost'
    port = 10000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    print("Connected to server")
    #send 
    s.send(user.encode())
    data = s.recv(1024).decode()
    print("From server: " + str(data))
    #send
    s.send(alien_signal.encode())
    data = s.recv(1024).decode()
    print("From server: " + str(data))
    #send
    s.send(passw.encode())
    data = s.recv(1024).decode()
    print("From server: " + str(data))
    #send
    s.send(unlock_server.encode())
    data = s.recv(1024).decode()
    print("From server: " + str(data))
    #send
    s.send(send.encode())
    data = s.recv(1024).decode()
    print("From server: " + str(data))
    #send
    s.send(moonbase.encode())
    data = s.recv(1024).decode()
    print("From server: " + str(data))
    #send
    s.send(end.encode())
    data = s.recv(1024).decode()
    print("From server: " + str(data))
    #close connection
    s.close()
    return data

if __name__ == '__main__':
    
    main("USER","aliensignal","PASS","unlockserver","SEND","moonbase","END")
    print(data)