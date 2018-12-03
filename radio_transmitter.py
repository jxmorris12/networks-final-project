from playsounds import modulate_array
import bitarray
import time

def radio_transmit(str):
    ba = bitarray.bitarray()
    ba.frombytes(str.encode('utf-8'))
    for i in range(0, 30):
        modulate_array(ba.tolist())
        time.sleep(10)

#radio_transmit('Hi')