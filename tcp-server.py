from socket import *

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Awaiting message to send to server")
connectionSocket, addr = serverSocket.accept()
print("Connected to client " + str(addr))
message = connectionSocket.recv(1024)
print(message)
command = ""
while command != "exit":
	command = input("Please enter a command (or 'exit' to exit): ")
	connectionSocket.send(command.encode())
	message = connectionSocket.recv(1024)
	print(message)

connectionSocket.close()
print('Connection closed.')