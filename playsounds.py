import numpy as np 
# import sounddevice as sd
# import scipy.io.wavfile as wav
# import matplotlib.pyplot as plt
import scikits.audiolab
from demod import *


AUDIO_SAMPLE_RATE = 44100  # Hz




# generate a tone of the given duration (in seconds) at the given frequency
def gen_tone(amplitude,tone_duration, frequency):
    x = np.arange(AUDIO_SAMPLE_RATE)
    tone = amplitude*np.sin(2 * np.pi * frequency/AUDIO_SAMPLE_RATE * x)
    
    return tone


def play(tone):
    scikits.audiolab.play(tone, fs=AUDIO_SAMPLE_RATE)
    # print(type(tone[0]))
    # sd.play(tone, AUDIO_SAMPLE_RATE)

#fSK modulation 
def modulateFSK(array, tone1, tone2): 
    for i in array: 
        if i == 1: 
            play(tone1)
        else:
            play(tone2)


def main():
    tone1 = gen_tone(100,1, 100)
    tone2 = gen_tone(100,1, 900)
    
    while True:
        print("Please enter Message")
        message = input()
        array = [1, 1, 0, 0, 1]
        modulateFSK(array, tone1, tone2)

if __name__ == '__main__':
    main()