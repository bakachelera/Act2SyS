import numpy as np
import matplotlib.pyplot as plt

# Parámetros
Fs = 1000      # Frecuencia de muestreo en Hz
T = 1          # Duración total en segundos
t = np.linspace(0, T, int(Fs*T), endpoint=False)

# Señal escalón unitario: 0 antes de t=0.5, 1 después
x = np.where(t >= 0.5, 1.0, 0.0)

# Transformada de Fourier
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(X), 1/Fs)

# Solo la mitad positiva del espectro
half = len(X) // 2
X_mag = np.abs(X[:half])
X_phase = np.angle(X[:half])
frequencies = frequencies[:half]

# Graficar
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title("Función Escalón Unitario")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(3, 1, 2)
plt.plot(frequencies, X_mag)
plt.title("Espectro de Magnitud")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")

plt.subplot(3, 1, 3)
plt.plot(frequencies, X_phase)
plt.title("Espectro de Fase")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (radianes)")

plt.tight_layout()
plt.show()
