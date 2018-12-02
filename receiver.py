# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:02:27 2018

@author: Gautam K
"""

import socket
import sys
from rtlsdr import *


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 4000))

# client class
class TCPclient():
    def __init__(self, socket, address):
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent:', self.sock.recvfrom(1024).decode())
            self.sock.send('Test')

# server listening to FM 87.7 on port 4000
ss.listen(4)
print ('Server started and listening')
while 1:
    print('Test')
    try:
        print('Test')
        (clientsocket, address) = ss.accept()
        TCPclient = RtlSdrTcpClient(hostname='localhost', port=4000)
        TCPclient.center_freq = 87.7e6
        data = TCPclient.read_samples()
        print ("Connection Made")
        print(data)
        ss.close()
    except KeyboardInterrupt:
        print ('', 'Interrupted')
        sys.exit(0)