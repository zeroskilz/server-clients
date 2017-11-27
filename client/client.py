import socket

port = 4201
host = '127.0.0.1'
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host,port))

while True:
    buf = raw_input("Send Buffer : ")
    str(buf)
    pay = soc.send(buf)
    data = soc.recv(4096)

    soc.close()
