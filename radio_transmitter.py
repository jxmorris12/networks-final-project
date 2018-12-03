from playsounds import modulate_array
import bitarray
import time

def radio_transmit(s):
    ba = bitarray.bitarray()
    ba.frombytes(s.encode('utf-8'))
    for i in range(0, 30):
        modulate_array(ba.tolist())
        time.sleep(10)
    return 'ACK'

#radio_transmit('Hi')