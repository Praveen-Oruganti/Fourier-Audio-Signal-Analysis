import numpy as np

fs = 1000                              #  Sampling frequency
t = np.arange(0, 1, 1/fs)              # Time vector
freq = 5                               # Frequency of the sine wave
x = np.sin(2 * np.pi * freq * t)

                                       # Compute the Fourier Transform
X = np.fft.fft(x)
N = len(X)
n = np.arange(N)
T = N/fs
freq = n/T

