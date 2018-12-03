import subprocess
from packetizer import packetize
from radio_transmitter import radio_transmit
from socket import *

serverName = 'localhost'
serverPort = 54321

windowSize = 1024*4

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('Client connected to server. Awaiting messages...')
clientSocket.send('Client printing messages'.encode())
message = clientSocket.recv(windowSize).decode()

while message != "exit":
	print(message)
	packet = packetize(message)
	print("Transmitting packet: '" + packet + "'")
	radio_transmit(packet)
	clientSocket.send('ACK'.encode())
	message = clientSocket.recv(windowSize).decode()

clientSocket.close()
print('Connection closed.')