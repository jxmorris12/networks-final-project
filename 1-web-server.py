# jack morris 11/13/16

# 1. Implement a base web-server that responds to all web request with a simple
# HTML page that says: 'Secret black Site' and displays the IP-Address of the requester.

# Python socket documentation: https://docs.python.org/3/library/socket.html
# Based off of the 'Echo Server Program' Python example.

# This script starts a server 

import errno
import signal
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 54321              # Arbitrary non-privileged port (port number > 1024)

HTML_BODY = 'Secret black Site<br>'
def HTML_RESPONSE(ip_address):
	HTML_RESPONSE = 'HTTP/1.0 200 OK\r\n'
	HTML_RESPONSE += 'Content-Type:text/html\r\n'
	HTML_RESPONSE += 'Connection:close\r\n\n'
	HTML_RESPONSE += '<html><head>' 
	HTML_RESPONSE += HTML_BODY
	HTML_RESPONSE += ip_address
	HTML_RESPONSE += '</head></html>\r\n'
	return HTML_RESPONSE

def create_server_socket():
	s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	return s

def wait_for_client(s):
	while True:
		try:
		  conn_sock, (src_ip, src_port) = s.accept()
		  conn_sock.sendall(HTML_RESPONSE(src_ip))
		  conn_sock.shutdown(socket.SHUT_WR)
		  # Why doesn't this work when I call conn_sock.close()?
		  # And why does each browser request happen twice?
		  print('Responded to', src_ip + ':' + str(src_port))
		except socket.error as (code, msg):
			exit(-1)


def handle_sigint(s):
	def handler(signum, frame):
		s.close()
		print '\nSocket closed.'
	signal.signal(signal.SIGINT, handler)
	print 'registered handler'

def main():
	socket = create_server_socket()
	handle_sigint(socket)
	wait_for_client(socket)

main()