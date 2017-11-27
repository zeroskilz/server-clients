# Server and client applications written in python commin soon

### here are some useful commands with netcat while working with clients and servers

#### netcat listen on specified port with verbose
		* nc -l -vv -p 4444

#### connet using netcat
		* nc 127.0.0.1 4444

#### send file or echo data to remote host with netcat using pipeline

		* echo hello | nc -l -p 4444
#### to accept and write to file do 
		* nc 127.0.0.1 4444 >> tmpfile



# Some Bugs
    *have to reconnect client multiple times after file transfer in order to transfer messages!

    
