import numpy as np
import matplotlib
#matplotlib.use("TkAgg")
import matplotlib.pyplot as plt



time = np.load("time_points.npy")
energy = np.load("energy_ccsd.npy")
#dipole = np.load("0.001dir0.npy")

plt.figure()
plt.subplot(211)
plt.plot(time, energy.real, label=r"First deriv real")
plt.grid()
plt.subplot(212)
plt.plot(time, energy.imag, label=r"First deriv imag")
plt.grid()
plt.show()


#plt.figure()
##plt.plot(time, energy, label = "cc2")
#plt.title(r"Fourier transform of $\langle z(t)\rangle$")
#plt.legend()
#plt.xlabel("frequency/au")
#plt.show()

#omega = 0.1
#dt = 1e-1

#print(2 * np.pi / omega)

#after_pulse = int((2 * np.pi / omega)/ dt)

#print(time)
#print(after_pulse)

#time_2 = time[after_pulse:]
#energy_2 = energy[after_pulse:]

#plt.figure()
#plt.plot(time_2, energy_2, label = "cc2")
#plt.legend()
#plt.xlabel("frequency/au")
#plt.show()
