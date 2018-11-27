# jack morris 11/13/16

# 1. Implement a base web-server that responds to all web request with a simple
# HTML page that says: 'Secret black Site' and displays the IP-Address of the requester.

# Python socket documentation: https://docs.python.org/3/library/socket.html
# Based off of the 'Echo Server Program' Python example.

# This script starts a server 

import errno
import signal
import socket

HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces
PORT = 3333  # Arbitrary non-privileged port (port number > 1024)

HTML_BODY = 'Secret black Site<br>'


def html_response(ip_address):
    html_message = 'HTTP/1.0 200 OK\r\n'
    html_message += 'Content-Type:text/html\r\n'
    html_message += 'Connection:close\r\n\n'
    html_message += '<html><head>'
    html_message += HTML_BODY
    html_message += ip_address
    html_message += '</head></html>\r\n'
    return html_message


def create_server_socket():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    return s


def wait_for_client(s):
    while True:
        try:
            conn_sock, (src_ip, src_port) = s.accept()
            conn_sock.sendall(html_response(src_ip).encode())
            conn_sock.shutdown(socket.SHUT_WR)
            # Why doesn't this work when I call conn_sock.close()?
            # And why does each browser request happen twice?
            print('Responded to', src_ip + ':' + str(src_port))
        except socket.error:
            exit(-1)


def handle_sigint(s):
    def handler(signum, frame):
        s.close()
        print('\nSocket closed.')
    signal.signal(signal.SIGINT, handler)
    print('registered handler')


def main():
    server_socket = create_server_socket()
    handle_sigint(server_socket)
    wait_for_client(server_socket)


main()
