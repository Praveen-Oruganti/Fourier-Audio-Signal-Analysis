import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def perform_fft(signal):
    return np.fft.fft(signal)

def plot_time_domain(signal, sample_rate):
    plt.figure(figsize=(10, 4))
    time_axis = np.arange(len(signal)) / sample_rate
    plt.plot(time_axis, signal)
    plt.title("Time Domain Signal")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

def plot_frequency_spectrum(fft_result, sample_rate):
    # Compute frequency bins
    freqs = np.fft.fftfreq(len(fft_result), 1/sample_rate)
    magnitude = np.abs(fft_result)
    
    # Only plot positive frequencies (real world signals are symmetric)
    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:len(freqs)//2], magnitude[:len(magnitude)//2])
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.show()

def plot_both(signal, fft_result, sample_rate):
    # Plot time domain and frequency domain side by side
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))

    # Time domain plot
    time_axis = np.arange(len(signal)) / sample_rate
    ax[0].plot(time_axis, signal)
    ax[0].set_title("Time Domain  Signal of Bird ")
    ax[0].set_xlabel("Time [s]")
    ax[0].set_ylabel("Amplitude")
    ax[0].grid(True)

    # Frequency domain plot
    freqs = np.fft.fftfreq(len(fft_result), 1/sample_rate)
    magnitude = np.abs(fft_result)
    ax[1].plot(freqs[:len(freqs)//2], magnitude[:len(magnitude)//2])
    ax[1].set_title("Frequency Spectrum of Bird")
    ax[1].set_xlabel("Frequency [Hz]")
    ax[1].set_ylabel("Magnitude")
    ax[1].grid(True)

    plt.tight_layout()
    plt.show()

# Example usage: Read any WAV audio file of any duration
audio_file = 'Greater_Coucal.29sljpaq.wav'  # Path to your audio file
sample_rate, signal = wavfile.read(audio_file)

# If the audio file is stereo (2 channels), take one channel for simplicity
if len(signal.shape) > 1:
    signal = signal[:, 0]  # Use the first channel

# Perform FFT on the signal
fft_result = perform_fft(signal)

# Plot time-domain and frequency-domain signals
plot_both(signal, fft_result, sample_rate)
