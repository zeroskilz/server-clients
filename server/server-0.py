#!/usr/bin/python
import socket
import sys

print("setting socket and host info : ")
port = str(sys.argv[2])
host = str(sys.argv[1])

if host != '' :
    print("Server Running Host %s port %s : "  %(str(host) , str(port)) )
else:
    host="0.0.0.0"

print host
print("server : %s port : %s : "  %(str(host) ,str(port)))
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((host, int(port)))
soc.listen(1)
conn, addr = soc.accept()
print( conn.recv(4096))
conn.send('You are connected to Host : %s running on port %s : ' %(str(host), str(port)))

while True:

    try:
        data = conn.recv(4096)
        data.strip("\n")
        print("sent %s :  %s : " %(data, str(data)))
        conn.send("Your connected to the simple server : " )


    except socket.error as msg:
        conn.close()

