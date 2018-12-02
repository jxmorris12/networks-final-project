import subprocess
from socket import *

serverName = 'localhost'
serverPort = 8000

windowSize = 1024*4

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send('Client printing messages'.encode())
message = clientSocket.recv(windowSize).decode()

while message != "exit":
	print(message)
	clientSocket.send('ACK'.encode())
	message = clientSocket.recv(windowSize).decode()

clientSocket.close()
print('Connection closed.')