import sounddevice as sd
import numpy as np

def play_sound(data_array):
    rate = 24000
    sd.play(data_array, rate)


data_array = []
for i in range(0,99):
    data_array.append(np.float(3))

i=1
while i:
    play_sound(data_array)
    print(i)
    i += 1