import socket
from io import BytesIO
import gzip

host = 'localhost'
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#send "GET_KEY" to server
s.connect((host,port))
s.sendall(b"GET_KEY")
#recieve data from server
data = s.recv(1024)
#decode data from gzip
data = gzip.decompress(data)
read_data = BytesIO(data)
