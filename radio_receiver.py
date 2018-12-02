from pylab import *
from rtlsdr import RtlSdr
import rtlsdr
from demod import demodulate, write_to_audio, write_to_txt, plot_t


def test_device():
    print(rtlsdr.librtlsdr)
    print(rtlsdr.librtlsdr.rtlsdr_get_device_count())


# samples 5 seconds of signal and write to txt and audio
def read_n_plot():
    sdr = RtlSdr()
    # configure device
    sdr.sample_rate = 2.4e6
    sdr.center_freq = 90e6
    sdr.gain = 4
    samples = sdr.read_samples(12000*1024)
    sdr.close()
    demod_result = demodulate(samples)

    write_to_txt(demod_result)
    write_to_audio(demod_result)
    plot_t(demod_result)

    # use matplotlib to estimate and plot the PSD
    psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
    xlabel('Frequency (MHz)')
    ylabel('Relative power (dB)')
    show()


def async_callback(samples, sdr):
    result = demodulate(samples)
    print(len(result))


def stream_radio():
    sdr = RtlSdr()
    sdr.sample_rate = 2.4e6
    sdr.center_freq = 90e6
    sdr.gain = 4
    sdr.read_samples_async(async_callback)

test_device()
read_n_plot()