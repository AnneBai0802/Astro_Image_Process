#select .wav file, read and plot
#calculate Fourier Transform and display absolute value 0-500 Hz

from scipy.io.wavfile import read
import numpy as np
import plotdata

filename = "signal.wav" #edit filename as appropriate

# read audio samples
input_data = read(filename)
signal = input_data[1]
sampling_freq = input_data[0]
time = np.arange(len(signal))/sampling_freq
freq = 0.5 * sampling_freq * np.linspace(-1.0, 1.0, len(signal))
FTdata = np.fft.fftshift(np.fft.fft(np.fft.fftshift(signal)))
fundamental_freq = freq[list(abs(FTdata)).index(np.max(abs(FTdata)))]

plotdata.plot_data(time,signal,0,9) #plot signal in time window defined by 2 values
plotdata.plot_data(freq,abs(FTdata),0,1000)

print('Fundamental frequecy is', abs(fundamental_freq), 'Hz')