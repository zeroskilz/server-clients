#!/usr/bin/python
import socket

def socketConnect():
    global soc
    global data
    port = 4201
    host = '127.0.0.1'
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((host,port))


def sendData():
    buf = raw_input("Send Buffer : ")
    buf = str(buf)
    pay = soc.send(buf)
    data = soc.recv(4096)
    if 'file' in buf:
        print("caught keyword activating fileSave function")
        return fileSave(data)

def fileSave(data): # accept argument of file path
    fd = open('testFile.tmp', 'w') # open file for writting
    while True:  # loop to catch data
        print("data in transmission")
        data = soc.recv(4096)
        print("data = %s : " %data)
        if not data:
            break
        fd.write(data)
    fd.close()
    print("File Transfer Complete exiting function:")

socketConnect()
while (1):
    sendData()










