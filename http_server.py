### http_server_template.py

import socket
from socket import *    
import sys

intPort = int(input("Please enter port number: "))
serverSocket = socket(AF_INET, SOCK_STREAM)		# Creates TCP socket

serverSocket.bind(('', intPort))	# Associates the server port number "intPort" with this socket		
print ('starting up on port')
serverSocket.listen(1)
	
while True:
    print ('Ready to serve...')
    
    connectionSocket, client_address = serverSocket.accept()	# server listens for a TCP connection requests from client 
    
    try:
        message =  connectionSocket.recv(1024)
        message = bytes.decode(message)
		
        fServerLog = open("server.log", "a+")
        request_method = message.split(' ')[0]
        if 'Python 3' in message:
            fServerLog.write(message + " " + "HTTP/1.0\n\n")		
        else:
            fServerLog.write(message + '\n')	
        fServerLog.close()
        print (message)
        response = "HTTP/1.1 200 OK"
        connectionSocket.send(response.encode())

        filename = message
        if len(message)>1:
            filename = message.split()[1]
        	
        #file=""+filename.decode("utf-8") 
        file=filename[1:len(filename)]

        #In Chrome browser it sends two Requests at Server 
        if file == "favicon.ico":
            continue
        #print(file)
		
        fo = open(file, "r+") #r+ is read for reading and writing
        str = fo.read();
        fo.close()
        for i in range(0,len(str)):
            connectionSocket.send(str[i].encode())
			
        
        connectionSocket.close()
        
    except IOError:
        # Send HTTP response message for file not found
        a1="HTTP/1.1 404 Not Found\r\n\r\n"
        a2="<html><head></head><body><h1>404 Not Found - Please Check your filename!</h1></body></html>\r\n"
        connectionSocket.send(a1.encode())
        connectionSocket.send(a2.encode())
        
        connectionSocket.close()
        break
    
# close the server socket
serverSocket.close()
                


