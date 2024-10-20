import numpy as np
import matplotlib.pyplot as plt

fs = 1000                              #  Sampling frequency
t = np.arange(0, 1, 1/fs)              # Time vector
freq = 5                               # Frequency of the sine wave
x = np.sin(2 * np.pi * freq * t)

                                       # Compute the Fourier Transforms
X = np.fft.fft(x)
N = len(X)
n = np.arange(N)
T = N/fs
freq = n/T


# Plot the frequency spectrum
plt.figure(figsize=(12, 6))
plt.plot(freq[:N//2], np.abs(X)[:N//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum of a Sample Sine Wave')
plt.grid()
plt.show()