# Import socket module
from socket import *
import requests
import json
import sys	

serverName=input("Server Name/IP: ")
serverPort=int(input("Server Port: "))
fileName=input("File to get from server: ")
fileToWrite=input("File to write data from server: ")

sock = socket(AF_INET,SOCK_STREAM)		#creates client socket(sock), 1st parameter indicates network is using IPv4 and 2nd indicates socket type is TCP.
sock.connect((serverName, serverPort))	#Initiates TCP connection and establishes it after three-way handshaking. 

url = "GET /" + fileName + " HTTP/1.0" 
url = url + """
Host:""" + serverName +""" 
Email: khatris1@hawkmail.newpaltz.edu 
User-agent: Python """ + str(sys.version_info[0])

sock.send(url.encode()) 			# Sends the socket through the client's socket and into the TCP connection. 

try:
    with open(fileToWrite, 'wb') as f: 
        while True:
            data = sock.recv(1024)
            if not data:
                break
            f.write(data)
            print(bytes.decode(data))

except IOError:
    a1="HTTP/1.1 404 Not Found\r\n\r\n"
    a2="<html><head></head><body><h1>404 Not Found - Please Check your filename!</h1></body></html>\r\n"
    print(a1.encode())
    print(a2.encode())
sock.close()
