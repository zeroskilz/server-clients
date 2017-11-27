#!/usr/bin/python
import socket
import sys

def socket_thread():
    print("setting socket and host info : ")
# script arguments

    if len(sys.argv)>=2:
        port = str(sys.argv[2])
        host = str(sys.argv[1])

    else:
        usage = '''
        usage: python server.py arg[1] arg[2]
        or:    python server.py host port

        open up a socket and stream data over tcp sockets
        '''
        print usage
        exit()


    if host != '' :
        print("Server Running Host %s port %s : "  %(str(host) ,str(port)))
    else:
        host="0.0.0.0"

    print host
    print("server : %s port : %s : "  %(str(host) ,str(port)))

# setup socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# attempt to make sock halt TIME_WAIT and reuse socket
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    soc.bind((host, int(port)))
    soc.listen(1)
    global conn
    conn, addr = soc.accept()
    print( conn.recv(4096))
    conn.send('You are connected to Host : %s running on port %s : ' %(str(host), str(port)))

def sendData():
    while True:


        try:
            data = conn.recv(4096)
            print(data)

            if not data:
                print socket.errno
                return main()

            elif data != 'file':
                conn.send ("you sent the string %s :" %(data))
                conn.send("Your connected to the simple server : \n" )

            elif file in command:
                data = data.strip('file :')
                conn.sendall(data)
                return data

        except socket.error as msg:
            conn.close()

def fileTransfer(data):
    print data
    sendFile = str(data)
    fd = open(sendFile, 'r')
    data = fd.read()
    conn.sendall(data)
    return main

main()
if conn:

    sendData()
else:
    print socket.errno


