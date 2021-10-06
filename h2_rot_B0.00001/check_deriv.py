import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#after_deriv = np.load()


deriv = np.load('0.001dir0.npy') 
time_points = np.arange(len(deriv))

plt.figure()
plt.subplot(211)
plt.plot(time_points, deriv.real, label=r"$\Re(\langle \hat{H}(t) \rangle)$")
plt.grid()
plt.subplot(212)
plt.plot(time_points, deriv.imag, label=r"$\Im(\langle \hat{H}(t) \rangle)$")
plt.grid()
plt.show()
