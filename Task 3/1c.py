# 1.Write a program to create a server that listens to port 53 using Stream sockets. Write a simple client program to connect to the server . Send a simple text message  "HELLO" from the client  to the server and close the connection.
# client

import socket

c = socket.socket()
c.connect_ex(("localhost", 53))
c.sendall(b"HELLO THERE!")
