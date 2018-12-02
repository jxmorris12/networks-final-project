from playsounds import modulate_array
import bitarray

def radio_transmit(str):
    ba = bitarray.bitarray()
    ba.frombytes(str.encode('utf-8'))
    modulate_array(ba.tolist())

radio_transmit('Hi')