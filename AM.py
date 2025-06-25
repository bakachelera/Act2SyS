import numpy as np
import matplotlib.pyplot as plt

# Parámetros
Fs = 10000              # Frecuencia de muestreo (más alta)
T = 1                   # Duración en segundos
t = np.linspace(0, T, int(Fs*T), endpoint=False)

# Señal moduladora
fm = 10                 # Frecuencia moduladora en Hz
moduladora = np.sin(2 * np.pi * fm * t)

# Señal portadora
fc = 100                # Frecuencia portadora en Hz
portadora = np.cos(2 * np.pi * fc * t)

# Señal AM
x = (1 + moduladora) * portadora

# FFT
X = np.fft.fft(x)
freq = np.fft.fftfreq(len(x), 1/Fs)
X_mag = np.abs(X)

# Filtramos la mitad positiva del espectro y cerca de fc
idx = np.where((freq >= 0) & (freq <= 200))  # mostrar solo hasta 200 Hz

# Graficar
plt.figure(figsize=(12, 5))

plt.subplot(2, 1, 1)
plt.plot(t[:1000], x[:1000])  # Muestra solo una parte del tiempo
plt.title("Señal AM (dominio del tiempo)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(2, 1, 2)
plt.plot(freq[idx], X_mag[idx])
plt.title("FFT de la señal AM (espectro recortado)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")

plt.tight_layout()
plt.show()
