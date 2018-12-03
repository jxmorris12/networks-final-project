import subprocess
from radio_transmitter import radio_transmit
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
	message = clientSocket.recv(windowSize).decode()
	ack = radio_transmit(message)
	clientSocket.send(ack.encode())

clientSocket.close()
print('Connection closed.')