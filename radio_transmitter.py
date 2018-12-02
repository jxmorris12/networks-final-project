import sounddevice as sd
import numpy as np
from demod import *


def play_sound(data_array):
    rate = 24000
    sd.play(data_array, rate)


def write_test_wav():
    rate = 2400000
    a = np.empty(rate * 5)
    a.fill(5)
    write_to_audio(a, 'test.wav')