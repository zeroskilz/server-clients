import socket

port = 4201
host = '127.0.0.1'
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host,port))
