import numpy as np
import matplotlib.pyplot as plt
# Parámetros 
fs = 5000
t = np.linspace(0, 1, fs, endpoint=False)  # Tiempo
fm = 5  # Frecuencia de la señal mensaje 
fc = 100  # Frecuencia de la portadora
Ac = 1  #amplitud

# Crear una señal de mensaje binaria (1s y 0s representados como amplitudes)
bits = [1, 0, 1, 1, 0]
samples_per_bit = fs // len(bits)
bit_signal = np.repeat(bits, samples_per_bit)
bit_signal = bit_signal[:len(t)]
m_t = bit_signal * 0.9  # asi se ve mas bonito
# Portadora
c_t = Ac * np.cos(2 * np.pi * fc * t)
# Señal AM modulada
s_t = (1 + m_t) * c_t
# Graficar 
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, m_t, label='Mensaje (0s y 1s)', color='orange')
plt.title("Señal de mensaje binaria (modulada en amplitud)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(t, s_t, label='Señal AM', color='blue')
plt.title("Señal modulada en amplitud (AM)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
