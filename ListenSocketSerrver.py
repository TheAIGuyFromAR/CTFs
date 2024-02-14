
# The aliens seem to be trying to make direct contact, so it's time
# for us to properly listen.
# Write a server that listens on ('localhost', 10000).
# The flag will be sent to that address.
# Record signal to /tmp/aliensignallog.txt
#
# If you get an address already in use error then try again in a few
# moments.
#
import socket


#socket server that listens

def main():
    host = 'localhost'
    port = 10000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)
    while True:
        c, addr = s.accept()
        print("Connection from: " + str(addr))
        #recieve data from client and store in /tmp/aliensignallog.txt
        data = c.recv(1024).decode()
        if not data:
            break
        with open('/tmp/aliensignallog.txt', 'w') as f:
            f.write(data)
            
        c.send("You have connected to the server".encode())
        c.close()

if __name__ == '__main__':
    main()


  