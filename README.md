### Mini Internet

This repository contains source code for our Networks Final Project. All code is runnable using Python 3. You might need to install some packages, including `numpy` and `sounddevice`. Our project consists of five parts:

1. An HTTP server that responds to web requests with a "Secret Black Site." The server is implemented in the runnable script `web_server.py`. Run it and connect to `localhost:80` to see the site.

2. A DNS server that routes the URL `blacksite.secret` to our localhost server. The DNS server is all in `dns_serrver.py`, a runnable script. Don't forget to add the `localhost` DNS server to your machine. This is `dns_server.py`.

3. The TCP client and server. In this model, the "server" sends commands to the "client" which then broadcasts them via an FM transmitter connected directly to the soundcard. (Eventually, this signal will be able to be demodulated and displayed using `receiver.py` and helper code in `radio_receiver.py` and `demod.py`. We didn't finish this part yet.)

The TCP server runs as `tcp_server.py` and takes text input to send strings to the client. The TCP client is `tcp_client.py`. Make sure that the server is started before the client and the host and port strings are properly set at the top of each file. The client should display the strings it receives from the server. It then converts the strings to bytes and broadcasts them through the soundcard and FM transmitter (code in `playsounds.py` and `radio_transmitter.py`).

4. The TCP client converts each string into a packet structure before broadcast. Each packet contains a header length, checksum hash (generated with MD5), and total packet size. This code is in `packetizer.py`.

5. Before sending the payload, the TCP client encrypts it using a one time pad. The one time pad will be shared between the receiver and the TCP client for secure communication. The code for generating a one time pad and using it for encryption and decryption is in `one_time_pad.py`.