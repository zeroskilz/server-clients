#!/usr/bin/python
import socket
import sys
import time
import os

def socketThread():
    print("setting socket and host info : ")
# script arguments

    if len(sys.argv)>2:
        port = str(sys.argv[2])
        host = str(sys.argv[1])

    else:
        usage = '''
        usage: python server.py arg[1] arg[2]
        or:    python server.py host port

        open up a socket and stream data over tcp sockets
        defaulting to 0.0.0.0 and port 4201
        '''
        print usage

        host = '0.0.0.0'
        port = 4201


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
    conn, addr = soc.accept()

    conn.send('You are connected to Host : %s running on port %s : ' %(str(host), str(port)))
    global conn

    return sendData(conn)
def sendData(conn):
    while True:

        try:
            data = conn.recv(4096)
            print(data)

            if not data:
                print socket.errno
                return

            elif 'file' not in data:

                conn.send ("you sent the string %s :" %(data))
                conn.send("Your connected to the simple server :" )



            elif 'file' in data:

                return fileTransfer(data)

        except socket.error as msg:
                print msg






def fileTransfer(data):

        print data

        sendFile = (data)
        sendFile = sendFile.strip("file ")
        sendFile = sendFile.strip('\n')
        pathexist = os.path.isfile(sendFile)
        print data
        if pathexist == False:
            conn.send("no file by that name")
            return socketThread()
        else:

            with open(sendFile, 'r') as fd:
                if(fd):
                    print "sending data"
                    dataFile = fd.read()
                    print dataFile
                    conn.send(dataFile)
                    print "sending file complete"
                    pass
                    return

                else:
                    print "exiting"
                    return




while (1):
    if __name__ == '__main__':
        socketThread()
    #if conn:
      #  sendData()
    #else:
     #   print socket.errno


