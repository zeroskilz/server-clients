#!/usr/bin/python
import socket
import sys
import os

def socketConnect():
    global soc

    port = 4201
    host = '127.0.0.1'
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((host,port))


def sendData():
    try:
        buf = raw_input("Send Buffer : ")
        buf = str(buf)
        pay = soc.send(buf)
        data = soc.recv(4096)
        if 'file' in buf:
            print("caught keyword activating fileSave function")
            return fileSave(data)

    except socket.error as msg:
        print msg
        return

def fileSave(data): # accept argument of file path
    try:
        with open('testFile.tmp', 'w') as fd: # open file for writting
            print("data in transmission")
            while (fd):  # loop to catch data
                data = soc.recv(4096)
                print("data = %s : " %data)

                if not data:
                    break

                else:
                    fd.write(data)
                    print " data download fin"

                return socketConnect()
    except socket.error as msg:
        print msg
        return socketConnect()


    except socket.error as msg:
        print msg
        return

socketConnect()
while (1):
    sendData()










