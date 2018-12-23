
Skip to content

    Why GitHub?
                          


                    
Business
Explore
                      

                    
Marketplace
Pricing
                       


                        

Sign in
Sign up

0
0

    0

Jargon314/Programming_Concept
Code
Issues 1
Pull requests 0
Projects 0
Insights
Join GitHub today

GitHub is home to over 28 million developers working together to host and review code, manage projects, and build software together.
Programming_Concept/python/Networking/basic.py
ed88320 on Jul 27
@Jargon314 Jargon314 added simple http request
33 lines (26 sloc) 1.85 KB
import socket 		#socket library containing modules


host = 'www.github.org'		# url or ip address
port = 80		#		Port that their HTTP server is running on 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# create the socket object

s.connect((host,port))		# connect to the host address and port

# New in python 3 must be a byte object to send it trhough socket 
# for python 3 it expects a byte object b = bytes_onject
#example  print(b'the string')
byte_string = b'GET / HTTP/1.1\r\nHost: www.github.com\r\n\r\n'		# byte encoded string HTTP GET Request
string = 'GET / HTTP/1.1\r\nHost: www.github.com\r\n\r\n'		# regular string works in python 2 without the bytes convertor b'string'
s.send(byte_string)		# send the byte_data over the socket 
print(s.recv(4096))		# print to the screen the received message 


s.close()		#dont forget to close the socket  when done receiving 

###################		DESCRIPTION OF WHATS HAPPENING HERE 		#########
#		First the client will establish or negotiate the 3 way handshake 
#		client sends the synchronization packet also known as the "syn packet "
#		server then send back a syn and ack packet or syn-ack  the ack packet is known as the acknowledgement packet 
#		The client then sends back the servers ack packet and the 3 way handshake is created 
#		Then we are able to send data between the sockets including HTTP GET requests
#		NOTE: if the port was 443 the port that SSL runs on then we would need to accept the key from the server to encrypt messages in order to connect
#		#####################		 FOR MORE INFO ON PYTHON AND THE WEB LOOK BELOW 		###########################
#		LINKS: 
#		
#		http://docs.python-requests.org/en/master/user/quickstart/
#		https://docs.python.org/3/library/http.client.html
##################################################################################################################################
