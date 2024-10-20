# Fourier Transform Analysis of Audio Signals in Python

## Project Overview

The goal of this project is to develop a Python program that generates an audio signal (such as a sine wave, noise, or a combination of both) and applies the Fourier Transform to analyze its frequency components. The program uses NumPy and SciPy for performing Fast Fourier Transform (FFT) and Matplotlib for visualizing both the time-domain signal and its corresponding frequency spectrum.

This tool serves as an educational resource for EEE students, helping them understand the concepts of time-domain and frequency-domain analysis.

## Table of Contents
- [Libraries Required](#libraries-required)
- [How to Run the Program](#how-to-run-the-program)
- [Functionality](#functionality)
- [Files in this Repository](#files-in-this-repository)
  
## Libraries Required

- **NumPy**: For numerical operations and implementing FFT.
- **SciPy**: Provides additional signal processing functions (if required).
- **Matplotlib**: For visualizing the time-domain and frequency-domain signals.

### Install dependencies
You can install all the required libraries by running:

```bash
pip install -r requirements.txt
```
### How to Run the Program
```
python SignWave.py
python aduioInput.py
```
## Functionality
**1. Fourier Transform (FFT)**

   The program uses the Fast Fourier Transform (FFT) algorithm to convert the time-domain signal into its frequency-domain representation. This is essential for analyzing the different frequency components of the signal, making it easier to understand the underlying patterns.Steps are as follows:
    <br>**1.Generate a time-domain signal:** The user can create different signals such as a sine wave, noise, or a combination of both.
    Apply FFT: Using numpy.fft.fft(), the signal is transformed into its frequency components.For more information refer [Numpy.fft()](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html)
    <br>**2.Frequency spectrum:** The resulting frequency components are plotted against their respective frequencies, allowing users to observe which frequencies are present and their amplitudes.

Here is the code snippet for applying FFT:
```
import numpy as np

def apply_fft(signal, sampling_rate):
    
    fft_result = np.fft.fft(signal)
    freq_axis = np.fft.fftfreq(len(signal), 1 / sampling_rate)
    return fft_result, freq_axis
```
**2. Visualizing with Matplotlib**

To help students grasp the difference between time-domain and frequency-domain analysis, Matplotlib is used to visualize the results. The tool generates two plots:
Time-domain plot: Shows the amplitude of the signal over time.
Frequency-domain plot: Displays the magnitude of different frequency components.

Here is a code snippet how the matplotlib plots the graphs:
```
import matplotlib.pyplot as plt

Draw a line in a diagram from position (1, 3) to position (8, 10):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
```
## Files in this Repository
* _SignWave.py_ <br>
This script generates a sine wave with the following parameters:<br>
    **fs:** The sampling frequency, which determines how many samples per second are taken.<br>
    **t:** The time vector, which defines the duration of the signal (from 0 to 1 second with intervals of 1/fs).<br>
    **freq:** The frequency of the sine wave (set to 5 Hz).<br>
   **x:** The actual sine wave generated using NumPy's sine function, based on the given frequency.<br/>
**Output:**
  ![image](https://github.com/user-attachments/assets/f9be8eba-1984-4499-891f-cd1c820b1b38)

  This graph represents the frequency spectrum of a sample sine wave. The x-axis shows the frequency in Hertz (Hz), while the y-axis shows the amplitude of each frequency component. The plot features a prominent spike at a low frequency, indicating the dominant frequency of the sine wave. Since this is a pure sine wave, the spectrum shows only one significant frequency component, with no other frequencies contributing. The rest of the plot is flat, suggesting that no higher frequencies are present in the signal.

* _aduioInput.py_ <br>
  The reference aduio input file is collected from the link: [_Link_](https://xeno-canto.org/)<br>
  
  This script perform below operations

    perform_fft(signal):
  
      Computes the Fast Fourier Transform (FFT) of the input signal.

    plot_time_domain(signal, sample_rate):

      - Plots the audio signal in the time domain.

    plot_frequency_spectrum(fft_result, sample_rate):

      - Plots the magnitude of the FFT result in the frequency domain.

    plot_both(signal, fft_result, sample_rate):

      - Plots both the time-domain signal and frequency-domain spectrum side by side for easy comparison.<br/>
**Output:** <br>
    ![noiseGraph](https://github.com/user-attachments/assets/00484a46-8d5a-4023-a0b9-ff1d3e0085fb)
        <p style="text-align: center;">Time domain and Frequency spectrum of Noise after applying the FFT.</p>
    ![birdGraph](https://github.com/user-attachments/assets/c54efa54-fa6e-4cb4-b08b-c90f325f98fd)
        <p style="text-align: center;">Time domain and Frequency spectrum of Bird Sound after applying the FFT.</p>
        

