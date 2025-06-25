import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
Fs = 1000      # Frecuencia de muestreo en Hz
T = 1          # Duración total de la señal en segundos
t = np.linspace(0, T, int(Fs*T), endpoint=False)  # Vector de tiempo

# Pulso rectangular: duración 0.2s dentro del segundo
x = np.where((t >= 0.4) & (t <= 0.6), 1.0, 0.0)  # Pulso entre 0.4 y 0.6

# Transformada de Fourier
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(X), 1/Fs)

# Tomar solo la mitad positiva del espectro
half = len(X) // 2
X_mag = np.abs(X[:half])
X_phase = np.angle(X[:half])
frequencies = frequencies[:half]

# Graficar la señal en el tiempo
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title("Pulso Rectangular")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Graficar la magnitud del espectro
plt.subplot(3, 1, 2)
plt.plot(frequencies, X_mag)
plt.title("Espectro de Magnitud")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")

# Graficar la fase
plt.subplot(3, 1, 3)
plt.plot(frequencies, X_phase)
plt.title("Espectro de Fase")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (radianes)")

plt.tight_layout()
plt.show()
