import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as writer

# IQ_samples = np.loadtxt("audio.txt", dtype=complex)
# print(IQ_samples)
# demodulated = np.angle(IQ_samples[1:]*np.conjugate(IQ_samples[:-1]))
# result = demodulated[::4]
#
# print(len(result))
# rate = 2400000
# writer.write("signal3.wav", rate, result)
# plt.plot(result)
# plt.show()

def demodulate(IQ_samples):
    demodulated = np.angle(IQ_samples[1:] * np.conjugate(IQ_samples[:-1]))
    #result = demodulated[::4]
    result = demodulated
    return result


def write_to_audio(demod_sample):
    rate = 2400000
    writer.write("signal3.wav", rate, demod_sample)


def write_to_txt(demod_sample):
    np.savetxt('audio.txt', demod_sample)


def plot_t(demod_sample):
    plt.plot(demod_sample)
    plt.show()

