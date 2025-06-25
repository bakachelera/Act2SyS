import numpy as np
import matplotlib.pyplot as plt

# Parámetros
Fs = 1000
T = 1
f = 5
t = np.linspace(0, T, int(Fs*T), endpoint=False)

# Señal senoidal
x = np.sin(2 * np.pi * f * t)

# Transformada de Fourier
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(X), 1/Fs)

# Solo la mitad positiva
half = len(X)//2
X_mag = np.abs(X[:half])
X_phase = np.angle(X[:half])
frequencies = frequencies[:half]

# Gráficas
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Señal Senoidal de 5 Hz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')

plt.subplot(3, 1, 2)
plt.stem(frequencies, X_mag)
plt.title('Espectro de Magnitud')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|X(f)|')

plt.subplot(3, 1, 3)
plt.stem(frequencies, X_phase)
plt.title('Fase de la Transformada de Fourier')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')

plt.tight_layout()
plt.show()
