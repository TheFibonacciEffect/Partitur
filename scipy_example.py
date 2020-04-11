#from os.path import dirname, join as pjoin
from scipy.io import wavfile

samplerate, data = wavfile.read(r"Partitur\528hz Pure tone No Music-IMeusltcDGM.wav")
print(f"number of channels = {data.shape[1]}")

length = data.shape[0] / samplerate
print(f"length = {length}s")

import matplotlib.pyplot as plt
import numpy as np
time = np.linspace(0., length, data.shape[0])

plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")

plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()