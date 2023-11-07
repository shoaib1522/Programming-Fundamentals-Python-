import numpy as np
import matplotlib.pyplot as plt

# Constants and component values
C1 = 4e-15
C2 = 255e-15
C3 = 45.5e-15
R1 = 440
R2 = 442
Zo = 440
er = 6.325
t1 = 1e-3
t2 = 11.4e-3
freqs = np.linspace(2e9, 16e9, 1000)

# Calculate the propagation constant (Beta)
c = 3e8 # speed of light in m/s
beta1 = 2 * np.pi * freqs * np.sqrt(er) / c * t1
beta2 = 2 * np.pi * freqs * np.sqrt(er) / c * t2

# Compute the input admittance (Yin) for the range of frequencies
Yin = np.zeros_like(freqs, dtype=np.complex128)
for i, freq in enumerate(freqs):
    Y_C1 = 1j * 2 * np.pi * freq * C1
    Y_C2 = 1j * 2 * np.pi * freq * C2
    Y_C3 = 1j * 2 * np.pi * freq * C3

Y_R1 = 1 / R1
Y_R2 = 1 / R2

Z1 = Zo * (1 + np.exp(-2j * beta1[i])) / (1 - np.exp(-2j * beta1[i]))
Z2 = Zo * (1 + np.exp(-2j * beta2[i])) / (1 - np.exp(-2j * beta2[i]))

Y1 = 1 / Z1
Y2 = 1 / Z2

Yin[i] = Y_C1 + (Y_C2 * Y_R1 * (Y1 + Y_R2) + Y1 * Y_R2 * Y_C3) / (Y_C2 + Y_R1 + Y1 + Y_R2 + Y_C3)

# Plot the real part of the input admittance (Re{Yin})
plt.plot(freqs / 1e9, np.real(Yin))
plt.yscale#39;log&#39;)
plt.xlabel#39;Frequency (GHz)&#39;)
plt.ylabel#39;Re{Yin}&#39;)
plt.grid()
plt.title#39;Real Part of Input Admittance vs. Frequency&#39;)
plt.show()