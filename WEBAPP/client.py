#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8089                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close