import numpy as np
import matplotlib.pyplot as plt

def compute_fft(f1=50, f2=120, fs=1000, T=1):
    # Time array
    t = np.linspace(0, T, int(fs * T), endpoint=False)
    
    # Define the signal
    s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    
    # Compute the FFT
    N = len(s)
    fft_values = np.fft.fft(s)
    fft_freqs = np.fft.fftfreq(N, 1/fs)
    
    # Compute the magnitude spectrum
    magnitude = np.abs(fft_values) / N
    
    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(fft_freqs[:N//2], magnitude[:N//2])  # Only plot the positive frequencies
    plt.title('Magnitude Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()

# Call the function
compute_fft()
